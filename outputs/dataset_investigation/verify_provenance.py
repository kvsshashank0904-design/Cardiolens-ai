"""Reproduce content comparisons from saved public source snapshots; no training or source writes.
Run: python -B outputs/dataset_investigation/verify_provenance.py
"""
import csv
import hashlib
import io
import json
import zipfile
from collections import Counter, defaultdict
from decimal import Decimal
from pathlib import Path

OUT=Path(__file__).resolve().parent
SOURCE=Path(r'C:\Users\DELL\Desktop\DSAI SOCIETY\heart.csv')
ANCHORS=['age','sex','trestbps','chol','fbs','thalach','exang','oldpeak']

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def run():
    for entry in json.loads((OUT/'sources/source_manifest.json').read_text()):
        assert sha(OUT/'sources'/entry['file'])==entry['sha256'], 'Reference snapshot changed'
    original=SOURCE.read_bytes()
    with zipfile.ZipFile(OUT/'sources/kaggle_version2.zip') as z:
        reference=z.read('heart.csv')
    assert original==reference, 'Kaggle version 2 does not byte-match local CSV'
    reader=csv.reader(io.StringIO(original.decode('utf-8-sig'),newline=''))
    headers=next(reader); previous=reader.line_num
    records=[]
    for n,r in enumerate(reader,1):
        records.append({'values':dict(zip(headers,r)),'record_number':n,'line_start':previous+1,'line_end':reader.line_num})
        previous=reader.line_num
    buckets=defaultdict(list)
    for r in records: buckets[tuple(r['values'][f] for f in headers)].append(r)
    uci=[dict(zip(headers,r)) for r in csv.reader((OUT/'sources/uci_cleveland.data').read_text().splitlines())]
    key=lambda r:tuple(Decimal(r[f]) for f in ANCHORS)
    lookup=defaultdict(list)
    for n,r in enumerate(uci,1): lookup[key(r)].append((n,r))
    matched=[]; maps={f:Counter() for f in ['cp','restecg','slope','ca','thal','target']}
    used=set()
    for copies in buckets.values():
        r=copies[0]['values']; matches=lookup[key(r)]
        assert len(matches)==1, 'Missing or ambiguous upstream anchor match'
        line,u=matches[0]; used.add(line)
        group_id=hashlib.sha256(json.dumps([headers[:-1],[r[f] for f in headers[:-1]]],separators=(',',':')).encode()).hexdigest()
        matched.append({'group_id':group_id,'uci_physical_line':line,'multiplicity':len(copies),
                        'local_values':r,'uci_values_num_named_target_for_comparison':u,
                        'source_occurrences':[{k:v for k,v in x.items() if k!='values'} for x in copies]})
        for f in maps: maps[f][(u[f],r[f])]+=1
    # Derived mappings must be deterministic for each observed upstream code.
    conversion={}
    for field,pairs in maps.items():
        conversion[field]={}
        for (up,local),count in pairs.items():
            assert up not in conversion[field] or conversion[field][up]==local
            conversion[field][up]=local
    for m in matched:
        u=m['uci_values_num_named_target_for_comparison']; l=m['local_values']
        for field in headers:
            transformed=conversion[field][u[field]] if field in conversion else u[field]
            assert Decimal(transformed)==Decimal(l[field]), 'Full transformed record mismatch'
    assert len(matched)==len(used)==302 and len(records)==1025
    evidence={'source_sha256':sha(SOURCE),'kaggle_version_2_byte_identical':True,
        'anchor_fields':ANCHORS,'method':'Exact numeric matching on eight anchor fields; target and recoded fields excluded from matching. Every local distinct record has exactly one UCI candidate. Mappings inferred afterward and all 14 values checked. This verifies correspondence, not historical custody or author intent.',
        'local_rows':len(records),'distinct_local_records':len(matched),'uci_records':len(uci),
        'multiplicity_histogram':dict(sorted(Counter(len(v) for v in buckets.values()).items())),
        'derived_uci_to_local_mapping':conversion,
        'mapping_counts_distinct_records':{f:[{'uci_code':up,'local_code':local,'distinct_records':n} for (up,local),n in pairs.items()] for f,pairs in maps.items()},
        'unmatched_uci_records':[{'line':n,'values':r} for n,r in enumerate(uci,1) if n not in used],
        'sentinel_correspondences':{},'matched_records':matched}
    for field,code in [('ca','4'),('thal','0')]:
        selected=[m for m in matched if m['local_values'][field]==code]
        assert all(m['uci_values_num_named_target_for_comparison'][field]=='?' for m in selected)
        evidence['sentinel_correspondences'][field]={'local_code':code,'uci_code':'?',
            'distinct_records':len(selected),'original_rows':sum(m['multiplicity'] for m in selected)}
    (OUT/'record_correspondence.json').write_text(json.dumps(evidence,indent=2)+'\n',encoding='utf-8')
    before=json.loads((OUT/'integrity_before.json').read_text())
    errors=[]
    for name,h in before.items():
        path=SOURCE if name=='SOURCE_CSV' else OUT.parent/name
        if not path.is_file() or sha(path)!=h:errors.append('Changed: '+name)
    result={'status':'FAIL' if errors else 'PASS','errors':errors,
        'protected_artifacts_checked':len(before)-1,'source_sha256':sha(SOURCE),
        'kaggle_version_2_exact_byte_match':True,'uci_unique_anchor_matches':len(matched),
        'full_transformed_record_matches':len(matched),'models_trained':0,'source_or_experiment_changes':False if not errors else 'see errors'}
    (OUT/'investigation_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    print('Derived mappings:',conversion)
    print('Sentinels:',evidence['sentinel_correspondences'])
    assert not errors

if __name__=='__main__': run()
