# Complete duplicate-group details

CSV-aware parsing, UTF-8 with optional BOM. Header excluded. Record numbers are 1-based logical records after header, including blank/malformed records. Physical line numbers are 1-based and include header; quoted multiline fields retain start/end lines. Blank records and malformed-width records are separately reported and excluded from column/group denominators.

Exact duplicates match every parsed cell string including target. Feature-only duplicates match all columns except target; labels are compared separately. Original whitespace is retained. Additional copies = sum(group size - 1); participating records includes first occurrences. No rows are deleted. Groups appear in first-occurrence order.

Feature-only groups include groups that are also exact duplicates. They are not an additional disjoint set of duplicates.

## Exact duplicates (all columns)

### Group 1 — 4 occurrences

Key: `{"age": "52", "sex": "1", "cp": "0", "trestbps": "125", "chol": "212", "fbs": "0", "restecg": "1", "thalach": "168", "exang": "0", "oldpeak": "1", "slope": "2", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 1 | 2 | 2 |
| 635 | 636 | 636 |
| 672 | 673 | 673 |
| 864 | 865 | 865 |

### Group 2 — 4 occurrences

Key: `{"age": "53", "sex": "1", "cp": "0", "trestbps": "140", "chol": "203", "fbs": "1", "restecg": "0", "thalach": "155", "exang": "1", "oldpeak": "3.1", "slope": "0", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 2 | 3 | 3 |
| 693 | 694 | 694 |
| 814 | 815 | 815 |
| 969 | 970 | 970 |

### Group 3 — 4 occurrences

Key: `{"age": "70", "sex": "1", "cp": "0", "trestbps": "145", "chol": "174", "fbs": "0", "restecg": "1", "thalach": "125", "exang": "1", "oldpeak": "2.6", "slope": "0", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 3 | 4 | 4 |
| 841 | 842 | 842 |
| 885 | 886 | 886 |
| 949 | 950 | 950 |

### Group 4 — 4 occurrences

Key: `{"age": "61", "sex": "1", "cp": "0", "trestbps": "148", "chol": "203", "fbs": "0", "restecg": "1", "thalach": "161", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 4 | 5 | 5 |
| 520 | 521 | 521 |
| 524 | 525 | 525 |
| 596 | 597 | 597 |

### Group 5 — 3 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "138", "chol": "294", "fbs": "1", "restecg": "1", "thalach": "106", "exang": "0", "oldpeak": "1.9", "slope": "1", "ca": "3", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 5 | 6 | 6 |
| 623 | 624 | 624 |
| 789 | 790 | 790 |

### Group 6 — 3 occurrences

Key: `{"age": "58", "sex": "0", "cp": "0", "trestbps": "100", "chol": "248", "fbs": "0", "restecg": "0", "thalach": "122", "exang": "0", "oldpeak": "1", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 6 | 7 | 7 |
| 664 | 665 | 665 |
| 962 | 963 | 963 |

### Group 7 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "114", "chol": "318", "fbs": "0", "restecg": "2", "thalach": "140", "exang": "0", "oldpeak": "4.4", "slope": "0", "ca": "3", "thal": "1", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 7 | 8 | 8 |
| 151 | 152 | 152 |
| 662 | 663 | 663 |
| 1014 | 1015 | 1015 |

### Group 8 — 4 occurrences

Key: `{"age": "55", "sex": "1", "cp": "0", "trestbps": "160", "chol": "289", "fbs": "0", "restecg": "0", "thalach": "145", "exang": "1", "oldpeak": "0.8", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 8 | 9 | 9 |
| 279 | 280 | 280 |
| 448 | 449 | 449 |
| 786 | 787 | 787 |

### Group 9 — 4 occurrences

Key: `{"age": "46", "sex": "1", "cp": "0", "trestbps": "120", "chol": "249", "fbs": "0", "restecg": "0", "thalach": "144", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 9 | 10 | 10 |
| 44 | 45 | 45 |
| 539 | 540 | 540 |
| 916 | 917 | 917 |

### Group 10 — 4 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "122", "chol": "286", "fbs": "0", "restecg": "0", "thalach": "116", "exang": "1", "oldpeak": "3.2", "slope": "1", "ca": "2", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 10 | 11 | 11 |
| 220 | 221 | 221 |
| 552 | 553 | 553 |
| 590 | 591 | 591 |

### Group 11 — 4 occurrences

Key: `{"age": "71", "sex": "0", "cp": "0", "trestbps": "112", "chol": "149", "fbs": "0", "restecg": "1", "thalach": "125", "exang": "0", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 11 | 12 | 12 |
| 402 | 403 | 403 |
| 501 | 502 | 502 |
| 649 | 650 | 650 |

### Group 12 — 4 occurrences

Key: `{"age": "43", "sex": "0", "cp": "0", "trestbps": "132", "chol": "341", "fbs": "1", "restecg": "0", "thalach": "136", "exang": "1", "oldpeak": "3", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 12 | 13 | 13 |
| 371 | 372 | 372 |
| 553 | 554 | 554 |
| 611 | 612 | 612 |

### Group 13 — 3 occurrences

Key: `{"age": "34", "sex": "0", "cp": "1", "trestbps": "118", "chol": "210", "fbs": "0", "restecg": "1", "thalach": "192", "exang": "0", "oldpeak": "0.7", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 13 | 14 | 14 |
| 16 | 17 | 17 |
| 780 | 781 | 781 |

### Group 14 — 3 occurrences

Key: `{"age": "51", "sex": "1", "cp": "0", "trestbps": "140", "chol": "298", "fbs": "0", "restecg": "1", "thalach": "122", "exang": "1", "oldpeak": "4.2", "slope": "1", "ca": "3", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 14 | 15 | 15 |
| 483 | 484 | 484 |
| 788 | 789 | 789 |

### Group 15 — 4 occurrences

Key: `{"age": "52", "sex": "1", "cp": "0", "trestbps": "128", "chol": "204", "fbs": "1", "restecg": "1", "thalach": "156", "exang": "1", "oldpeak": "1", "slope": "1", "ca": "0", "thal": "0", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 15 | 16 | 16 |
| 687 | 688 | 688 |
| 735 | 736 | 736 |
| 894 | 895 | 895 |

### Group 16 — 3 occurrences

Key: `{"age": "51", "sex": "0", "cp": "2", "trestbps": "140", "chol": "308", "fbs": "0", "restecg": "0", "thalach": "142", "exang": "0", "oldpeak": "1.5", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 17 | 18 | 18 |
| 933 | 934 | 934 |
| 1005 | 1006 | 1006 |

### Group 17 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "124", "chol": "266", "fbs": "0", "restecg": "0", "thalach": "109", "exang": "1", "oldpeak": "2.2", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 18 | 19 | 19 |
| 830 | 831 | 831 |
| 929 | 930 | 930 |

### Group 18 — 3 occurrences

Key: `{"age": "50", "sex": "0", "cp": "1", "trestbps": "120", "chol": "244", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "1.1", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 19 | 20 | 20 |
| 32 | 33 | 33 |
| 908 | 909 | 909 |

### Group 19 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "2", "trestbps": "140", "chol": "211", "fbs": "1", "restecg": "0", "thalach": "165", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 20 | 21 | 21 |
| 87 | 88 | 88 |
| 407 | 408 | 408 |
| 1007 | 1008 | 1008 |

### Group 20 — 3 occurrences

Key: `{"age": "60", "sex": "1", "cp": "2", "trestbps": "140", "chol": "185", "fbs": "0", "restecg": "0", "thalach": "155", "exang": "0", "oldpeak": "3", "slope": "1", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 21 | 22 | 22 |
| 244 | 245 | 245 |
| 685 | 686 | 686 |

### Group 21 — 3 occurrences

Key: `{"age": "67", "sex": "0", "cp": "0", "trestbps": "106", "chol": "223", "fbs": "0", "restecg": "1", "thalach": "142", "exang": "0", "oldpeak": "0.3", "slope": "2", "ca": "2", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 22 | 23 | 23 |
| 548 | 549 | 549 |
| 983 | 984 | 984 |

### Group 22 — 3 occurrences

Key: `{"age": "45", "sex": "1", "cp": "0", "trestbps": "104", "chol": "208", "fbs": "0", "restecg": "0", "thalach": "148", "exang": "1", "oldpeak": "3", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 23 | 24 | 24 |
| 266 | 267 | 267 |
| 914 | 915 | 915 |

### Group 23 — 3 occurrences

Key: `{"age": "63", "sex": "0", "cp": "2", "trestbps": "135", "chol": "252", "fbs": "0", "restecg": "0", "thalach": "172", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 24 | 25 | 25 |
| 318 | 319 | 319 |
| 826 | 827 | 827 |

### Group 24 — 3 occurrences

Key: `{"age": "42", "sex": "0", "cp": "2", "trestbps": "120", "chol": "209", "fbs": "0", "restecg": "1", "thalach": "173", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 25 | 26 | 26 |
| 387 | 388 | 388 |
| 563 | 564 | 564 |

### Group 25 — 4 occurrences

Key: `{"age": "61", "sex": "0", "cp": "0", "trestbps": "145", "chol": "307", "fbs": "0", "restecg": "0", "thalach": "146", "exang": "1", "oldpeak": "1", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 26 | 27 | 27 |
| 116 | 117 | 117 |
| 589 | 590 | 590 |
| 777 | 778 | 778 |

### Group 26 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "2", "trestbps": "130", "chol": "233", "fbs": "0", "restecg": "1", "thalach": "179", "exang": "1", "oldpeak": "0.4", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 27 | 28 | 28 |
| 808 | 809 | 809 |
| 829 | 830 | 830 |

### Group 27 — 4 occurrences

Key: `{"age": "58", "sex": "0", "cp": "1", "trestbps": "136", "chol": "319", "fbs": "1", "restecg": "0", "thalach": "152", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "2", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 28 | 29 | 29 |
| 391 | 392 | 392 |
| 424 | 425 | 425 |
| 912 | 913 | 913 |

### Group 28 — 4 occurrences

Key: `{"age": "56", "sex": "1", "cp": "2", "trestbps": "130", "chol": "256", "fbs": "1", "restecg": "0", "thalach": "142", "exang": "1", "oldpeak": "0.6", "slope": "1", "ca": "1", "thal": "1", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 29 | 30 | 30 |
| 339 | 340 | 340 |
| 406 | 407 | 407 |
| 718 | 719 | 719 |

### Group 29 — 4 occurrences

Key: `{"age": "55", "sex": "0", "cp": "0", "trestbps": "180", "chol": "327", "fbs": "0", "restecg": "2", "thalach": "117", "exang": "1", "oldpeak": "3.4", "slope": "1", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 30 | 31 | 31 |
| 510 | 511 | 511 |
| 610 | 611 | 611 |
| 987 | 988 | 988 |

### Group 30 — 4 occurrences

Key: `{"age": "44", "sex": "1", "cp": "0", "trestbps": "120", "chol": "169", "fbs": "0", "restecg": "1", "thalach": "144", "exang": "1", "oldpeak": "2.8", "slope": "0", "ca": "0", "thal": "1", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 31 | 32 | 32 |
| 94 | 95 | 95 |
| 122 | 123 | 123 |
| 781 | 782 | 782 |

### Group 31 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "130", "chol": "131", "fbs": "0", "restecg": "1", "thalach": "115", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 33 | 34 | 34 |
| 883 | 884 | 884 |
| 926 | 927 | 927 |

### Group 32 — 3 occurrences

Key: `{"age": "70", "sex": "1", "cp": "2", "trestbps": "160", "chol": "269", "fbs": "0", "restecg": "1", "thalach": "112", "exang": "1", "oldpeak": "2.9", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 34 | 35 | 35 |
| 313 | 314 | 314 |
| 593 | 594 | 594 |

### Group 33 — 3 occurrences

Key: `{"age": "50", "sex": "1", "cp": "2", "trestbps": "129", "chol": "196", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 35 | 36 | 36 |
| 134 | 135 | 135 |
| 736 | 737 | 737 |

### Group 34 — 3 occurrences

Key: `{"age": "46", "sex": "1", "cp": "2", "trestbps": "150", "chol": "231", "fbs": "0", "restecg": "1", "thalach": "147", "exang": "0", "oldpeak": "3.6", "slope": "1", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 36 | 37 | 37 |
| 83 | 84 | 84 |
| 410 | 411 | 411 |

### Group 35 — 3 occurrences

Key: `{"age": "51", "sex": "1", "cp": "3", "trestbps": "125", "chol": "213", "fbs": "0", "restecg": "0", "thalach": "125", "exang": "1", "oldpeak": "1.4", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 37 | 38 | 38 |
| 715 | 716 | 716 |
| 839 | 840 | 840 |

### Group 36 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "138", "chol": "271", "fbs": "0", "restecg": "0", "thalach": "182", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 38 | 39 | 39 |
| 660 | 661 | 661 |
| 880 | 881 | 881 |

### Group 37 — 3 occurrences

Key: `{"age": "64", "sex": "1", "cp": "0", "trestbps": "128", "chol": "263", "fbs": "0", "restecg": "1", "thalach": "105", "exang": "1", "oldpeak": "0.2", "slope": "1", "ca": "1", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 39 | 40 | 40 |
| 643 | 644 | 644 |
| 984 | 985 | 985 |

### Group 38 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "2", "trestbps": "128", "chol": "229", "fbs": "0", "restecg": "0", "thalach": "150", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 40 | 41 | 41 |
| 478 | 479 | 479 |
| 707 | 708 | 708 |
| 828 | 829 | 829 |

### Group 39 — 3 occurrences

Key: `{"age": "65", "sex": "0", "cp": "2", "trestbps": "160", "chol": "360", "fbs": "0", "restecg": "0", "thalach": "151", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 41 | 42 | 42 |
| 420 | 421 | 421 |
| 752 | 753 | 753 |

### Group 40 — 4 occurrences

Key: `{"age": "54", "sex": "1", "cp": "2", "trestbps": "120", "chol": "258", "fbs": "0", "restecg": "0", "thalach": "147", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 42 | 43 | 43 |
| 154 | 155 | 155 |
| 158 | 159 | 159 |
| 674 | 675 | 675 |

### Group 41 — 4 occurrences

Key: `{"age": "61", "sex": "0", "cp": "0", "trestbps": "130", "chol": "330", "fbs": "0", "restecg": "0", "thalach": "169", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 43 | 44 | 44 |
| 671 | 672 | 672 |
| 760 | 761 | 761 |
| 925 | 926 | 926 |

### Group 42 — 4 occurrences

Key: `{"age": "55", "sex": "0", "cp": "1", "trestbps": "132", "chol": "342", "fbs": "0", "restecg": "1", "thalach": "166", "exang": "0", "oldpeak": "1.2", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 45 | 46 | 46 |
| 137 | 138 | 138 |
| 264 | 265 | 265 |
| 303 | 304 | 304 |

### Group 43 — 3 occurrences

Key: `{"age": "42", "sex": "1", "cp": "0", "trestbps": "140", "chol": "226", "fbs": "0", "restecg": "1", "thalach": "178", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 46 | 47 | 47 |
| 907 | 908 | 908 |
| 1002 | 1003 | 1003 |

### Group 44 — 4 occurrences

Key: `{"age": "41", "sex": "1", "cp": "1", "trestbps": "135", "chol": "203", "fbs": "0", "restecg": "1", "thalach": "132", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "1", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 47 | 48 | 48 |
| 133 | 134 | 134 |
| 771 | 772 | 772 |
| 797 | 798 | 798 |

### Group 45 — 4 occurrences

Key: `{"age": "66", "sex": "0", "cp": "0", "trestbps": "178", "chol": "228", "fbs": "1", "restecg": "1", "thalach": "165", "exang": "1", "oldpeak": "1", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 48 | 49 | 49 |
| 230 | 231 | 231 |
| 453 | 454 | 454 |
| 945 | 946 | 946 |

### Group 46 — 4 occurrences

Key: `{"age": "66", "sex": "0", "cp": "2", "trestbps": "146", "chol": "278", "fbs": "0", "restecg": "0", "thalach": "152", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 49 | 50 | 50 |
| 62 | 63 | 63 |
| 205 | 206 | 206 |
| 396 | 397 | 397 |

### Group 47 — 4 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "117", "chol": "230", "fbs": "1", "restecg": "1", "thalach": "160", "exang": "1", "oldpeak": "1.4", "slope": "2", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 50 | 51 | 51 |
| 239 | 240 | 240 |
| 748 | 749 | 749 |
| 992 | 993 | 993 |

### Group 48 — 3 occurrences

Key: `{"age": "58", "sex": "0", "cp": "3", "trestbps": "150", "chol": "283", "fbs": "1", "restecg": "0", "thalach": "162", "exang": "0", "oldpeak": "1", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 51 | 52 | 52 |
| 764 | 765 | 765 |
| 849 | 850 | 850 |

### Group 49 — 3 occurrences

Key: `{"age": "57", "sex": "0", "cp": "0", "trestbps": "140", "chol": "241", "fbs": "0", "restecg": "1", "thalach": "123", "exang": "1", "oldpeak": "0.2", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 52 | 53 | 53 |
| 941 | 942 | 942 |
| 964 | 965 | 965 |

### Group 50 — 8 occurrences

Key: `{"age": "38", "sex": "1", "cp": "2", "trestbps": "138", "chol": "175", "fbs": "0", "restecg": "1", "thalach": "173", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "4", "thal": "2", "target": "1"}`

Target counts: {'1': 8}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 53 | 54 | 54 |
| 84 | 85 | 85 |
| 209 | 210 | 210 |
| 243 | 244 | 244 |
| 341 | 342 | 342 |
| 466 | 467 | 467 |
| 598 | 599 | 599 |
| 971 | 972 | 972 |

### Group 51 — 4 occurrences

Key: `{"age": "49", "sex": "1", "cp": "2", "trestbps": "120", "chol": "188", "fbs": "0", "restecg": "1", "thalach": "139", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "3", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 54 | 55 | 55 |
| 401 | 402 | 402 |
| 516 | 517 | 517 |
| 519 | 520 | 520 |

### Group 52 — 4 occurrences

Key: `{"age": "55", "sex": "1", "cp": "0", "trestbps": "140", "chol": "217", "fbs": "0", "restecg": "1", "thalach": "111", "exang": "1", "oldpeak": "5.6", "slope": "0", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 55 | 56 | 56 |
| 56 | 57 | 57 |
| 614 | 615 | 615 |
| 834 | 835 | 835 |

### Group 53 — 3 occurrences

Key: `{"age": "56", "sex": "1", "cp": "3", "trestbps": "120", "chol": "193", "fbs": "0", "restecg": "0", "thalach": "162", "exang": "0", "oldpeak": "1.9", "slope": "1", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 57 | 58 | 58 |
| 946 | 947 | 947 |
| 1008 | 1009 | 1009 |

### Group 54 — 3 occurrences

Key: `{"age": "48", "sex": "1", "cp": "1", "trestbps": "130", "chol": "245", "fbs": "0", "restecg": "0", "thalach": "180", "exang": "0", "oldpeak": "0.2", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 58 | 59 | 59 |
| 325 | 326 | 326 |
| 753 | 754 | 754 |

### Group 55 — 4 occurrences

Key: `{"age": "67", "sex": "1", "cp": "2", "trestbps": "152", "chol": "212", "fbs": "0", "restecg": "0", "thalach": "150", "exang": "0", "oldpeak": "0.8", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 59 | 60 | 60 |
| 242 | 243 | 243 |
| 431 | 432 | 432 |
| 698 | 699 | 699 |

### Group 56 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "1", "trestbps": "154", "chol": "232", "fbs": "0", "restecg": "0", "thalach": "164", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 60 | 61 | 61 |
| 498 | 499 | 499 |
| 882 | 883 | 883 |
| 988 | 989 | 989 |

### Group 57 — 4 occurrences

Key: `{"age": "29", "sex": "1", "cp": "1", "trestbps": "130", "chol": "204", "fbs": "0", "restecg": "0", "thalach": "202", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 61 | 62 | 62 |
| 65 | 66 | 66 |
| 119 | 120 | 120 |
| 669 | 670 | 670 |

### Group 58 — 3 occurrences

Key: `{"age": "67", "sex": "1", "cp": "0", "trestbps": "100", "chol": "299", "fbs": "0", "restecg": "0", "thalach": "125", "exang": "1", "oldpeak": "0.9", "slope": "1", "ca": "2", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 63 | 64 | 64 |
| 212 | 213 | 213 |
| 296 | 297 | 297 |

### Group 59 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "2", "trestbps": "150", "chol": "212", "fbs": "1", "restecg": "1", "thalach": "157", "exang": "0", "oldpeak": "1.6", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 64 | 65 | 65 |
| 196 | 197 | 197 |
| 294 | 295 | 295 |

### Group 60 — 4 occurrences

Key: `{"age": "59", "sex": "1", "cp": "3", "trestbps": "170", "chol": "288", "fbs": "0", "restecg": "0", "thalach": "159", "exang": "0", "oldpeak": "0.2", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 66 | 67 | 67 |
| 415 | 416 | 416 |
| 799 | 800 | 800 |
| 863 | 864 | 864 |

### Group 61 — 3 occurrences

Key: `{"age": "53", "sex": "1", "cp": "2", "trestbps": "130", "chol": "197", "fbs": "1", "restecg": "0", "thalach": "152", "exang": "0", "oldpeak": "1.2", "slope": "0", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 67 | 68 | 68 |
| 128 | 129 | 129 |
| 554 | 555 | 555 |

### Group 62 — 4 occurrences

Key: `{"age": "42", "sex": "1", "cp": "0", "trestbps": "136", "chol": "315", "fbs": "0", "restecg": "1", "thalach": "125", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "0", "thal": "1", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 68 | 69 | 69 |
| 608 | 609 | 609 |
| 835 | 836 | 836 |
| 999 | 1000 | 1000 |

### Group 63 — 3 occurrences

Key: `{"age": "37", "sex": "0", "cp": "2", "trestbps": "120", "chol": "215", "fbs": "0", "restecg": "1", "thalach": "170", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 69 | 70 | 70 |
| 85 | 86 | 86 |
| 331 | 332 | 332 |

### Group 64 — 3 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "160", "chol": "164", "fbs": "0", "restecg": "0", "thalach": "145", "exang": "0", "oldpeak": "6.2", "slope": "0", "ca": "3", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 70 | 71 | 71 |
| 394 | 395 | 395 |
| 527 | 528 | 528 |

### Group 65 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "170", "chol": "326", "fbs": "0", "restecg": "0", "thalach": "140", "exang": "1", "oldpeak": "3.4", "slope": "0", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 71 | 72 | 72 |
| 166 | 167 | 167 |
| 682 | 683 | 683 |

### Group 66 — 4 occurrences

Key: `{"age": "61", "sex": "1", "cp": "0", "trestbps": "140", "chol": "207", "fbs": "0", "restecg": "0", "thalach": "138", "exang": "1", "oldpeak": "1.9", "slope": "2", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 72 | 73 | 73 |
| 405 | 406 | 406 |
| 821 | 822 | 822 |
| 877 | 878 | 878 |

### Group 67 — 4 occurrences

Key: `{"age": "56", "sex": "1", "cp": "0", "trestbps": "125", "chol": "249", "fbs": "1", "restecg": "0", "thalach": "144", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 73 | 74 | 74 |
| 165 | 166 | 166 |
| 188 | 189 | 189 |
| 412 | 413 | 413 |

### Group 68 — 4 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "140", "chol": "177", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 74 | 75 | 75 |
| 319 | 320 | 320 |
| 521 | 522 | 522 |
| 557 | 558 | 558 |

### Group 69 — 4 occurrences

Key: `{"age": "48", "sex": "1", "cp": "0", "trestbps": "130", "chol": "256", "fbs": "1", "restecg": "0", "thalach": "150", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 75 | 76 | 76 |
| 113 | 114 | 114 |
| 312 | 313 | 313 |
| 622 | 623 | 623 |

### Group 70 — 3 occurrences

Key: `{"age": "47", "sex": "1", "cp": "2", "trestbps": "138", "chol": "257", "fbs": "0", "restecg": "0", "thalach": "156", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 76 | 77 | 77 |
| 104 | 105 | 105 |
| 139 | 140 | 140 |

### Group 71 — 3 occurrences

Key: `{"age": "48", "sex": "1", "cp": "2", "trestbps": "124", "chol": "255", "fbs": "1", "restecg": "1", "thalach": "175", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "2", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 77 | 78 | 78 |
| 462 | 463 | 463 |
| 756 | 757 | 757 |

### Group 72 — 4 occurrences

Key: `{"age": "63", "sex": "1", "cp": "0", "trestbps": "140", "chol": "187", "fbs": "0", "restecg": "0", "thalach": "144", "exang": "1", "oldpeak": "4", "slope": "2", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 78 | 79 | 79 |
| 93 | 94 | 94 |
| 181 | 182 | 182 |
| 765 | 766 | 766 |

### Group 73 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "1", "trestbps": "134", "chol": "201", "fbs": "0", "restecg": "1", "thalach": "158", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 79 | 80 | 80 |
| 80 | 81 | 81 |
| 898 | 899 | 899 |

### Group 74 — 3 occurrences

Key: `{"age": "50", "sex": "1", "cp": "2", "trestbps": "140", "chol": "233", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 81 | 82 | 82 |
| 911 | 912 | 912 |
| 958 | 959 | 959 |

### Group 75 — 4 occurrences

Key: `{"age": "49", "sex": "1", "cp": "2", "trestbps": "118", "chol": "149", "fbs": "0", "restecg": "0", "thalach": "126", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "3", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 82 | 83 | 83 |
| 227 | 228 | 228 |
| 237 | 238 | 238 |
| 836 | 837 | 837 |

### Group 76 — 4 occurrences

Key: `{"age": "44", "sex": "1", "cp": "1", "trestbps": "120", "chol": "220", "fbs": "0", "restecg": "1", "thalach": "170", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 86 | 87 | 87 |
| 308 | 309 | 309 |
| 515 | 516 | 516 |
| 731 | 732 | 732 |

### Group 77 — 3 occurrences

Key: `{"age": "59", "sex": "0", "cp": "0", "trestbps": "174", "chol": "249", "fbs": "0", "restecg": "1", "thalach": "143", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 88 | 89 | 89 |
| 437 | 438 | 438 |
| 637 | 638 | 638 |

### Group 78 — 4 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "140", "chol": "268", "fbs": "0", "restecg": "0", "thalach": "160", "exang": "0", "oldpeak": "3.6", "slope": "0", "ca": "2", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 89 | 90 | 90 |
| 813 | 814 | 814 |
| 822 | 823 | 823 |
| 903 | 904 | 904 |

### Group 79 — 3 occurrences

Key: `{"age": "68", "sex": "1", "cp": "0", "trestbps": "144", "chol": "193", "fbs": "1", "restecg": "1", "thalach": "141", "exang": "0", "oldpeak": "3.4", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 90 | 91 | 91 |
| 768 | 769 | 769 |
| 793 | 794 | 794 |

### Group 80 — 3 occurrences

Key: `{"age": "54", "sex": "0", "cp": "2", "trestbps": "108", "chol": "267", "fbs": "0", "restecg": "0", "thalach": "167", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 91 | 92 | 92 |
| 348 | 349 | 349 |
| 535 | 536 | 536 |

### Group 81 — 4 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "124", "chol": "209", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 92 | 93 | 93 |
| 201 | 202 | 202 |
| 419 | 420 | 420 |
| 528 | 529 | 529 |

### Group 82 — 3 occurrences

Key: `{"age": "62", "sex": "1", "cp": "1", "trestbps": "128", "chol": "208", "fbs": "1", "restecg": "0", "thalach": "140", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 95 | 96 | 96 |
| 796 | 797 | 797 |
| 815 | 816 | 816 |

### Group 83 — 3 occurrences

Key: `{"age": "45", "sex": "0", "cp": "0", "trestbps": "138", "chol": "236", "fbs": "0", "restecg": "0", "thalach": "152", "exang": "1", "oldpeak": "0.2", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 96 | 97 | 97 |
| 772 | 773 | 773 |
| 954 | 955 | 955 |

### Group 84 — 3 occurrences

Key: `{"age": "57", "sex": "0", "cp": "0", "trestbps": "128", "chol": "303", "fbs": "0", "restecg": "0", "thalach": "159", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 97 | 98 | 98 |
| 421 | 422 | 422 |
| 491 | 492 | 492 |

### Group 85 — 4 occurrences

Key: `{"age": "53", "sex": "1", "cp": "0", "trestbps": "123", "chol": "282", "fbs": "0", "restecg": "1", "thalach": "95", "exang": "1", "oldpeak": "2", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 98 | 99 | 99 |
| 267 | 268 | 268 |
| 778 | 779 | 779 |
| 1018 | 1019 | 1019 |

### Group 86 — 3 occurrences

Key: `{"age": "65", "sex": "1", "cp": "0", "trestbps": "110", "chol": "248", "fbs": "0", "restecg": "0", "thalach": "158", "exang": "0", "oldpeak": "0.6", "slope": "2", "ca": "2", "thal": "1", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 99 | 100 | 100 |
| 485 | 486 | 486 |
| 620 | 621 | 621 |

### Group 87 — 3 occurrences

Key: `{"age": "76", "sex": "0", "cp": "2", "trestbps": "140", "chol": "197", "fbs": "0", "restecg": "2", "thalach": "116", "exang": "0", "oldpeak": "1.1", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 100 | 101 | 101 |
| 536 | 537 | 537 |
| 966 | 967 | 967 |

### Group 88 — 3 occurrences

Key: `{"age": "43", "sex": "0", "cp": "2", "trestbps": "122", "chol": "213", "fbs": "0", "restecg": "1", "thalach": "165", "exang": "0", "oldpeak": "0.2", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 101 | 102 | 102 |
| 363 | 364 | 364 |
| 878 | 879 | 879 |

### Group 89 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "2", "trestbps": "150", "chol": "126", "fbs": "1", "restecg": "1", "thalach": "173", "exang": "0", "oldpeak": "0.2", "slope": "2", "ca": "1", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 102 | 103 | 103 |
| 337 | 338 | 338 |
| 476 | 477 | 477 |

### Group 90 — 4 occurrences

Key: `{"age": "54", "sex": "1", "cp": "1", "trestbps": "108", "chol": "309", "fbs": "0", "restecg": "1", "thalach": "156", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 103 | 104 | 104 |
| 121 | 122 | 122 |
| 135 | 136 | 136 |
| 156 | 157 | 157 |

### Group 91 — 4 occurrences

Key: `{"age": "52", "sex": "1", "cp": "3", "trestbps": "118", "chol": "186", "fbs": "0", "restecg": "0", "thalach": "190", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "1", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 105 | 106 | 106 |
| 380 | 381 | 381 |
| 463 | 464 | 464 |
| 973 | 974 | 974 |

### Group 92 — 4 occurrences

Key: `{"age": "47", "sex": "1", "cp": "0", "trestbps": "110", "chol": "275", "fbs": "0", "restecg": "0", "thalach": "118", "exang": "1", "oldpeak": "1", "slope": "1", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 106 | 107 | 107 |
| 251 | 252 | 252 |
| 468 | 469 | 469 |
| 1023 | 1024 | 1024 |

### Group 93 — 4 occurrences

Key: `{"age": "51", "sex": "1", "cp": "0", "trestbps": "140", "chol": "299", "fbs": "0", "restecg": "1", "thalach": "173", "exang": "1", "oldpeak": "1.6", "slope": "2", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 107 | 108 | 108 |
| 860 | 861 | 861 |
| 895 | 896 | 896 |
| 1011 | 1012 | 1012 |

### Group 94 — 4 occurrences

Key: `{"age": "62", "sex": "1", "cp": "1", "trestbps": "120", "chol": "281", "fbs": "0", "restecg": "0", "thalach": "103", "exang": "0", "oldpeak": "1.4", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 108 | 109 | 109 |
| 210 | 211 | 211 |
| 486 | 487 | 487 |
| 790 | 791 | 791 |

### Group 95 — 4 occurrences

Key: `{"age": "40", "sex": "1", "cp": "0", "trestbps": "152", "chol": "223", "fbs": "0", "restecg": "1", "thalach": "181", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 109 | 110 | 110 |
| 290 | 291 | 291 |
| 932 | 933 | 933 |
| 1010 | 1011 | 1011 |

### Group 96 — 4 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "110", "chol": "206", "fbs": "0", "restecg": "0", "thalach": "108", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 110 | 111 | 111 |
| 274 | 275 | 275 |
| 514 | 515 | 515 |
| 927 | 928 | 928 |

### Group 97 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "0", "trestbps": "110", "chol": "197", "fbs": "0", "restecg": "0", "thalach": "177", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 111 | 112 | 112 |
| 179 | 180 | 180 |
| 979 | 980 | 980 |

### Group 98 — 3 occurrences

Key: `{"age": "53", "sex": "1", "cp": "0", "trestbps": "142", "chol": "226", "fbs": "0", "restecg": "0", "thalach": "111", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 112 | 113 | 113 |
| 806 | 807 | 807 |
| 939 | 940 | 940 |

### Group 99 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "110", "chol": "335", "fbs": "0", "restecg": "1", "thalach": "143", "exang": "1", "oldpeak": "3", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 114 | 115 | 115 |
| 353 | 354 | 354 |
| 766 | 767 | 767 |
| 767 | 768 | 768 |

### Group 100 — 4 occurrences

Key: `{"age": "59", "sex": "1", "cp": "2", "trestbps": "126", "chol": "218", "fbs": "1", "restecg": "1", "thalach": "134", "exang": "0", "oldpeak": "2.2", "slope": "1", "ca": "1", "thal": "1", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 115 | 116 | 116 |
| 207 | 208 | 208 |
| 309 | 310 | 310 |
| 904 | 905 | 905 |

### Group 101 — 4 occurrences

Key: `{"age": "63", "sex": "1", "cp": "0", "trestbps": "130", "chol": "254", "fbs": "0", "restecg": "0", "thalach": "147", "exang": "0", "oldpeak": "1.4", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 117 | 118 | 118 |
| 189 | 190 | 190 |
| 222 | 223 | 223 |
| 678 | 679 | 679 |

### Group 102 — 4 occurrences

Key: `{"age": "43", "sex": "1", "cp": "0", "trestbps": "120", "chol": "177", "fbs": "0", "restecg": "0", "thalach": "120", "exang": "1", "oldpeak": "2.5", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 118 | 119 | 119 |
| 512 | 513 | 513 |
| 584 | 585 | 585 |
| 684 | 685 | 685 |

### Group 103 — 3 occurrences

Key: `{"age": "42", "sex": "1", "cp": "1", "trestbps": "120", "chol": "295", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 120 | 121 | 121 |
| 681 | 682 | 682 |
| 1009 | 1010 | 1010 |

### Group 104 — 3 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "145", "chol": "282", "fbs": "0", "restecg": "0", "thalach": "142", "exang": "1", "oldpeak": "2.8", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 123 | 124 | 124 |
| 304 | 305 | 305 |
| 572 | 573 | 573 |

### Group 105 — 3 occurrences

Key: `{"age": "65", "sex": "0", "cp": "2", "trestbps": "140", "chol": "417", "fbs": "1", "restecg": "0", "thalach": "157", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 124 | 125 | 125 |
| 666 | 667 | 667 |
| 959 | 960 | 960 |

### Group 106 — 4 occurrences

Key: `{"age": "61", "sex": "1", "cp": "0", "trestbps": "120", "chol": "260", "fbs": "0", "restecg": "1", "thalach": "140", "exang": "1", "oldpeak": "3.6", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 125 | 126 | 126 |
| 311 | 312 | 312 |
| 507 | 508 | 508 |
| 887 | 888 | 888 |

### Group 107 — 4 occurrences

Key: `{"age": "60", "sex": "0", "cp": "3", "trestbps": "150", "chol": "240", "fbs": "0", "restecg": "1", "thalach": "171", "exang": "0", "oldpeak": "0.9", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 126 | 127 | 127 |
| 131 | 132 | 132 |
| 471 | 472 | 472 |
| 866 | 867 | 867 |

### Group 108 — 3 occurrences

Key: `{"age": "66", "sex": "1", "cp": "0", "trestbps": "120", "chol": "302", "fbs": "0", "restecg": "0", "thalach": "151", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 127 | 128 | 128 |
| 260 | 261 | 261 |
| 351 | 352 | 352 |

### Group 109 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "2", "trestbps": "138", "chol": "223", "fbs": "0", "restecg": "1", "thalach": "169", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "4", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 129 | 130 | 130 |
| 291 | 292 | 292 |
| 418 | 419 | 419 |

### Group 110 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "140", "chol": "192", "fbs": "0", "restecg": "1", "thalach": "148", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "0", "thal": "1", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 130 | 131 | 131 |
| 874 | 875 | 875 |
| 981 | 982 | 982 |

### Group 111 — 3 occurrences

Key: `{"age": "51", "sex": "0", "cp": "2", "trestbps": "130", "chol": "256", "fbs": "0", "restecg": "0", "thalach": "149", "exang": "0", "oldpeak": "0.5", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 132 | 133 | 133 |
| 526 | 527 | 527 |
| 755 | 756 | 756 |

### Group 112 — 4 occurrences

Key: `{"age": "58", "sex": "0", "cp": "0", "trestbps": "170", "chol": "225", "fbs": "1", "restecg": "0", "thalach": "146", "exang": "1", "oldpeak": "2.8", "slope": "1", "ca": "2", "thal": "1", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 136 | 137 | 137 |
| 265 | 266 | 266 |
| 613 | 614 | 614 |
| 820 | 821 | 821 |

### Group 113 — 3 occurrences

Key: `{"age": "64", "sex": "0", "cp": "0", "trestbps": "180", "chol": "325", "fbs": "0", "restecg": "1", "thalach": "154", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 138 | 139 | 139 |
| 258 | 259 | 259 |
| 892 | 893 | 893 |

### Group 114 — 3 occurrences

Key: `{"age": "41", "sex": "1", "cp": "1", "trestbps": "110", "chol": "235", "fbs": "0", "restecg": "1", "thalach": "153", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 140 | 141 | 141 |
| 656 | 657 | 657 |
| 868 | 869 | 869 |

### Group 115 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "152", "chol": "274", "fbs": "0", "restecg": "1", "thalach": "88", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 141 | 142 | 142 |
| 443 | 444 | 444 |
| 621 | 622 | 622 |

### Group 116 — 3 occurrences

Key: `{"age": "63", "sex": "0", "cp": "0", "trestbps": "124", "chol": "197", "fbs": "0", "restecg": "1", "thalach": "136", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 142 | 143 | 143 |
| 533 | 534 | 534 |
| 803 | 804 | 804 |

### Group 117 — 4 occurrences

Key: `{"age": "61", "sex": "1", "cp": "3", "trestbps": "134", "chol": "234", "fbs": "0", "restecg": "1", "thalach": "145", "exang": "0", "oldpeak": "2.6", "slope": "1", "ca": "2", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 143 | 144 | 144 |
| 624 | 625 | 625 |
| 795 | 796 | 796 |
| 901 | 902 | 902 |

### Group 118 — 3 occurrences

Key: `{"age": "34", "sex": "1", "cp": "3", "trestbps": "118", "chol": "182", "fbs": "0", "restecg": "0", "thalach": "174", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 144 | 145 | 145 |
| 202 | 203 | 203 |
| 573 | 574 | 574 |

### Group 119 — 3 occurrences

Key: `{"age": "47", "sex": "1", "cp": "0", "trestbps": "112", "chol": "204", "fbs": "0", "restecg": "1", "thalach": "143", "exang": "0", "oldpeak": "0.1", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 145 | 146 | 146 |
| 663 | 664 | 664 |
| 1020 | 1021 | 1021 |

### Group 120 — 4 occurrences

Key: `{"age": "40", "sex": "1", "cp": "0", "trestbps": "110", "chol": "167", "fbs": "0", "restecg": "0", "thalach": "114", "exang": "1", "oldpeak": "2", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 146 | 147 | 147 |
| 187 | 188 | 188 |
| 398 | 399 | 399 |
| 811 | 812 | 812 |

### Group 121 — 3 occurrences

Key: `{"age": "51", "sex": "0", "cp": "2", "trestbps": "120", "chol": "295", "fbs": "0", "restecg": "0", "thalach": "157", "exang": "0", "oldpeak": "0.6", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 147 | 148 | 148 |
| 449 | 450 | 450 |
| 549 | 550 | 550 |

### Group 122 — 3 occurrences

Key: `{"age": "41", "sex": "1", "cp": "0", "trestbps": "110", "chol": "172", "fbs": "0", "restecg": "0", "thalach": "158", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 148 | 149 | 149 |
| 487 | 488 | 488 |
| 1019 | 1020 | 1020 |

### Group 123 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "3", "trestbps": "152", "chol": "298", "fbs": "1", "restecg": "1", "thalach": "178", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 149 | 150 | 150 |
| 203 | 204 | 204 |
| 577 | 578 | 578 |

### Group 124 — 3 occurrences

Key: `{"age": "39", "sex": "1", "cp": "2", "trestbps": "140", "chol": "321", "fbs": "0", "restecg": "0", "thalach": "182", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 150 | 151 | 151 |
| 479 | 480 | 480 |
| 872 | 873 | 873 |

### Group 125 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "1", "trestbps": "192", "chol": "283", "fbs": "0", "restecg": "0", "thalach": "195", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 152 | 153 | 153 |
| 247 | 248 | 248 |
| 327 | 328 | 328 |

### Group 126 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "125", "chol": "300", "fbs": "0", "restecg": "0", "thalach": "171", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 153 | 154 | 154 |
| 231 | 232 | 232 |
| 688 | 689 | 689 |
| 739 | 740 | 740 |

### Group 127 — 4 occurrences

Key: `{"age": "63", "sex": "1", "cp": "0", "trestbps": "130", "chol": "330", "fbs": "1", "restecg": "0", "thalach": "132", "exang": "1", "oldpeak": "1.8", "slope": "2", "ca": "3", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 155 | 156 | 156 |
| 395 | 396 | 396 |
| 675 | 676 | 676 |
| 743 | 744 | 744 |

### Group 128 — 3 occurrences

Key: `{"age": "40", "sex": "1", "cp": "3", "trestbps": "140", "chol": "199", "fbs": "0", "restecg": "1", "thalach": "178", "exang": "1", "oldpeak": "1.4", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 157 | 158 | 158 |
| 315 | 316 | 316 |
| 586 | 587 | 587 |

### Group 129 — 3 occurrences

Key: `{"age": "67", "sex": "0", "cp": "2", "trestbps": "115", "chol": "564", "fbs": "0", "restecg": "0", "thalach": "160", "exang": "0", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 159 | 160 | 160 |
| 193 | 194 | 194 |
| 465 | 466 | 466 |

### Group 130 — 4 occurrences

Key: `{"age": "41", "sex": "1", "cp": "1", "trestbps": "120", "chol": "157", "fbs": "0", "restecg": "1", "thalach": "182", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 160 | 161 | 161 |
| 218 | 219 | 219 |
| 345 | 346 | 346 |
| 652 | 653 | 653 |

### Group 131 — 3 occurrences

Key: `{"age": "77", "sex": "1", "cp": "0", "trestbps": "125", "chol": "304", "fbs": "0", "restecg": "0", "thalach": "162", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "3", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 161 | 162 | 162 |
| 163 | 164 | 164 |
| 388 | 389 | 389 |

### Group 132 — 4 occurrences

Key: `{"age": "51", "sex": "1", "cp": "2", "trestbps": "100", "chol": "222", "fbs": "0", "restecg": "1", "thalach": "143", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 162 | 163 | 163 |
| 746 | 747 | 747 |
| 776 | 777 | 777 |
| 831 | 832 | 832 |

### Group 133 — 3 occurrences

Key: `{"age": "48", "sex": "1", "cp": "0", "trestbps": "124", "chol": "274", "fbs": "0", "restecg": "0", "thalach": "166", "exang": "0", "oldpeak": "0.5", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 164 | 165 | 165 |
| 727 | 728 | 728 |
| 884 | 885 | 885 |

### Group 134 — 3 occurrences

Key: `{"age": "56", "sex": "1", "cp": "0", "trestbps": "132", "chol": "184", "fbs": "0", "restecg": "0", "thalach": "105", "exang": "1", "oldpeak": "2.1", "slope": "1", "ca": "1", "thal": "1", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 167 | 168 | 168 |
| 565 | 566 | 566 |
| 846 | 847 | 847 |

### Group 135 — 3 occurrences

Key: `{"age": "57", "sex": "0", "cp": "0", "trestbps": "120", "chol": "354", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "1", "oldpeak": "0.6", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 168 | 169 | 169 |
| 423 | 424 | 424 |
| 436 | 437 | 437 |

### Group 136 — 3 occurrences

Key: `{"age": "43", "sex": "1", "cp": "2", "trestbps": "130", "chol": "315", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "1.9", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 169 | 170 | 170 |
| 214 | 215 | 215 |
| 937 | 938 | 938 |

### Group 137 — 3 occurrences

Key: `{"age": "45", "sex": "0", "cp": "1", "trestbps": "112", "chol": "160", "fbs": "0", "restecg": "1", "thalach": "138", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 170 | 171 | 171 |
| 252 | 253 | 253 |
| 713 | 714 | 714 |

### Group 138 — 3 occurrences

Key: `{"age": "43", "sex": "1", "cp": "0", "trestbps": "150", "chol": "247", "fbs": "0", "restecg": "1", "thalach": "171", "exang": "0", "oldpeak": "1.5", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 171 | 172 | 172 |
| 459 | 460 | 460 |
| 576 | 577 | 577 |

### Group 139 — 4 occurrences

Key: `{"age": "56", "sex": "1", "cp": "0", "trestbps": "130", "chol": "283", "fbs": "1", "restecg": "0", "thalach": "103", "exang": "1", "oldpeak": "1.6", "slope": "0", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 172 | 173 | 173 |
| 177 | 178 | 178 |
| 276 | 277 | 277 |
| 654 | 655 | 655 |

### Group 140 — 4 occurrences

Key: `{"age": "56", "sex": "1", "cp": "1", "trestbps": "120", "chol": "240", "fbs": "0", "restecg": "1", "thalach": "169", "exang": "0", "oldpeak": "0", "slope": "0", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 173 | 174 | 174 |
| 784 | 785 | 785 |
| 869 | 870 | 870 |
| 936 | 937 | 937 |

### Group 141 — 3 occurrences

Key: `{"age": "39", "sex": "0", "cp": "2", "trestbps": "94", "chol": "199", "fbs": "0", "restecg": "1", "thalach": "179", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 174 | 175 | 175 |
| 224 | 225 | 225 |
| 559 | 560 | 560 |

### Group 142 — 4 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "110", "chol": "239", "fbs": "0", "restecg": "1", "thalach": "126", "exang": "1", "oldpeak": "2.8", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 175 | 176 | 176 |
| 791 | 792 | 792 |
| 792 | 793 | 793 |
| 893 | 894 | 894 |

### Group 143 — 4 occurrences

Key: `{"age": "56", "sex": "0", "cp": "0", "trestbps": "200", "chol": "288", "fbs": "1", "restecg": "0", "thalach": "133", "exang": "1", "oldpeak": "4", "slope": "0", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 176 | 177 | 177 |
| 295 | 296 | 296 |
| 509 | 510 | 510 |
| 689 | 690 | 690 |

### Group 144 — 4 occurrences

Key: `{"age": "64", "sex": "1", "cp": "0", "trestbps": "120", "chol": "246", "fbs": "0", "restecg": "0", "thalach": "96", "exang": "1", "oldpeak": "2.2", "slope": "0", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 178 | 179 | 179 |
| 389 | 390 | 390 |
| 757 | 758 | 758 |
| 906 | 907 | 907 |

### Group 145 — 3 occurrences

Key: `{"age": "56", "sex": "0", "cp": "0", "trestbps": "134", "chol": "409", "fbs": "0", "restecg": "0", "thalach": "150", "exang": "1", "oldpeak": "1.9", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 180 | 181 | 181 |
| 642 | 643 | 643 |
| 997 | 998 | 998 |

### Group 146 — 3 occurrences

Key: `{"age": "64", "sex": "1", "cp": "3", "trestbps": "110", "chol": "211", "fbs": "0", "restecg": "0", "thalach": "144", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 182 | 183 | 183 |
| 223 | 224 | 224 |
| 284 | 285 | 285 |

### Group 147 — 4 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "140", "chol": "293", "fbs": "0", "restecg": "0", "thalach": "170", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 183 | 184 | 184 |
| 442 | 443 | 443 |
| 845 | 846 | 846 |
| 989 | 990 | 990 |

### Group 148 — 4 occurrences

Key: `{"age": "42", "sex": "1", "cp": "2", "trestbps": "130", "chol": "180", "fbs": "0", "restecg": "1", "thalach": "150", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 184 | 185 | 185 |
| 250 | 251 | 251 |
| 827 | 828 | 828 |
| 935 | 936 | 936 |

### Group 149 — 3 occurrences

Key: `{"age": "45", "sex": "1", "cp": "1", "trestbps": "128", "chol": "308", "fbs": "0", "restecg": "0", "thalach": "170", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 185 | 186 | 186 |
| 215 | 216 | 216 |
| 1012 | 1013 | 1013 |

### Group 150 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "165", "chol": "289", "fbs": "1", "restecg": "0", "thalach": "124", "exang": "0", "oldpeak": "1", "slope": "1", "ca": "3", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 186 | 187 | 187 |
| 254 | 255 | 255 |
| 477 | 478 | 478 |
| 886 | 887 | 887 |

### Group 151 — 4 occurrences

Key: `{"age": "64", "sex": "1", "cp": "2", "trestbps": "125", "chol": "309", "fbs": "0", "restecg": "1", "thalach": "131", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 190 | 191 | 191 |
| 493 | 494 | 494 |
| 587 | 588 | 588 |
| 659 | 660 | 660 |

### Group 152 — 3 occurrences

Key: `{"age": "41", "sex": "1", "cp": "2", "trestbps": "112", "chol": "250", "fbs": "0", "restecg": "1", "thalach": "179", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 191 | 192 | 192 |
| 208 | 209 | 209 |
| 867 | 868 | 868 |

### Group 153 — 4 occurrences

Key: `{"age": "56", "sex": "1", "cp": "1", "trestbps": "130", "chol": "221", "fbs": "0", "restecg": "0", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 192 | 193 | 193 |
| 711 | 712 | 712 |
| 728 | 729 | 729 |
| 763 | 764 | 764 |

### Group 154 — 3 occurrences

Key: `{"age": "69", "sex": "1", "cp": "3", "trestbps": "160", "chol": "234", "fbs": "1", "restecg": "0", "thalach": "131", "exang": "0", "oldpeak": "0.1", "slope": "1", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 194 | 195 | 195 |
| 456 | 457 | 457 |
| 530 | 531 | 531 |

### Group 155 — 4 occurrences

Key: `{"age": "67", "sex": "1", "cp": "0", "trestbps": "160", "chol": "286", "fbs": "0", "restecg": "0", "thalach": "108", "exang": "1", "oldpeak": "1.5", "slope": "1", "ca": "3", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 195 | 196 | 196 |
| 358 | 359 | 359 |
| 470 | 471 | 471 |
| 951 | 952 | 952 |

### Group 156 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "100", "chol": "234", "fbs": "0", "restecg": "1", "thalach": "156", "exang": "0", "oldpeak": "0.1", "slope": "2", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 197 | 198 | 198 |
| 408 | 409 | 409 |
| 555 | 556 | 556 |
| 676 | 677 | 677 |

### Group 157 — 3 occurrences

Key: `{"age": "45", "sex": "1", "cp": "0", "trestbps": "115", "chol": "260", "fbs": "0", "restecg": "0", "thalach": "185", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 198 | 199 | 199 |
| 722 | 723 | 723 |
| 818 | 819 | 819 |

### Group 158 — 3 occurrences

Key: `{"age": "60", "sex": "0", "cp": "2", "trestbps": "102", "chol": "318", "fbs": "0", "restecg": "1", "thalach": "160", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 199 | 200 | 200 |
| 433 | 434 | 434 |
| 745 | 746 | 746 |

### Group 159 — 3 occurrences

Key: `{"age": "50", "sex": "1", "cp": "0", "trestbps": "144", "chol": "200", "fbs": "0", "restecg": "0", "thalach": "126", "exang": "1", "oldpeak": "0.9", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 200 | 201 | 201 |
| 352 | 353 | 353 |
| 910 | 911 | 911 |

### Group 160 — 4 occurrences

Key: `{"age": "64", "sex": "1", "cp": "3", "trestbps": "170", "chol": "227", "fbs": "0", "restecg": "0", "thalach": "155", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 204 | 205 | 205 |
| 236 | 237 | 237 |
| 540 | 541 | 541 |
| 873 | 874 | 874 |

### Group 161 — 3 occurrences

Key: `{"age": "42", "sex": "1", "cp": "3", "trestbps": "148", "chol": "244", "fbs": "0", "restecg": "0", "thalach": "178", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "2", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 206 | 207 | 207 |
| 316 | 317 | 317 |
| 819 | 820 | 820 |

### Group 162 — 3 occurrences

Key: `{"age": "42", "sex": "1", "cp": "2", "trestbps": "120", "chol": "240", "fbs": "1", "restecg": "1", "thalach": "194", "exang": "0", "oldpeak": "0.8", "slope": "0", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 211 | 212 | 212 |
| 570 | 571 | 571 |
| 928 | 929 | 929 |

### Group 163 — 3 occurrences

Key: `{"age": "50", "sex": "1", "cp": "0", "trestbps": "150", "chol": "243", "fbs": "0", "restecg": "0", "thalach": "128", "exang": "0", "oldpeak": "2.6", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 213 | 214 | 214 |
| 347 | 348 | 348 |
| 646 | 647 | 647 |

### Group 164 — 3 occurrences

Key: `{"age": "49", "sex": "1", "cp": "1", "trestbps": "130", "chol": "266", "fbs": "0", "restecg": "1", "thalach": "171", "exang": "0", "oldpeak": "0.6", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 216 | 217 | 217 |
| 619 | 620 | 620 |
| 632 | 633 | 633 |

### Group 165 — 4 occurrences

Key: `{"age": "65", "sex": "1", "cp": "0", "trestbps": "135", "chol": "254", "fbs": "0", "restecg": "0", "thalach": "127", "exang": "0", "oldpeak": "2.8", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 217 | 218 | 218 |
| 488 | 489 | 489 |
| 917 | 918 | 918 |
| 931 | 932 | 932 |

### Group 166 — 4 occurrences

Key: `{"age": "46", "sex": "1", "cp": "0", "trestbps": "140", "chol": "311", "fbs": "0", "restecg": "1", "thalach": "120", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 219 | 220 | 220 |
| 248 | 249 | 249 |
| 602 | 603 | 603 |
| 729 | 730 | 730 |

### Group 167 — 3 occurrences

Key: `{"age": "57", "sex": "0", "cp": "1", "trestbps": "130", "chol": "236", "fbs": "0", "restecg": "0", "thalach": "174", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 221 | 222 | 222 |
| 365 | 366 | 366 |
| 657 | 658 | 658 |

### Group 168 — 3 occurrences

Key: `{"age": "51", "sex": "1", "cp": "0", "trestbps": "140", "chol": "261", "fbs": "0", "restecg": "0", "thalach": "186", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 225 | 226 | 226 |
| 460 | 461 | 461 |
| 840 | 841 | 841 |

### Group 169 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "2", "trestbps": "150", "chol": "232", "fbs": "0", "restecg": "0", "thalach": "165", "exang": "0", "oldpeak": "1.6", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 226 | 227 | 227 |
| 262 | 263 | 263 |
| 785 | 786 | 786 |

### Group 170 — 3 occurrences

Key: `{"age": "44", "sex": "0", "cp": "2", "trestbps": "118", "chol": "242", "fbs": "0", "restecg": "1", "thalach": "149", "exang": "0", "oldpeak": "0.3", "slope": "1", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 228 | 229 | 229 |
| 307 | 308 | 308 |
| 506 | 507 | 507 |

### Group 171 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "1", "trestbps": "128", "chol": "205", "fbs": "1", "restecg": "1", "thalach": "184", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 229 | 230 | 230 |
| 446 | 447 | 447 |
| 978 | 979 | 979 |

### Group 172 — 3 occurrences

Key: `{"age": "56", "sex": "1", "cp": "1", "trestbps": "120", "chol": "236", "fbs": "0", "restecg": "1", "thalach": "178", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 232 | 233 | 233 |
| 870 | 871 | 871 |
| 991 | 992 | 992 |

### Group 173 — 3 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "125", "chol": "258", "fbs": "0", "restecg": "0", "thalach": "141", "exang": "1", "oldpeak": "2.8", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 233 | 234 | 234 |
| 575 | 576 | 576 |
| 1022 | 1023 | 1023 |

### Group 174 — 3 occurrences

Key: `{"age": "41", "sex": "0", "cp": "1", "trestbps": "126", "chol": "306", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 234 | 235 | 235 |
| 618 | 619 | 619 |
| 655 | 656 | 656 |

### Group 175 — 3 occurrences

Key: `{"age": "49", "sex": "0", "cp": "0", "trestbps": "130", "chol": "269", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 235 | 236 | 236 |
| 762 | 763 | 763 |
| 957 | 958 | 958 |

### Group 176 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "1", "trestbps": "124", "chol": "261", "fbs": "0", "restecg": "1", "thalach": "141", "exang": "0", "oldpeak": "0.3", "slope": "2", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 238 | 239 | 239 |
| 355 | 356 | 356 |
| 668 | 669 | 669 |
| 812 | 813 | 813 |

### Group 177 — 3 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "150", "chol": "244", "fbs": "0", "restecg": "1", "thalach": "154", "exang": "1", "oldpeak": "1.4", "slope": "1", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 240 | 241 | 241 |
| 441 | 442 | 442 |
| 773 | 774 | 774 |

### Group 178 — 3 occurrences

Key: `{"age": "54", "sex": "0", "cp": "1", "trestbps": "132", "chol": "288", "fbs": "1", "restecg": "0", "thalach": "159", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 241 | 242 | 242 |
| 489 | 490 | 490 |
| 511 | 512 | 512 |

### Group 179 — 3 occurrences

Key: `{"age": "51", "sex": "1", "cp": "2", "trestbps": "125", "chol": "245", "fbs": "1", "restecg": "0", "thalach": "166", "exang": "0", "oldpeak": "2.4", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 245 | 246 | 246 |
| 495 | 496 | 496 |
| 974 | 975 | 975 |

### Group 180 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "1", "trestbps": "130", "chol": "219", "fbs": "0", "restecg": "0", "thalach": "188", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 246 | 247 | 247 |
| 278 | 279 | 279 |
| 467 | 468 | 468 |

### Group 181 — 4 occurrences

Key: `{"age": "39", "sex": "0", "cp": "2", "trestbps": "138", "chol": "220", "fbs": "0", "restecg": "1", "thalach": "152", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 249 | 250 | 250 |
| 273 | 274 | 274 |
| 458 | 459 | 459 |
| 658 | 659 | 659 |

### Group 182 — 4 occurrences

Key: `{"age": "55", "sex": "1", "cp": "0", "trestbps": "132", "chol": "353", "fbs": "0", "restecg": "1", "thalach": "132", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 253 | 254 | 254 |
| 372 | 373 | 373 |
| 494 | 495 | 495 |
| 585 | 586 | 586 |

### Group 183 — 4 occurrences

Key: `{"age": "35", "sex": "1", "cp": "0", "trestbps": "120", "chol": "198", "fbs": "0", "restecg": "1", "thalach": "130", "exang": "1", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 255 | 256 | 256 |
| 702 | 703 | 703 |
| 712 | 713 | 713 |
| 913 | 914 | 914 |

### Group 184 — 3 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "140", "chol": "394", "fbs": "0", "restecg": "0", "thalach": "157", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 256 | 257 | 257 |
| 543 | 544 | 544 |
| 579 | 580 | 580 |

### Group 185 — 4 occurrences

Key: `{"age": "35", "sex": "0", "cp": "0", "trestbps": "138", "chol": "183", "fbs": "0", "restecg": "1", "thalach": "182", "exang": "0", "oldpeak": "1.4", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 257 | 258 | 258 |
| 502 | 503 | 503 |
| 842 | 843 | 843 |
| 847 | 848 | 848 |

### Group 186 — 4 occurrences

Key: `{"age": "38", "sex": "1", "cp": "3", "trestbps": "120", "chol": "231", "fbs": "0", "restecg": "1", "thalach": "182", "exang": "1", "oldpeak": "3.8", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 259 | 260 | 260 |
| 628 | 629 | 629 |
| 920 | 921 | 921 |
| 934 | 935 | 935 |

### Group 187 — 4 occurrences

Key: `{"age": "44", "sex": "1", "cp": "2", "trestbps": "120", "chol": "226", "fbs": "0", "restecg": "1", "thalach": "169", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 261 | 262 | 262 |
| 342 | 343 | 343 |
| 645 | 646 | 646 |
| 749 | 750 | 750 |

### Group 188 — 3 occurrences

Key: `{"age": "48", "sex": "1", "cp": "0", "trestbps": "122", "chol": "222", "fbs": "0", "restecg": "0", "thalach": "186", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 263 | 264 | 264 |
| 361 | 362 | 362 |
| 558 | 559 | 559 |

### Group 189 — 4 occurrences

Key: `{"age": "67", "sex": "1", "cp": "0", "trestbps": "120", "chol": "237", "fbs": "0", "restecg": "1", "thalach": "71", "exang": "0", "oldpeak": "1", "slope": "1", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 268 | 269 | 269 |
| 297 | 298 | 298 |
| 379 | 380 | 380 |
| 560 | 561 | 561 |

### Group 190 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "2", "trestbps": "132", "chol": "224", "fbs": "0", "restecg": "0", "thalach": "173", "exang": "0", "oldpeak": "3.2", "slope": "2", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 269 | 270 | 270 |
| 285 | 286 | 286 |
| 382 | 383 | 383 |
| 627 | 628 | 628 |

### Group 191 — 4 occurrences

Key: `{"age": "71", "sex": "0", "cp": "2", "trestbps": "110", "chol": "265", "fbs": "1", "restecg": "0", "thalach": "130", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 270 | 271 | 271 |
| 286 | 287 | 287 |
| 606 | 607 | 607 |
| 770 | 771 | 771 |

### Group 192 — 3 occurrences

Key: `{"age": "43", "sex": "1", "cp": "0", "trestbps": "110", "chol": "211", "fbs": "0", "restecg": "1", "thalach": "161", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 271 | 272 | 272 |
| 464 | 465 | 465 |
| 975 | 976 | 976 |

### Group 193 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "1", "trestbps": "120", "chol": "263", "fbs": "0", "restecg": "1", "thalach": "173", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 272 | 273 | 273 |
| 923 | 924 | 924 |
| 996 | 997 | 997 |

### Group 194 — 4 occurrences

Key: `{"age": "66", "sex": "1", "cp": "0", "trestbps": "160", "chol": "228", "fbs": "0", "restecg": "0", "thalach": "138", "exang": "0", "oldpeak": "2.3", "slope": "2", "ca": "0", "thal": "1", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 275 | 276 | 276 |
| 376 | 377 | 377 |
| 399 | 400 | 400 |
| 758 | 759 | 759 |

### Group 195 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "132", "chol": "207", "fbs": "0", "restecg": "1", "thalach": "168", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 277 | 278 | 278 |
| 881 | 882 | 882 |
| 950 | 951 | 951 |

### Group 196 — 3 occurrences

Key: `{"age": "41", "sex": "0", "cp": "1", "trestbps": "105", "chol": "198", "fbs": "0", "restecg": "1", "thalach": "168", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 280 | 281 | 281 |
| 411 | 412 | 412 |
| 518 | 519 | 519 |

### Group 197 — 4 occurrences

Key: `{"age": "45", "sex": "0", "cp": "1", "trestbps": "130", "chol": "234", "fbs": "0", "restecg": "0", "thalach": "175", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 281 | 282 | 282 |
| 504 | 505 | 505 |
| 633 | 634 | 634 |
| 650 | 651 | 651 |

### Group 198 — 4 occurrences

Key: `{"age": "35", "sex": "1", "cp": "1", "trestbps": "122", "chol": "192", "fbs": "0", "restecg": "1", "thalach": "174", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 282 | 283 | 283 |
| 299 | 300 | 300 |
| 484 | 485 | 485 |
| 667 | 668 | 668 |

### Group 199 — 3 occurrences

Key: `{"age": "41", "sex": "0", "cp": "1", "trestbps": "130", "chol": "204", "fbs": "0", "restecg": "0", "thalach": "172", "exang": "0", "oldpeak": "1.4", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 283 | 284 | 284 |
| 416 | 417 | 417 |
| 508 | 509 | 509 |

### Group 200 — 3 occurrences

Key: `{"age": "64", "sex": "0", "cp": "2", "trestbps": "140", "chol": "313", "fbs": "0", "restecg": "1", "thalach": "133", "exang": "0", "oldpeak": "0.2", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 287 | 288 | 288 |
| 317 | 318 | 318 |
| 472 | 473 | 473 |

### Group 201 — 3 occurrences

Key: `{"age": "71", "sex": "0", "cp": "1", "trestbps": "160", "chol": "302", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "0.4", "slope": "2", "ca": "2", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 288 | 289 | 289 |
| 703 | 704 | 704 |
| 990 | 991 | 991 |

### Group 202 — 3 occurrences

Key: `{"age": "58", "sex": "0", "cp": "2", "trestbps": "120", "chol": "340", "fbs": "0", "restecg": "1", "thalach": "172", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 289 | 290 | 290 |
| 603 | 604 | 604 |
| 638 | 639 | 639 |

### Group 203 — 3 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "128", "chol": "259", "fbs": "0", "restecg": "0", "thalach": "130", "exang": "1", "oldpeak": "3", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 292 | 293 | 293 |
| 541 | 542 | 542 |
| 967 | 968 | 968 |

### Group 204 — 3 occurrences

Key: `{"age": "61", "sex": "1", "cp": "2", "trestbps": "150", "chol": "243", "fbs": "1", "restecg": "1", "thalach": "137", "exang": "1", "oldpeak": "1", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 293 | 294 | 294 |
| 469 | 470 | 470 |
| 490 | 491 | 491 |

### Group 205 — 3 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "150", "chol": "270", "fbs": "0", "restecg": "0", "thalach": "111", "exang": "1", "oldpeak": "0.8", "slope": "2", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 298 | 299 | 299 |
| 336 | 337 | 337 |
| 384 | 385 | 385 |

### Group 206 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "1", "trestbps": "120", "chol": "325", "fbs": "0", "restecg": "1", "thalach": "172", "exang": "0", "oldpeak": "0.2", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 300 | 301 | 301 |
| 538 | 539 | 539 |
| 970 | 971 | 971 |

### Group 207 — 3 occurrences

Key: `{"age": "46", "sex": "0", "cp": "1", "trestbps": "105", "chol": "204", "fbs": "0", "restecg": "1", "thalach": "172", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 301 | 302 | 302 |
| 404 | 405 | 405 |
| 759 | 760 | 760 |

### Group 208 — 4 occurrences

Key: `{"age": "51", "sex": "1", "cp": "2", "trestbps": "94", "chol": "227", "fbs": "0", "restecg": "1", "thalach": "154", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "3", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 302 | 303 | 303 |
| 705 | 706 | 706 |
| 733 | 734 | 734 |
| 809 | 810 | 810 |

### Group 209 — 3 occurrences

Key: `{"age": "52", "sex": "0", "cp": "2", "trestbps": "136", "chol": "196", "fbs": "0", "restecg": "0", "thalach": "169", "exang": "0", "oldpeak": "0.1", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 305 | 306 | 306 |
| 942 | 943 | 943 |
| 961 | 962 | 962 |

### Group 210 — 3 occurrences

Key: `{"age": "62", "sex": "1", "cp": "0", "trestbps": "120", "chol": "267", "fbs": "0", "restecg": "1", "thalach": "99", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 306 | 307 | 307 |
| 651 | 652 | 652 |
| 909 | 910 | 910 |

### Group 211 — 3 occurrences

Key: `{"age": "56", "sex": "0", "cp": "1", "trestbps": "140", "chol": "294", "fbs": "0", "restecg": "0", "thalach": "153", "exang": "0", "oldpeak": "1.3", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 310 | 311 | 311 |
| 326 | 327 | 327 |
| 708 | 709 | 709 |

### Group 212 — 3 occurrences

Key: `{"age": "74", "sex": "0", "cp": "1", "trestbps": "120", "chol": "269", "fbs": "0", "restecg": "0", "thalach": "121", "exang": "1", "oldpeak": "0.2", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 314 | 315 | 315 |
| 591 | 592 | 592 |
| 725 | 726 | 726 |

### Group 213 — 3 occurrences

Key: `{"age": "53", "sex": "0", "cp": "2", "trestbps": "128", "chol": "216", "fbs": "0", "restecg": "0", "thalach": "115", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "0", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 320 | 321 | 321 |
| 330 | 331 | 331 |
| 360 | 361 | 361 |

### Group 214 — 3 occurrences

Key: `{"age": "53", "sex": "0", "cp": "0", "trestbps": "130", "chol": "264", "fbs": "0", "restecg": "0", "thalach": "143", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 321 | 322 | 322 |
| 636 | 637 | 637 |
| 955 | 956 | 956 |

### Group 215 — 3 occurrences

Key: `{"age": "48", "sex": "0", "cp": "2", "trestbps": "130", "chol": "275", "fbs": "0", "restecg": "1", "thalach": "139", "exang": "0", "oldpeak": "0.2", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 322 | 323 | 323 |
| 775 | 776 | 776 |
| 871 | 872 | 872 |

### Group 216 — 3 occurrences

Key: `{"age": "45", "sex": "1", "cp": "0", "trestbps": "142", "chol": "309", "fbs": "0", "restecg": "0", "thalach": "147", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "3", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 323 | 324 | 324 |
| 425 | 426 | 426 |
| 980 | 981 | 981 |

### Group 217 — 3 occurrences

Key: `{"age": "66", "sex": "1", "cp": "1", "trestbps": "160", "chol": "246", "fbs": "0", "restecg": "1", "thalach": "120", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "3", "thal": "1", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 324 | 325 | 325 |
| 346 | 347 | 347 |
| 670 | 671 | 671 |

### Group 218 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "150", "chol": "276", "fbs": "0", "restecg": "0", "thalach": "112", "exang": "1", "oldpeak": "0.6", "slope": "1", "ca": "1", "thal": "1", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 328 | 329 | 329 |
| 413 | 414 | 414 |
| 761 | 762 | 762 |
| 807 | 808 | 808 |

### Group 219 — 4 occurrences

Key: `{"age": "70", "sex": "1", "cp": "0", "trestbps": "130", "chol": "322", "fbs": "0", "restecg": "0", "thalach": "109", "exang": "0", "oldpeak": "2.4", "slope": "1", "ca": "3", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 329 | 330 | 330 |
| 414 | 415 | 415 |
| 547 | 548 | 548 |
| 578 | 579 | 579 |

### Group 220 — 4 occurrences

Key: `{"age": "63", "sex": "0", "cp": "0", "trestbps": "108", "chol": "269", "fbs": "0", "restecg": "1", "thalach": "169", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "2", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 332 | 333 | 333 |
| 592 | 593 | 593 |
| 594 | 595 | 595 |
| 977 | 978 | 978 |

### Group 221 — 3 occurrences

Key: `{"age": "37", "sex": "1", "cp": "2", "trestbps": "130", "chol": "250", "fbs": "0", "restecg": "1", "thalach": "187", "exang": "0", "oldpeak": "3.5", "slope": "0", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 333 | 334 | 334 |
| 434 | 435 | 435 |
| 852 | 853 | 853 |

### Group 222 — 3 occurrences

Key: `{"age": "54", "sex": "0", "cp": "2", "trestbps": "110", "chol": "214", "fbs": "0", "restecg": "1", "thalach": "158", "exang": "0", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 334 | 335 | 335 |
| 373 | 374 | 374 |
| 810 | 811 | 811 |

### Group 223 — 4 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "130", "chol": "206", "fbs": "0", "restecg": "0", "thalach": "132", "exang": "1", "oldpeak": "2.4", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 335 | 336 | 336 |
| 517 | 518 | 518 |
| 876 | 877 | 877 |
| 930 | 931 | 931 |

### Group 224 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "2", "trestbps": "125", "chol": "273", "fbs": "0", "restecg": "0", "thalach": "152", "exang": "0", "oldpeak": "0.5", "slope": "0", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 338 | 339 | 339 |
| 417 | 418 | 418 |
| 545 | 546 | 546 |

### Group 225 — 3 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "130", "chol": "253", "fbs": "0", "restecg": "1", "thalach": "144", "exang": "1", "oldpeak": "1.4", "slope": "2", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 340 | 341 | 341 |
| 677 | 678 | 678 |
| 823 | 824 | 824 |

### Group 226 — 3 occurrences

Key: `{"age": "65", "sex": "0", "cp": "2", "trestbps": "155", "chol": "269", "fbs": "0", "restecg": "1", "thalach": "148", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 343 | 344 | 344 |
| 532 | 533 | 533 |
| 562 | 563 | 563 |

### Group 227 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "2", "trestbps": "172", "chol": "199", "fbs": "1", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "0.5", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 344 | 345 | 345 |
| 838 | 839 | 839 |
| 972 | 973 | 973 |

### Group 228 — 3 occurrences

Key: `{"age": "43", "sex": "1", "cp": "0", "trestbps": "132", "chol": "247", "fbs": "1", "restecg": "0", "thalach": "143", "exang": "1", "oldpeak": "0.1", "slope": "1", "ca": "4", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 349 | 350 | 350 |
| 429 | 430 | 430 |
| 994 | 995 | 995 |

### Group 229 — 4 occurrences

Key: `{"age": "62", "sex": "0", "cp": "2", "trestbps": "130", "chol": "263", "fbs": "0", "restecg": "1", "thalach": "97", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 350 | 351 | 351 |
| 601 | 602 | 602 |
| 896 | 897 | 897 |
| 952 | 953 | 953 |

### Group 230 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "110", "chol": "201", "fbs": "0", "restecg": "1", "thalach": "126", "exang": "1", "oldpeak": "1.5", "slope": "1", "ca": "0", "thal": "1", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 354 | 355 | 355 |
| 704 | 705 | 705 |
| 888 | 889 | 889 |

### Group 231 — 3 occurrences

Key: `{"age": "46", "sex": "0", "cp": "0", "trestbps": "138", "chol": "243", "fbs": "0", "restecg": "0", "thalach": "152", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 356 | 357 | 357 |
| 409 | 410 | 410 |
| 641 | 642 | 642 |

### Group 232 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "164", "chol": "176", "fbs": "1", "restecg": "0", "thalach": "90", "exang": "0", "oldpeak": "1", "slope": "1", "ca": "2", "thal": "1", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 357 | 358 | 358 |
| 588 | 589 | 589 |
| 683 | 684 | 684 |

### Group 233 — 4 occurrences

Key: `{"age": "59", "sex": "1", "cp": "3", "trestbps": "134", "chol": "204", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "2", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 359 | 360 | 360 |
| 544 | 545 | 545 |
| 779 | 780 | 780 |
| 919 | 920 | 920 |

### Group 234 — 3 occurrences

Key: `{"age": "62", "sex": "1", "cp": "2", "trestbps": "130", "chol": "231", "fbs": "0", "restecg": "1", "thalach": "146", "exang": "0", "oldpeak": "1.8", "slope": "1", "ca": "3", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 362 | 363 | 363 |
| 956 | 957 | 957 |
| 986 | 987 | 987 |

### Group 235 — 3 occurrences

Key: `{"age": "53", "sex": "1", "cp": "2", "trestbps": "130", "chol": "246", "fbs": "1", "restecg": "0", "thalach": "173", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "3", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 364 | 365 | 365 |
| 366 | 367 | 367 |
| 447 | 448 | 448 |

### Group 236 — 3 occurrences

Key: `{"age": "58", "sex": "1", "cp": "2", "trestbps": "112", "chol": "230", "fbs": "0", "restecg": "0", "thalach": "165", "exang": "0", "oldpeak": "2.5", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 367 | 368 | 368 |
| 525 | 526 | 526 |
| 843 | 844 | 844 |

### Group 237 — 4 occurrences

Key: `{"age": "48", "sex": "1", "cp": "1", "trestbps": "110", "chol": "229", "fbs": "0", "restecg": "1", "thalach": "168", "exang": "0", "oldpeak": "1", "slope": "0", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 368 | 369 | 369 |
| 475 | 476 | 476 |
| 546 | 547 | 547 |
| 1013 | 1014 | 1014 |

### Group 238 — 3 occurrences

Key: `{"age": "58", "sex": "1", "cp": "2", "trestbps": "105", "chol": "240", "fbs": "0", "restecg": "0", "thalach": "154", "exang": "1", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 369 | 370 | 370 |
| 691 | 692 | 692 |
| 816 | 817 | 817 |

### Group 239 — 3 occurrences

Key: `{"age": "51", "sex": "1", "cp": "2", "trestbps": "110", "chol": "175", "fbs": "0", "restecg": "1", "thalach": "123", "exang": "0", "oldpeak": "0.6", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 370 | 371 | 371 |
| 386 | 387 | 387 |
| 393 | 394 | 394 |

### Group 240 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "1", "trestbps": "120", "chol": "284", "fbs": "0", "restecg": "0", "thalach": "160", "exang": "0", "oldpeak": "1.8", "slope": "1", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 374 | 375 | 375 |
| 440 | 441 | 441 |
| 599 | 600 | 600 |
| 851 | 852 | 852 |

### Group 241 — 3 occurrences

Key: `{"age": "46", "sex": "0", "cp": "2", "trestbps": "142", "chol": "177", "fbs": "0", "restecg": "0", "thalach": "160", "exang": "1", "oldpeak": "1.4", "slope": "0", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 375 | 376 | 376 |
| 500 | 501 | 501 |
| 503 | 504 | 504 |

### Group 242 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "1", "trestbps": "140", "chol": "221", "fbs": "0", "restecg": "1", "thalach": "164", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 377 | 378 | 378 |
| 597 | 598 | 598 |
| 1021 | 1022 | 1022 |

### Group 243 — 3 occurrences

Key: `{"age": "64", "sex": "0", "cp": "0", "trestbps": "130", "chol": "303", "fbs": "0", "restecg": "1", "thalach": "122", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "2", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 378 | 379 | 379 |
| 648 | 649 | 649 |
| 783 | 784 | 784 |

### Group 244 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "146", "chol": "218", "fbs": "0", "restecg": "1", "thalach": "105", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 381 | 382 | 382 |
| 580 | 581 | 581 |
| 782 | 783 | 783 |
| 922 | 923 | 923 |

### Group 245 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "110", "chol": "239", "fbs": "0", "restecg": "0", "thalach": "142", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 383 | 384 | 384 |
| 737 | 738 | 738 |
| 995 | 996 | 996 |

### Group 246 — 3 occurrences

Key: `{"age": "35", "sex": "1", "cp": "0", "trestbps": "126", "chol": "282", "fbs": "0", "restecg": "0", "thalach": "156", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 385 | 386 | 386 |
| 696 | 697 | 697 |
| 700 | 701 | 701 |

### Group 247 — 3 occurrences

Key: `{"age": "63", "sex": "1", "cp": "3", "trestbps": "145", "chol": "233", "fbs": "1", "restecg": "0", "thalach": "150", "exang": "0", "oldpeak": "2.3", "slope": "0", "ca": "0", "thal": "1", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 390 | 391 | 391 |
| 400 | 401 | 401 |
| 802 | 803 | 803 |

### Group 248 — 3 occurrences

Key: `{"age": "45", "sex": "1", "cp": "3", "trestbps": "110", "chol": "264", "fbs": "0", "restecg": "1", "thalach": "132", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 392 | 393 | 393 |
| 631 | 632 | 632 |
| 710 | 711 | 711 |

### Group 249 — 3 occurrences

Key: `{"age": "68", "sex": "1", "cp": "2", "trestbps": "180", "chol": "274", "fbs": "1", "restecg": "0", "thalach": "150", "exang": "1", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 397 | 398 | 398 |
| 497 | 498 | 498 |
| 680 | 681 | 681 |

### Group 250 — 3 occurrences

Key: `{"age": "70", "sex": "1", "cp": "1", "trestbps": "156", "chol": "245", "fbs": "0", "restecg": "0", "thalach": "143", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 403 | 404 | 404 |
| 716 | 717 | 717 |
| 817 | 818 | 818 |

### Group 251 — 3 occurrences

Key: `{"age": "42", "sex": "0", "cp": "0", "trestbps": "102", "chol": "265", "fbs": "0", "restecg": "0", "thalach": "122", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 422 | 423 | 423 |
| 899 | 900 | 900 |
| 902 | 903 | 903 |

### Group 252 — 3 occurrences

Key: `{"age": "51", "sex": "0", "cp": "0", "trestbps": "130", "chol": "305", "fbs": "0", "restecg": "1", "thalach": "142", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 426 | 427 | 427 |
| 481 | 482 | 482 |
| 615 | 616 | 616 |

### Group 253 — 3 occurrences

Key: `{"age": "54", "sex": "0", "cp": "2", "trestbps": "160", "chol": "201", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 427 | 428 | 428 |
| 569 | 570 | 570 |
| 948 | 949 | 949 |

### Group 254 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "2", "trestbps": "150", "chol": "168", "fbs": "0", "restecg": "1", "thalach": "174", "exang": "0", "oldpeak": "1.6", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 428 | 429 | 429 |
| 444 | 445 | 445 |
| 492 | 493 | 493 |

### Group 255 — 4 occurrences

Key: `{"age": "47", "sex": "1", "cp": "2", "trestbps": "108", "chol": "243", "fbs": "0", "restecg": "1", "thalach": "152", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 430 | 431 | 431 |
| 457 | 458 | 458 |
| 505 | 506 | 506 |
| 647 | 648 | 648 |

### Group 256 — 4 occurrences

Key: `{"age": "65", "sex": "0", "cp": "0", "trestbps": "150", "chol": "225", "fbs": "0", "restecg": "0", "thalach": "114", "exang": "0", "oldpeak": "1", "slope": "1", "ca": "3", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 432 | 433 | 433 |
| 455 | 456 | 456 |
| 774 | 775 | 775 |
| 798 | 799 | 799 |

### Group 257 — 3 occurrences

Key: `{"age": "41", "sex": "0", "cp": "2", "trestbps": "112", "chol": "268", "fbs": "0", "restecg": "0", "thalach": "172", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 435 | 436 | 436 |
| 679 | 680 | 680 |
| 742 | 743 | 743 |

### Group 258 — 4 occurrences

Key: `{"age": "67", "sex": "1", "cp": "0", "trestbps": "120", "chol": "229", "fbs": "0", "restecg": "0", "thalach": "129", "exang": "1", "oldpeak": "2.6", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 438 | 439 | 439 |
| 738 | 739 | 739 |
| 801 | 802 | 802 |
| 854 | 855 | 855 |

### Group 259 — 4 occurrences

Key: `{"age": "47", "sex": "1", "cp": "2", "trestbps": "130", "chol": "253", "fbs": "0", "restecg": "1", "thalach": "179", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 439 | 440 | 440 |
| 445 | 446 | 446 |
| 605 | 606 | 606 |
| 918 | 919 | 919 |

### Group 260 — 4 occurrences

Key: `{"age": "52", "sex": "1", "cp": "0", "trestbps": "112", "chol": "230", "fbs": "0", "restecg": "1", "thalach": "160", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 450 | 451 | 451 |
| 732 | 733 | 733 |
| 804 | 805 | 805 |
| 861 | 862 | 862 |

### Group 261 — 4 occurrences

Key: `{"age": "63", "sex": "0", "cp": "0", "trestbps": "150", "chol": "407", "fbs": "0", "restecg": "0", "thalach": "154", "exang": "0", "oldpeak": "4", "slope": "1", "ca": "3", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 451 | 452 | 452 |
| 482 | 483 | 483 |
| 686 | 687 | 687 |
| 890 | 891 | 891 |

### Group 262 — 3 occurrences

Key: `{"age": "49", "sex": "0", "cp": "1", "trestbps": "134", "chol": "271", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 452 | 453 | 453 |
| 454 | 455 | 455 |
| 940 | 941 | 941 |

### Group 263 — 3 occurrences

Key: `{"age": "69", "sex": "1", "cp": "2", "trestbps": "140", "chol": "254", "fbs": "0", "restecg": "0", "thalach": "146", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "3", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 461 | 462 | 462 |
| 551 | 552 | 552 |
| 626 | 627 | 627 |

### Group 264 — 4 occurrences

Key: `{"age": "58", "sex": "0", "cp": "0", "trestbps": "130", "chol": "197", "fbs": "0", "restecg": "1", "thalach": "131", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 473 | 474 | 474 |
| 561 | 562 | 562 |
| 640 | 641 | 641 |
| 805 | 806 | 806 |

### Group 265 — 3 occurrences

Key: `{"age": "41", "sex": "1", "cp": "2", "trestbps": "130", "chol": "214", "fbs": "0", "restecg": "0", "thalach": "168", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 474 | 475 | 475 |
| 568 | 569 | 569 |
| 701 | 702 | 702 |

### Group 266 — 3 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "128", "chol": "216", "fbs": "0", "restecg": "0", "thalach": "131", "exang": "1", "oldpeak": "2.2", "slope": "1", "ca": "3", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 480 | 481 | 481 |
| 706 | 707 | 707 |
| 1016 | 1017 | 1017 |

### Group 267 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "135", "chol": "234", "fbs": "0", "restecg": "1", "thalach": "161", "exang": "0", "oldpeak": "0.5", "slope": "1", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 496 | 497 | 497 |
| 900 | 901 | 901 |
| 985 | 986 | 986 |

### Group 268 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "140", "chol": "239", "fbs": "0", "restecg": "1", "thalach": "160", "exang": "0", "oldpeak": "1.2", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 499 | 500 | 500 |
| 824 | 825 | 825 |
| 924 | 925 | 925 |

### Group 269 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "0", "trestbps": "112", "chol": "290", "fbs": "0", "restecg": "0", "thalach": "153", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 513 | 514 | 514 |
| 564 | 565 | 565 |
| 574 | 575 | 575 |

### Group 270 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "1", "trestbps": "125", "chol": "220", "fbs": "0", "restecg": "1", "thalach": "144", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "4", "thal": "3", "target": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 522 | 523 | 523 |
| 744 | 745 | 745 |
| 750 | 751 | 751 |
| 832 | 833 | 833 |

### Group 271 — 3 occurrences

Key: `{"age": "67", "sex": "0", "cp": "2", "trestbps": "152", "chol": "277", "fbs": "0", "restecg": "1", "thalach": "172", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 523 | 524 | 524 |
| 723 | 724 | 724 |
| 947 | 948 | 948 |

### Group 272 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "3", "trestbps": "178", "chol": "270", "fbs": "0", "restecg": "0", "thalach": "145", "exang": "0", "oldpeak": "4.2", "slope": "0", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 529 | 530 | 530 |
| 625 | 626 | 626 |
| 897 | 898 | 898 |

### Group 273 — 3 occurrences

Key: `{"age": "60", "sex": "0", "cp": "0", "trestbps": "150", "chol": "258", "fbs": "0", "restecg": "0", "thalach": "157", "exang": "0", "oldpeak": "2.6", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 531 | 532 | 532 |
| 726 | 727 | 727 |
| 889 | 890 | 890 |

### Group 274 — 3 occurrences

Key: `{"age": "53", "sex": "0", "cp": "0", "trestbps": "138", "chol": "234", "fbs": "0", "restecg": "0", "thalach": "160", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 534 | 535 | 535 |
| 566 | 567 | 567 |
| 837 | 838 | 838 |

### Group 275 — 3 occurrences

Key: `{"age": "50", "sex": "0", "cp": "2", "trestbps": "120", "chol": "219", "fbs": "0", "restecg": "1", "thalach": "158", "exang": "0", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 537 | 538 | 538 |
| 616 | 617 | 617 |
| 697 | 698 | 698 |

### Group 276 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "2", "trestbps": "140", "chol": "235", "fbs": "0", "restecg": "0", "thalach": "180", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 542 | 543 | 543 |
| 582 | 583 | 583 |
| 741 | 742 | 742 |

### Group 277 — 3 occurrences

Key: `{"age": "68", "sex": "1", "cp": "2", "trestbps": "118", "chol": "277", "fbs": "0", "restecg": "1", "thalach": "151", "exang": "0", "oldpeak": "1", "slope": "2", "ca": "1", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 550 | 551 | 551 |
| 673 | 674 | 674 |
| 833 | 834 | 834 |

### Group 278 — 3 occurrences

Key: `{"age": "67", "sex": "1", "cp": "0", "trestbps": "125", "chol": "254", "fbs": "1", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0.2", "slope": "1", "ca": "2", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 556 | 557 | 557 |
| 787 | 788 | 788 |
| 1000 | 1001 | 1001 |

### Group 279 — 3 occurrences

Key: `{"age": "50", "sex": "0", "cp": "0", "trestbps": "110", "chol": "254", "fbs": "0", "restecg": "0", "thalach": "159", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 567 | 568 | 568 |
| 993 | 994 | 994 |
| 1024 | 1025 | 1025 |

### Group 280 — 3 occurrences

Key: `{"age": "54", "sex": "0", "cp": "2", "trestbps": "135", "chol": "304", "fbs": "1", "restecg": "1", "thalach": "170", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 571 | 572 | 572 |
| 690 | 691 | 691 |
| 953 | 954 | 954 |

### Group 281 — 3 occurrences

Key: `{"age": "46", "sex": "1", "cp": "1", "trestbps": "101", "chol": "197", "fbs": "1", "restecg": "1", "thalach": "156", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 581 | 582 | 582 |
| 769 | 770 | 770 |
| 856 | 857 | 857 |

### Group 282 — 3 occurrences

Key: `{"age": "55", "sex": "1", "cp": "1", "trestbps": "130", "chol": "262", "fbs": "0", "restecg": "1", "thalach": "155", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 583 | 584 | 584 |
| 751 | 752 | 752 |
| 905 | 906 | 906 |

### Group 283 — 3 occurrences

Key: `{"age": "64", "sex": "1", "cp": "0", "trestbps": "145", "chol": "212", "fbs": "0", "restecg": "0", "thalach": "132", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "2", "thal": "1", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 595 | 596 | 596 |
| 609 | 610 | 610 |
| 1001 | 1002 | 1002 |

### Group 284 — 3 occurrences

Key: `{"age": "63", "sex": "0", "cp": "1", "trestbps": "140", "chol": "195", "fbs": "0", "restecg": "1", "thalach": "179", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "2", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 600 | 601 | 601 |
| 604 | 605 | 605 |
| 694 | 695 | 695 |

### Group 285 — 4 occurrences

Key: `{"age": "66", "sex": "1", "cp": "0", "trestbps": "112", "chol": "212", "fbs": "0", "restecg": "0", "thalach": "132", "exang": "1", "oldpeak": "0.1", "slope": "2", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 607 | 608 | 608 |
| 699 | 700 | 700 |
| 915 | 916 | 916 |
| 1003 | 1004 | 1004 |

### Group 286 — 4 occurrences

Key: `{"age": "55", "sex": "0", "cp": "0", "trestbps": "128", "chol": "205", "fbs": "0", "restecg": "2", "thalach": "130", "exang": "1", "oldpeak": "2", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 612 | 613 | 613 |
| 717 | 718 | 718 |
| 891 | 892 | 892 |
| 1006 | 1007 | 1007 |

### Group 287 — 3 occurrences

Key: `{"age": "43", "sex": "1", "cp": "0", "trestbps": "115", "chol": "303", "fbs": "0", "restecg": "1", "thalach": "181", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 617 | 618 | 618 |
| 800 | 801 | 801 |
| 858 | 859 | 859 |

### Group 288 — 3 occurrences

Key: `{"age": "69", "sex": "0", "cp": "3", "trestbps": "140", "chol": "239", "fbs": "0", "restecg": "1", "thalach": "151", "exang": "0", "oldpeak": "1.8", "slope": "2", "ca": "2", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 629 | 630 | 630 |
| 943 | 944 | 944 |
| 960 | 961 | 961 |

### Group 289 — 4 occurrences

Key: `{"age": "65", "sex": "1", "cp": "3", "trestbps": "138", "chol": "282", "fbs": "1", "restecg": "0", "thalach": "174", "exang": "0", "oldpeak": "1.4", "slope": "1", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 630 | 631 | 631 |
| 639 | 640 | 640 |
| 855 | 856 | 856 |
| 1017 | 1018 | 1018 |

### Group 290 — 4 occurrences

Key: `{"age": "61", "sex": "1", "cp": "0", "trestbps": "138", "chol": "166", "fbs": "0", "restecg": "0", "thalach": "125", "exang": "1", "oldpeak": "3.6", "slope": "1", "ca": "1", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 634 | 635 | 635 |
| 661 | 662 | 662 |
| 825 | 826 | 826 |
| 848 | 849 | 849 |

### Group 291 — 3 occurrences

Key: `{"age": "65", "sex": "1", "cp": "0", "trestbps": "120", "chol": "177", "fbs": "0", "restecg": "1", "thalach": "140", "exang": "0", "oldpeak": "0.4", "slope": "2", "ca": "0", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 644 | 645 | 645 |
| 754 | 755 | 755 |
| 944 | 945 | 945 |

### Group 292 — 3 occurrences

Key: `{"age": "66", "sex": "0", "cp": "3", "trestbps": "150", "chol": "226", "fbs": "0", "restecg": "1", "thalach": "114", "exang": "0", "oldpeak": "2.6", "slope": "0", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 653 | 654 | 654 |
| 665 | 666 | 666 |
| 714 | 715 | 715 |

### Group 293 — 3 occurrences

Key: `{"age": "55", "sex": "0", "cp": "1", "trestbps": "135", "chol": "250", "fbs": "0", "restecg": "0", "thalach": "161", "exang": "0", "oldpeak": "1.4", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 692 | 693 | 693 |
| 719 | 720 | 720 |
| 730 | 731 | 731 |

### Group 294 — 4 occurrences

Key: `{"age": "39", "sex": "1", "cp": "0", "trestbps": "118", "chol": "219", "fbs": "0", "restecg": "1", "thalach": "140", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "3", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 695 | 696 | 696 |
| 921 | 922 | 922 |
| 976 | 977 | 977 |
| 982 | 983 | 983 |

### Group 295 — 3 occurrences

Key: `{"age": "60", "sex": "0", "cp": "2", "trestbps": "120", "chol": "178", "fbs": "1", "restecg": "1", "thalach": "96", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 709 | 710 | 710 |
| 794 | 795 | 795 |
| 968 | 969 | 969 |

### Group 296 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "0", "trestbps": "108", "chol": "233", "fbs": "1", "restecg": "1", "thalach": "147", "exang": "0", "oldpeak": "0.1", "slope": "2", "ca": "3", "thal": "3", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 720 | 721 | 721 |
| 963 | 964 | 964 |
| 1004 | 1005 | 1005 |

### Group 297 — 4 occurrences

Key: `{"age": "64", "sex": "1", "cp": "2", "trestbps": "140", "chol": "335", "fbs": "0", "restecg": "1", "thalach": "158", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 721 | 722 | 722 |
| 747 | 748 | 748 |
| 862 | 863 | 863 |
| 938 | 939 | 939 |

### Group 298 — 3 occurrences

Key: `{"age": "68", "sex": "0", "cp": "2", "trestbps": "120", "chol": "211", "fbs": "0", "restecg": "0", "thalach": "115", "exang": "0", "oldpeak": "1.5", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 724 | 725 | 725 |
| 857 | 858 | 858 |
| 859 | 860 | 860 |

### Group 299 — 3 occurrences

Key: `{"age": "44", "sex": "0", "cp": "2", "trestbps": "108", "chol": "141", "fbs": "0", "restecg": "1", "thalach": "175", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "2", "target": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 734 | 735 | 735 |
| 965 | 966 | 966 |
| 1015 | 1016 | 1016 |

### Group 300 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "0", "trestbps": "128", "chol": "255", "fbs": "0", "restecg": "1", "thalach": "161", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 740 | 741 | 741 |
| 850 | 851 | 851 |
| 853 | 854 | 854 |

### Group 301 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "3", "trestbps": "160", "chol": "273", "fbs": "0", "restecg": "0", "thalach": "125", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 844 | 845 | 845 |
| 865 | 866 | 866 |
| 875 | 876 | 876 |

### Group 302 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "120", "chol": "188", "fbs": "0", "restecg": "1", "thalach": "113", "exang": "0", "oldpeak": "1.4", "slope": "1", "ca": "1", "thal": "3", "target": "0"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 879 | 880 | 880 |
| 998 | 999 | 999 |
| 1025 | 1026 | 1026 |

## Feature-only duplicates (target excluded)

### Group 1 — 4 occurrences

Key: `{"age": "52", "sex": "1", "cp": "0", "trestbps": "125", "chol": "212", "fbs": "0", "restecg": "1", "thalach": "168", "exang": "0", "oldpeak": "1", "slope": "2", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 1 | 2 | 2 |
| 635 | 636 | 636 |
| 672 | 673 | 673 |
| 864 | 865 | 865 |

### Group 2 — 4 occurrences

Key: `{"age": "53", "sex": "1", "cp": "0", "trestbps": "140", "chol": "203", "fbs": "1", "restecg": "0", "thalach": "155", "exang": "1", "oldpeak": "3.1", "slope": "0", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 2 | 3 | 3 |
| 693 | 694 | 694 |
| 814 | 815 | 815 |
| 969 | 970 | 970 |

### Group 3 — 4 occurrences

Key: `{"age": "70", "sex": "1", "cp": "0", "trestbps": "145", "chol": "174", "fbs": "0", "restecg": "1", "thalach": "125", "exang": "1", "oldpeak": "2.6", "slope": "0", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 3 | 4 | 4 |
| 841 | 842 | 842 |
| 885 | 886 | 886 |
| 949 | 950 | 950 |

### Group 4 — 4 occurrences

Key: `{"age": "61", "sex": "1", "cp": "0", "trestbps": "148", "chol": "203", "fbs": "0", "restecg": "1", "thalach": "161", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 4 | 5 | 5 |
| 520 | 521 | 521 |
| 524 | 525 | 525 |
| 596 | 597 | 597 |

### Group 5 — 3 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "138", "chol": "294", "fbs": "1", "restecg": "1", "thalach": "106", "exang": "0", "oldpeak": "1.9", "slope": "1", "ca": "3", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 5 | 6 | 6 |
| 623 | 624 | 624 |
| 789 | 790 | 790 |

### Group 6 — 3 occurrences

Key: `{"age": "58", "sex": "0", "cp": "0", "trestbps": "100", "chol": "248", "fbs": "0", "restecg": "0", "thalach": "122", "exang": "0", "oldpeak": "1", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 6 | 7 | 7 |
| 664 | 665 | 665 |
| 962 | 963 | 963 |

### Group 7 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "114", "chol": "318", "fbs": "0", "restecg": "2", "thalach": "140", "exang": "0", "oldpeak": "4.4", "slope": "0", "ca": "3", "thal": "1"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 7 | 8 | 8 |
| 151 | 152 | 152 |
| 662 | 663 | 663 |
| 1014 | 1015 | 1015 |

### Group 8 — 4 occurrences

Key: `{"age": "55", "sex": "1", "cp": "0", "trestbps": "160", "chol": "289", "fbs": "0", "restecg": "0", "thalach": "145", "exang": "1", "oldpeak": "0.8", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 8 | 9 | 9 |
| 279 | 280 | 280 |
| 448 | 449 | 449 |
| 786 | 787 | 787 |

### Group 9 — 4 occurrences

Key: `{"age": "46", "sex": "1", "cp": "0", "trestbps": "120", "chol": "249", "fbs": "0", "restecg": "0", "thalach": "144", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 9 | 10 | 10 |
| 44 | 45 | 45 |
| 539 | 540 | 540 |
| 916 | 917 | 917 |

### Group 10 — 4 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "122", "chol": "286", "fbs": "0", "restecg": "0", "thalach": "116", "exang": "1", "oldpeak": "3.2", "slope": "1", "ca": "2", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 10 | 11 | 11 |
| 220 | 221 | 221 |
| 552 | 553 | 553 |
| 590 | 591 | 591 |

### Group 11 — 4 occurrences

Key: `{"age": "71", "sex": "0", "cp": "0", "trestbps": "112", "chol": "149", "fbs": "0", "restecg": "1", "thalach": "125", "exang": "0", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 11 | 12 | 12 |
| 402 | 403 | 403 |
| 501 | 502 | 502 |
| 649 | 650 | 650 |

### Group 12 — 4 occurrences

Key: `{"age": "43", "sex": "0", "cp": "0", "trestbps": "132", "chol": "341", "fbs": "1", "restecg": "0", "thalach": "136", "exang": "1", "oldpeak": "3", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 12 | 13 | 13 |
| 371 | 372 | 372 |
| 553 | 554 | 554 |
| 611 | 612 | 612 |

### Group 13 — 3 occurrences

Key: `{"age": "34", "sex": "0", "cp": "1", "trestbps": "118", "chol": "210", "fbs": "0", "restecg": "1", "thalach": "192", "exang": "0", "oldpeak": "0.7", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 13 | 14 | 14 |
| 16 | 17 | 17 |
| 780 | 781 | 781 |

### Group 14 — 3 occurrences

Key: `{"age": "51", "sex": "1", "cp": "0", "trestbps": "140", "chol": "298", "fbs": "0", "restecg": "1", "thalach": "122", "exang": "1", "oldpeak": "4.2", "slope": "1", "ca": "3", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 14 | 15 | 15 |
| 483 | 484 | 484 |
| 788 | 789 | 789 |

### Group 15 — 4 occurrences

Key: `{"age": "52", "sex": "1", "cp": "0", "trestbps": "128", "chol": "204", "fbs": "1", "restecg": "1", "thalach": "156", "exang": "1", "oldpeak": "1", "slope": "1", "ca": "0", "thal": "0"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 15 | 16 | 16 |
| 687 | 688 | 688 |
| 735 | 736 | 736 |
| 894 | 895 | 895 |

### Group 16 — 3 occurrences

Key: `{"age": "51", "sex": "0", "cp": "2", "trestbps": "140", "chol": "308", "fbs": "0", "restecg": "0", "thalach": "142", "exang": "0", "oldpeak": "1.5", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 17 | 18 | 18 |
| 933 | 934 | 934 |
| 1005 | 1006 | 1006 |

### Group 17 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "124", "chol": "266", "fbs": "0", "restecg": "0", "thalach": "109", "exang": "1", "oldpeak": "2.2", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 18 | 19 | 19 |
| 830 | 831 | 831 |
| 929 | 930 | 930 |

### Group 18 — 3 occurrences

Key: `{"age": "50", "sex": "0", "cp": "1", "trestbps": "120", "chol": "244", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "1.1", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 19 | 20 | 20 |
| 32 | 33 | 33 |
| 908 | 909 | 909 |

### Group 19 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "2", "trestbps": "140", "chol": "211", "fbs": "1", "restecg": "0", "thalach": "165", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 20 | 21 | 21 |
| 87 | 88 | 88 |
| 407 | 408 | 408 |
| 1007 | 1008 | 1008 |

### Group 20 — 3 occurrences

Key: `{"age": "60", "sex": "1", "cp": "2", "trestbps": "140", "chol": "185", "fbs": "0", "restecg": "0", "thalach": "155", "exang": "0", "oldpeak": "3", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 21 | 22 | 22 |
| 244 | 245 | 245 |
| 685 | 686 | 686 |

### Group 21 — 3 occurrences

Key: `{"age": "67", "sex": "0", "cp": "0", "trestbps": "106", "chol": "223", "fbs": "0", "restecg": "1", "thalach": "142", "exang": "0", "oldpeak": "0.3", "slope": "2", "ca": "2", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 22 | 23 | 23 |
| 548 | 549 | 549 |
| 983 | 984 | 984 |

### Group 22 — 3 occurrences

Key: `{"age": "45", "sex": "1", "cp": "0", "trestbps": "104", "chol": "208", "fbs": "0", "restecg": "0", "thalach": "148", "exang": "1", "oldpeak": "3", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 23 | 24 | 24 |
| 266 | 267 | 267 |
| 914 | 915 | 915 |

### Group 23 — 3 occurrences

Key: `{"age": "63", "sex": "0", "cp": "2", "trestbps": "135", "chol": "252", "fbs": "0", "restecg": "0", "thalach": "172", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 24 | 25 | 25 |
| 318 | 319 | 319 |
| 826 | 827 | 827 |

### Group 24 — 3 occurrences

Key: `{"age": "42", "sex": "0", "cp": "2", "trestbps": "120", "chol": "209", "fbs": "0", "restecg": "1", "thalach": "173", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 25 | 26 | 26 |
| 387 | 388 | 388 |
| 563 | 564 | 564 |

### Group 25 — 4 occurrences

Key: `{"age": "61", "sex": "0", "cp": "0", "trestbps": "145", "chol": "307", "fbs": "0", "restecg": "0", "thalach": "146", "exang": "1", "oldpeak": "1", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 26 | 27 | 27 |
| 116 | 117 | 117 |
| 589 | 590 | 590 |
| 777 | 778 | 778 |

### Group 26 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "2", "trestbps": "130", "chol": "233", "fbs": "0", "restecg": "1", "thalach": "179", "exang": "1", "oldpeak": "0.4", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 27 | 28 | 28 |
| 808 | 809 | 809 |
| 829 | 830 | 830 |

### Group 27 — 4 occurrences

Key: `{"age": "58", "sex": "0", "cp": "1", "trestbps": "136", "chol": "319", "fbs": "1", "restecg": "0", "thalach": "152", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "2", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 28 | 29 | 29 |
| 391 | 392 | 392 |
| 424 | 425 | 425 |
| 912 | 913 | 913 |

### Group 28 — 4 occurrences

Key: `{"age": "56", "sex": "1", "cp": "2", "trestbps": "130", "chol": "256", "fbs": "1", "restecg": "0", "thalach": "142", "exang": "1", "oldpeak": "0.6", "slope": "1", "ca": "1", "thal": "1"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 29 | 30 | 30 |
| 339 | 340 | 340 |
| 406 | 407 | 407 |
| 718 | 719 | 719 |

### Group 29 — 4 occurrences

Key: `{"age": "55", "sex": "0", "cp": "0", "trestbps": "180", "chol": "327", "fbs": "0", "restecg": "2", "thalach": "117", "exang": "1", "oldpeak": "3.4", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 30 | 31 | 31 |
| 510 | 511 | 511 |
| 610 | 611 | 611 |
| 987 | 988 | 988 |

### Group 30 — 4 occurrences

Key: `{"age": "44", "sex": "1", "cp": "0", "trestbps": "120", "chol": "169", "fbs": "0", "restecg": "1", "thalach": "144", "exang": "1", "oldpeak": "2.8", "slope": "0", "ca": "0", "thal": "1"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 31 | 32 | 32 |
| 94 | 95 | 95 |
| 122 | 123 | 123 |
| 781 | 782 | 782 |

### Group 31 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "130", "chol": "131", "fbs": "0", "restecg": "1", "thalach": "115", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 33 | 34 | 34 |
| 883 | 884 | 884 |
| 926 | 927 | 927 |

### Group 32 — 3 occurrences

Key: `{"age": "70", "sex": "1", "cp": "2", "trestbps": "160", "chol": "269", "fbs": "0", "restecg": "1", "thalach": "112", "exang": "1", "oldpeak": "2.9", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 34 | 35 | 35 |
| 313 | 314 | 314 |
| 593 | 594 | 594 |

### Group 33 — 3 occurrences

Key: `{"age": "50", "sex": "1", "cp": "2", "trestbps": "129", "chol": "196", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 35 | 36 | 36 |
| 134 | 135 | 135 |
| 736 | 737 | 737 |

### Group 34 — 3 occurrences

Key: `{"age": "46", "sex": "1", "cp": "2", "trestbps": "150", "chol": "231", "fbs": "0", "restecg": "1", "thalach": "147", "exang": "0", "oldpeak": "3.6", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 36 | 37 | 37 |
| 83 | 84 | 84 |
| 410 | 411 | 411 |

### Group 35 — 3 occurrences

Key: `{"age": "51", "sex": "1", "cp": "3", "trestbps": "125", "chol": "213", "fbs": "0", "restecg": "0", "thalach": "125", "exang": "1", "oldpeak": "1.4", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 37 | 38 | 38 |
| 715 | 716 | 716 |
| 839 | 840 | 840 |

### Group 36 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "138", "chol": "271", "fbs": "0", "restecg": "0", "thalach": "182", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 38 | 39 | 39 |
| 660 | 661 | 661 |
| 880 | 881 | 881 |

### Group 37 — 3 occurrences

Key: `{"age": "64", "sex": "1", "cp": "0", "trestbps": "128", "chol": "263", "fbs": "0", "restecg": "1", "thalach": "105", "exang": "1", "oldpeak": "0.2", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 39 | 40 | 40 |
| 643 | 644 | 644 |
| 984 | 985 | 985 |

### Group 38 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "2", "trestbps": "128", "chol": "229", "fbs": "0", "restecg": "0", "thalach": "150", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 40 | 41 | 41 |
| 478 | 479 | 479 |
| 707 | 708 | 708 |
| 828 | 829 | 829 |

### Group 39 — 3 occurrences

Key: `{"age": "65", "sex": "0", "cp": "2", "trestbps": "160", "chol": "360", "fbs": "0", "restecg": "0", "thalach": "151", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 41 | 42 | 42 |
| 420 | 421 | 421 |
| 752 | 753 | 753 |

### Group 40 — 4 occurrences

Key: `{"age": "54", "sex": "1", "cp": "2", "trestbps": "120", "chol": "258", "fbs": "0", "restecg": "0", "thalach": "147", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 42 | 43 | 43 |
| 154 | 155 | 155 |
| 158 | 159 | 159 |
| 674 | 675 | 675 |

### Group 41 — 4 occurrences

Key: `{"age": "61", "sex": "0", "cp": "0", "trestbps": "130", "chol": "330", "fbs": "0", "restecg": "0", "thalach": "169", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 43 | 44 | 44 |
| 671 | 672 | 672 |
| 760 | 761 | 761 |
| 925 | 926 | 926 |

### Group 42 — 4 occurrences

Key: `{"age": "55", "sex": "0", "cp": "1", "trestbps": "132", "chol": "342", "fbs": "0", "restecg": "1", "thalach": "166", "exang": "0", "oldpeak": "1.2", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 45 | 46 | 46 |
| 137 | 138 | 138 |
| 264 | 265 | 265 |
| 303 | 304 | 304 |

### Group 43 — 3 occurrences

Key: `{"age": "42", "sex": "1", "cp": "0", "trestbps": "140", "chol": "226", "fbs": "0", "restecg": "1", "thalach": "178", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 46 | 47 | 47 |
| 907 | 908 | 908 |
| 1002 | 1003 | 1003 |

### Group 44 — 4 occurrences

Key: `{"age": "41", "sex": "1", "cp": "1", "trestbps": "135", "chol": "203", "fbs": "0", "restecg": "1", "thalach": "132", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 47 | 48 | 48 |
| 133 | 134 | 134 |
| 771 | 772 | 772 |
| 797 | 798 | 798 |

### Group 45 — 4 occurrences

Key: `{"age": "66", "sex": "0", "cp": "0", "trestbps": "178", "chol": "228", "fbs": "1", "restecg": "1", "thalach": "165", "exang": "1", "oldpeak": "1", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 48 | 49 | 49 |
| 230 | 231 | 231 |
| 453 | 454 | 454 |
| 945 | 946 | 946 |

### Group 46 — 4 occurrences

Key: `{"age": "66", "sex": "0", "cp": "2", "trestbps": "146", "chol": "278", "fbs": "0", "restecg": "0", "thalach": "152", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "1", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 49 | 50 | 50 |
| 62 | 63 | 63 |
| 205 | 206 | 206 |
| 396 | 397 | 397 |

### Group 47 — 4 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "117", "chol": "230", "fbs": "1", "restecg": "1", "thalach": "160", "exang": "1", "oldpeak": "1.4", "slope": "2", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 50 | 51 | 51 |
| 239 | 240 | 240 |
| 748 | 749 | 749 |
| 992 | 993 | 993 |

### Group 48 — 3 occurrences

Key: `{"age": "58", "sex": "0", "cp": "3", "trestbps": "150", "chol": "283", "fbs": "1", "restecg": "0", "thalach": "162", "exang": "0", "oldpeak": "1", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 51 | 52 | 52 |
| 764 | 765 | 765 |
| 849 | 850 | 850 |

### Group 49 — 3 occurrences

Key: `{"age": "57", "sex": "0", "cp": "0", "trestbps": "140", "chol": "241", "fbs": "0", "restecg": "1", "thalach": "123", "exang": "1", "oldpeak": "0.2", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 52 | 53 | 53 |
| 941 | 942 | 942 |
| 964 | 965 | 965 |

### Group 50 — 8 occurrences

Key: `{"age": "38", "sex": "1", "cp": "2", "trestbps": "138", "chol": "175", "fbs": "0", "restecg": "1", "thalach": "173", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "4", "thal": "2"}`

Target counts: {'1': 8}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 53 | 54 | 54 |
| 84 | 85 | 85 |
| 209 | 210 | 210 |
| 243 | 244 | 244 |
| 341 | 342 | 342 |
| 466 | 467 | 467 |
| 598 | 599 | 599 |
| 971 | 972 | 972 |

### Group 51 — 4 occurrences

Key: `{"age": "49", "sex": "1", "cp": "2", "trestbps": "120", "chol": "188", "fbs": "0", "restecg": "1", "thalach": "139", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "3", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 54 | 55 | 55 |
| 401 | 402 | 402 |
| 516 | 517 | 517 |
| 519 | 520 | 520 |

### Group 52 — 4 occurrences

Key: `{"age": "55", "sex": "1", "cp": "0", "trestbps": "140", "chol": "217", "fbs": "0", "restecg": "1", "thalach": "111", "exang": "1", "oldpeak": "5.6", "slope": "0", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 55 | 56 | 56 |
| 56 | 57 | 57 |
| 614 | 615 | 615 |
| 834 | 835 | 835 |

### Group 53 — 3 occurrences

Key: `{"age": "56", "sex": "1", "cp": "3", "trestbps": "120", "chol": "193", "fbs": "0", "restecg": "0", "thalach": "162", "exang": "0", "oldpeak": "1.9", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 57 | 58 | 58 |
| 946 | 947 | 947 |
| 1008 | 1009 | 1009 |

### Group 54 — 3 occurrences

Key: `{"age": "48", "sex": "1", "cp": "1", "trestbps": "130", "chol": "245", "fbs": "0", "restecg": "0", "thalach": "180", "exang": "0", "oldpeak": "0.2", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 58 | 59 | 59 |
| 325 | 326 | 326 |
| 753 | 754 | 754 |

### Group 55 — 4 occurrences

Key: `{"age": "67", "sex": "1", "cp": "2", "trestbps": "152", "chol": "212", "fbs": "0", "restecg": "0", "thalach": "150", "exang": "0", "oldpeak": "0.8", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 59 | 60 | 60 |
| 242 | 243 | 243 |
| 431 | 432 | 432 |
| 698 | 699 | 699 |

### Group 56 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "1", "trestbps": "154", "chol": "232", "fbs": "0", "restecg": "0", "thalach": "164", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 60 | 61 | 61 |
| 498 | 499 | 499 |
| 882 | 883 | 883 |
| 988 | 989 | 989 |

### Group 57 — 4 occurrences

Key: `{"age": "29", "sex": "1", "cp": "1", "trestbps": "130", "chol": "204", "fbs": "0", "restecg": "0", "thalach": "202", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 61 | 62 | 62 |
| 65 | 66 | 66 |
| 119 | 120 | 120 |
| 669 | 670 | 670 |

### Group 58 — 3 occurrences

Key: `{"age": "67", "sex": "1", "cp": "0", "trestbps": "100", "chol": "299", "fbs": "0", "restecg": "0", "thalach": "125", "exang": "1", "oldpeak": "0.9", "slope": "1", "ca": "2", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 63 | 64 | 64 |
| 212 | 213 | 213 |
| 296 | 297 | 297 |

### Group 59 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "2", "trestbps": "150", "chol": "212", "fbs": "1", "restecg": "1", "thalach": "157", "exang": "0", "oldpeak": "1.6", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 64 | 65 | 65 |
| 196 | 197 | 197 |
| 294 | 295 | 295 |

### Group 60 — 4 occurrences

Key: `{"age": "59", "sex": "1", "cp": "3", "trestbps": "170", "chol": "288", "fbs": "0", "restecg": "0", "thalach": "159", "exang": "0", "oldpeak": "0.2", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 66 | 67 | 67 |
| 415 | 416 | 416 |
| 799 | 800 | 800 |
| 863 | 864 | 864 |

### Group 61 — 3 occurrences

Key: `{"age": "53", "sex": "1", "cp": "2", "trestbps": "130", "chol": "197", "fbs": "1", "restecg": "0", "thalach": "152", "exang": "0", "oldpeak": "1.2", "slope": "0", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 67 | 68 | 68 |
| 128 | 129 | 129 |
| 554 | 555 | 555 |

### Group 62 — 4 occurrences

Key: `{"age": "42", "sex": "1", "cp": "0", "trestbps": "136", "chol": "315", "fbs": "0", "restecg": "1", "thalach": "125", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "0", "thal": "1"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 68 | 69 | 69 |
| 608 | 609 | 609 |
| 835 | 836 | 836 |
| 999 | 1000 | 1000 |

### Group 63 — 3 occurrences

Key: `{"age": "37", "sex": "0", "cp": "2", "trestbps": "120", "chol": "215", "fbs": "0", "restecg": "1", "thalach": "170", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 69 | 70 | 70 |
| 85 | 86 | 86 |
| 331 | 332 | 332 |

### Group 64 — 3 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "160", "chol": "164", "fbs": "0", "restecg": "0", "thalach": "145", "exang": "0", "oldpeak": "6.2", "slope": "0", "ca": "3", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 70 | 71 | 71 |
| 394 | 395 | 395 |
| 527 | 528 | 528 |

### Group 65 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "170", "chol": "326", "fbs": "0", "restecg": "0", "thalach": "140", "exang": "1", "oldpeak": "3.4", "slope": "0", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 71 | 72 | 72 |
| 166 | 167 | 167 |
| 682 | 683 | 683 |

### Group 66 — 4 occurrences

Key: `{"age": "61", "sex": "1", "cp": "0", "trestbps": "140", "chol": "207", "fbs": "0", "restecg": "0", "thalach": "138", "exang": "1", "oldpeak": "1.9", "slope": "2", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 72 | 73 | 73 |
| 405 | 406 | 406 |
| 821 | 822 | 822 |
| 877 | 878 | 878 |

### Group 67 — 4 occurrences

Key: `{"age": "56", "sex": "1", "cp": "0", "trestbps": "125", "chol": "249", "fbs": "1", "restecg": "0", "thalach": "144", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 73 | 74 | 74 |
| 165 | 166 | 166 |
| 188 | 189 | 189 |
| 412 | 413 | 413 |

### Group 68 — 4 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "140", "chol": "177", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 74 | 75 | 75 |
| 319 | 320 | 320 |
| 521 | 522 | 522 |
| 557 | 558 | 558 |

### Group 69 — 4 occurrences

Key: `{"age": "48", "sex": "1", "cp": "0", "trestbps": "130", "chol": "256", "fbs": "1", "restecg": "0", "thalach": "150", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 75 | 76 | 76 |
| 113 | 114 | 114 |
| 312 | 313 | 313 |
| 622 | 623 | 623 |

### Group 70 — 3 occurrences

Key: `{"age": "47", "sex": "1", "cp": "2", "trestbps": "138", "chol": "257", "fbs": "0", "restecg": "0", "thalach": "156", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 76 | 77 | 77 |
| 104 | 105 | 105 |
| 139 | 140 | 140 |

### Group 71 — 3 occurrences

Key: `{"age": "48", "sex": "1", "cp": "2", "trestbps": "124", "chol": "255", "fbs": "1", "restecg": "1", "thalach": "175", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "2", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 77 | 78 | 78 |
| 462 | 463 | 463 |
| 756 | 757 | 757 |

### Group 72 — 4 occurrences

Key: `{"age": "63", "sex": "1", "cp": "0", "trestbps": "140", "chol": "187", "fbs": "0", "restecg": "0", "thalach": "144", "exang": "1", "oldpeak": "4", "slope": "2", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 78 | 79 | 79 |
| 93 | 94 | 94 |
| 181 | 182 | 182 |
| 765 | 766 | 766 |

### Group 73 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "1", "trestbps": "134", "chol": "201", "fbs": "0", "restecg": "1", "thalach": "158", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 79 | 80 | 80 |
| 80 | 81 | 81 |
| 898 | 899 | 899 |

### Group 74 — 3 occurrences

Key: `{"age": "50", "sex": "1", "cp": "2", "trestbps": "140", "chol": "233", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 81 | 82 | 82 |
| 911 | 912 | 912 |
| 958 | 959 | 959 |

### Group 75 — 4 occurrences

Key: `{"age": "49", "sex": "1", "cp": "2", "trestbps": "118", "chol": "149", "fbs": "0", "restecg": "0", "thalach": "126", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "3", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 82 | 83 | 83 |
| 227 | 228 | 228 |
| 237 | 238 | 238 |
| 836 | 837 | 837 |

### Group 76 — 4 occurrences

Key: `{"age": "44", "sex": "1", "cp": "1", "trestbps": "120", "chol": "220", "fbs": "0", "restecg": "1", "thalach": "170", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 86 | 87 | 87 |
| 308 | 309 | 309 |
| 515 | 516 | 516 |
| 731 | 732 | 732 |

### Group 77 — 3 occurrences

Key: `{"age": "59", "sex": "0", "cp": "0", "trestbps": "174", "chol": "249", "fbs": "0", "restecg": "1", "thalach": "143", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 88 | 89 | 89 |
| 437 | 438 | 438 |
| 637 | 638 | 638 |

### Group 78 — 4 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "140", "chol": "268", "fbs": "0", "restecg": "0", "thalach": "160", "exang": "0", "oldpeak": "3.6", "slope": "0", "ca": "2", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 89 | 90 | 90 |
| 813 | 814 | 814 |
| 822 | 823 | 823 |
| 903 | 904 | 904 |

### Group 79 — 3 occurrences

Key: `{"age": "68", "sex": "1", "cp": "0", "trestbps": "144", "chol": "193", "fbs": "1", "restecg": "1", "thalach": "141", "exang": "0", "oldpeak": "3.4", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 90 | 91 | 91 |
| 768 | 769 | 769 |
| 793 | 794 | 794 |

### Group 80 — 3 occurrences

Key: `{"age": "54", "sex": "0", "cp": "2", "trestbps": "108", "chol": "267", "fbs": "0", "restecg": "0", "thalach": "167", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 91 | 92 | 92 |
| 348 | 349 | 349 |
| 535 | 536 | 536 |

### Group 81 — 4 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "124", "chol": "209", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 92 | 93 | 93 |
| 201 | 202 | 202 |
| 419 | 420 | 420 |
| 528 | 529 | 529 |

### Group 82 — 3 occurrences

Key: `{"age": "62", "sex": "1", "cp": "1", "trestbps": "128", "chol": "208", "fbs": "1", "restecg": "0", "thalach": "140", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 95 | 96 | 96 |
| 796 | 797 | 797 |
| 815 | 816 | 816 |

### Group 83 — 3 occurrences

Key: `{"age": "45", "sex": "0", "cp": "0", "trestbps": "138", "chol": "236", "fbs": "0", "restecg": "0", "thalach": "152", "exang": "1", "oldpeak": "0.2", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 96 | 97 | 97 |
| 772 | 773 | 773 |
| 954 | 955 | 955 |

### Group 84 — 3 occurrences

Key: `{"age": "57", "sex": "0", "cp": "0", "trestbps": "128", "chol": "303", "fbs": "0", "restecg": "0", "thalach": "159", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 97 | 98 | 98 |
| 421 | 422 | 422 |
| 491 | 492 | 492 |

### Group 85 — 4 occurrences

Key: `{"age": "53", "sex": "1", "cp": "0", "trestbps": "123", "chol": "282", "fbs": "0", "restecg": "1", "thalach": "95", "exang": "1", "oldpeak": "2", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 98 | 99 | 99 |
| 267 | 268 | 268 |
| 778 | 779 | 779 |
| 1018 | 1019 | 1019 |

### Group 86 — 3 occurrences

Key: `{"age": "65", "sex": "1", "cp": "0", "trestbps": "110", "chol": "248", "fbs": "0", "restecg": "0", "thalach": "158", "exang": "0", "oldpeak": "0.6", "slope": "2", "ca": "2", "thal": "1"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 99 | 100 | 100 |
| 485 | 486 | 486 |
| 620 | 621 | 621 |

### Group 87 — 3 occurrences

Key: `{"age": "76", "sex": "0", "cp": "2", "trestbps": "140", "chol": "197", "fbs": "0", "restecg": "2", "thalach": "116", "exang": "0", "oldpeak": "1.1", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 100 | 101 | 101 |
| 536 | 537 | 537 |
| 966 | 967 | 967 |

### Group 88 — 3 occurrences

Key: `{"age": "43", "sex": "0", "cp": "2", "trestbps": "122", "chol": "213", "fbs": "0", "restecg": "1", "thalach": "165", "exang": "0", "oldpeak": "0.2", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 101 | 102 | 102 |
| 363 | 364 | 364 |
| 878 | 879 | 879 |

### Group 89 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "2", "trestbps": "150", "chol": "126", "fbs": "1", "restecg": "1", "thalach": "173", "exang": "0", "oldpeak": "0.2", "slope": "2", "ca": "1", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 102 | 103 | 103 |
| 337 | 338 | 338 |
| 476 | 477 | 477 |

### Group 90 — 4 occurrences

Key: `{"age": "54", "sex": "1", "cp": "1", "trestbps": "108", "chol": "309", "fbs": "0", "restecg": "1", "thalach": "156", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 103 | 104 | 104 |
| 121 | 122 | 122 |
| 135 | 136 | 136 |
| 156 | 157 | 157 |

### Group 91 — 4 occurrences

Key: `{"age": "52", "sex": "1", "cp": "3", "trestbps": "118", "chol": "186", "fbs": "0", "restecg": "0", "thalach": "190", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 105 | 106 | 106 |
| 380 | 381 | 381 |
| 463 | 464 | 464 |
| 973 | 974 | 974 |

### Group 92 — 4 occurrences

Key: `{"age": "47", "sex": "1", "cp": "0", "trestbps": "110", "chol": "275", "fbs": "0", "restecg": "0", "thalach": "118", "exang": "1", "oldpeak": "1", "slope": "1", "ca": "1", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 106 | 107 | 107 |
| 251 | 252 | 252 |
| 468 | 469 | 469 |
| 1023 | 1024 | 1024 |

### Group 93 — 4 occurrences

Key: `{"age": "51", "sex": "1", "cp": "0", "trestbps": "140", "chol": "299", "fbs": "0", "restecg": "1", "thalach": "173", "exang": "1", "oldpeak": "1.6", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 107 | 108 | 108 |
| 860 | 861 | 861 |
| 895 | 896 | 896 |
| 1011 | 1012 | 1012 |

### Group 94 — 4 occurrences

Key: `{"age": "62", "sex": "1", "cp": "1", "trestbps": "120", "chol": "281", "fbs": "0", "restecg": "0", "thalach": "103", "exang": "0", "oldpeak": "1.4", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 108 | 109 | 109 |
| 210 | 211 | 211 |
| 486 | 487 | 487 |
| 790 | 791 | 791 |

### Group 95 — 4 occurrences

Key: `{"age": "40", "sex": "1", "cp": "0", "trestbps": "152", "chol": "223", "fbs": "0", "restecg": "1", "thalach": "181", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 109 | 110 | 110 |
| 290 | 291 | 291 |
| 932 | 933 | 933 |
| 1010 | 1011 | 1011 |

### Group 96 — 4 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "110", "chol": "206", "fbs": "0", "restecg": "0", "thalach": "108", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "1", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 110 | 111 | 111 |
| 274 | 275 | 275 |
| 514 | 515 | 515 |
| 927 | 928 | 928 |

### Group 97 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "0", "trestbps": "110", "chol": "197", "fbs": "0", "restecg": "0", "thalach": "177", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 111 | 112 | 112 |
| 179 | 180 | 180 |
| 979 | 980 | 980 |

### Group 98 — 3 occurrences

Key: `{"age": "53", "sex": "1", "cp": "0", "trestbps": "142", "chol": "226", "fbs": "0", "restecg": "0", "thalach": "111", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 112 | 113 | 113 |
| 806 | 807 | 807 |
| 939 | 940 | 940 |

### Group 99 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "110", "chol": "335", "fbs": "0", "restecg": "1", "thalach": "143", "exang": "1", "oldpeak": "3", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 114 | 115 | 115 |
| 353 | 354 | 354 |
| 766 | 767 | 767 |
| 767 | 768 | 768 |

### Group 100 — 4 occurrences

Key: `{"age": "59", "sex": "1", "cp": "2", "trestbps": "126", "chol": "218", "fbs": "1", "restecg": "1", "thalach": "134", "exang": "0", "oldpeak": "2.2", "slope": "1", "ca": "1", "thal": "1"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 115 | 116 | 116 |
| 207 | 208 | 208 |
| 309 | 310 | 310 |
| 904 | 905 | 905 |

### Group 101 — 4 occurrences

Key: `{"age": "63", "sex": "1", "cp": "0", "trestbps": "130", "chol": "254", "fbs": "0", "restecg": "0", "thalach": "147", "exang": "0", "oldpeak": "1.4", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 117 | 118 | 118 |
| 189 | 190 | 190 |
| 222 | 223 | 223 |
| 678 | 679 | 679 |

### Group 102 — 4 occurrences

Key: `{"age": "43", "sex": "1", "cp": "0", "trestbps": "120", "chol": "177", "fbs": "0", "restecg": "0", "thalach": "120", "exang": "1", "oldpeak": "2.5", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 118 | 119 | 119 |
| 512 | 513 | 513 |
| 584 | 585 | 585 |
| 684 | 685 | 685 |

### Group 103 — 3 occurrences

Key: `{"age": "42", "sex": "1", "cp": "1", "trestbps": "120", "chol": "295", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 120 | 121 | 121 |
| 681 | 682 | 682 |
| 1009 | 1010 | 1010 |

### Group 104 — 3 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "145", "chol": "282", "fbs": "0", "restecg": "0", "thalach": "142", "exang": "1", "oldpeak": "2.8", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 123 | 124 | 124 |
| 304 | 305 | 305 |
| 572 | 573 | 573 |

### Group 105 — 3 occurrences

Key: `{"age": "65", "sex": "0", "cp": "2", "trestbps": "140", "chol": "417", "fbs": "1", "restecg": "0", "thalach": "157", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 124 | 125 | 125 |
| 666 | 667 | 667 |
| 959 | 960 | 960 |

### Group 106 — 4 occurrences

Key: `{"age": "61", "sex": "1", "cp": "0", "trestbps": "120", "chol": "260", "fbs": "0", "restecg": "1", "thalach": "140", "exang": "1", "oldpeak": "3.6", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 125 | 126 | 126 |
| 311 | 312 | 312 |
| 507 | 508 | 508 |
| 887 | 888 | 888 |

### Group 107 — 4 occurrences

Key: `{"age": "60", "sex": "0", "cp": "3", "trestbps": "150", "chol": "240", "fbs": "0", "restecg": "1", "thalach": "171", "exang": "0", "oldpeak": "0.9", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 126 | 127 | 127 |
| 131 | 132 | 132 |
| 471 | 472 | 472 |
| 866 | 867 | 867 |

### Group 108 — 3 occurrences

Key: `{"age": "66", "sex": "1", "cp": "0", "trestbps": "120", "chol": "302", "fbs": "0", "restecg": "0", "thalach": "151", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 127 | 128 | 128 |
| 260 | 261 | 261 |
| 351 | 352 | 352 |

### Group 109 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "2", "trestbps": "138", "chol": "223", "fbs": "0", "restecg": "1", "thalach": "169", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "4", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 129 | 130 | 130 |
| 291 | 292 | 292 |
| 418 | 419 | 419 |

### Group 110 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "140", "chol": "192", "fbs": "0", "restecg": "1", "thalach": "148", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "0", "thal": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 130 | 131 | 131 |
| 874 | 875 | 875 |
| 981 | 982 | 982 |

### Group 111 — 3 occurrences

Key: `{"age": "51", "sex": "0", "cp": "2", "trestbps": "130", "chol": "256", "fbs": "0", "restecg": "0", "thalach": "149", "exang": "0", "oldpeak": "0.5", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 132 | 133 | 133 |
| 526 | 527 | 527 |
| 755 | 756 | 756 |

### Group 112 — 4 occurrences

Key: `{"age": "58", "sex": "0", "cp": "0", "trestbps": "170", "chol": "225", "fbs": "1", "restecg": "0", "thalach": "146", "exang": "1", "oldpeak": "2.8", "slope": "1", "ca": "2", "thal": "1"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 136 | 137 | 137 |
| 265 | 266 | 266 |
| 613 | 614 | 614 |
| 820 | 821 | 821 |

### Group 113 — 3 occurrences

Key: `{"age": "64", "sex": "0", "cp": "0", "trestbps": "180", "chol": "325", "fbs": "0", "restecg": "1", "thalach": "154", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 138 | 139 | 139 |
| 258 | 259 | 259 |
| 892 | 893 | 893 |

### Group 114 — 3 occurrences

Key: `{"age": "41", "sex": "1", "cp": "1", "trestbps": "110", "chol": "235", "fbs": "0", "restecg": "1", "thalach": "153", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 140 | 141 | 141 |
| 656 | 657 | 657 |
| 868 | 869 | 869 |

### Group 115 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "152", "chol": "274", "fbs": "0", "restecg": "1", "thalach": "88", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 141 | 142 | 142 |
| 443 | 444 | 444 |
| 621 | 622 | 622 |

### Group 116 — 3 occurrences

Key: `{"age": "63", "sex": "0", "cp": "0", "trestbps": "124", "chol": "197", "fbs": "0", "restecg": "1", "thalach": "136", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 142 | 143 | 143 |
| 533 | 534 | 534 |
| 803 | 804 | 804 |

### Group 117 — 4 occurrences

Key: `{"age": "61", "sex": "1", "cp": "3", "trestbps": "134", "chol": "234", "fbs": "0", "restecg": "1", "thalach": "145", "exang": "0", "oldpeak": "2.6", "slope": "1", "ca": "2", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 143 | 144 | 144 |
| 624 | 625 | 625 |
| 795 | 796 | 796 |
| 901 | 902 | 902 |

### Group 118 — 3 occurrences

Key: `{"age": "34", "sex": "1", "cp": "3", "trestbps": "118", "chol": "182", "fbs": "0", "restecg": "0", "thalach": "174", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 144 | 145 | 145 |
| 202 | 203 | 203 |
| 573 | 574 | 574 |

### Group 119 — 3 occurrences

Key: `{"age": "47", "sex": "1", "cp": "0", "trestbps": "112", "chol": "204", "fbs": "0", "restecg": "1", "thalach": "143", "exang": "0", "oldpeak": "0.1", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 145 | 146 | 146 |
| 663 | 664 | 664 |
| 1020 | 1021 | 1021 |

### Group 120 — 4 occurrences

Key: `{"age": "40", "sex": "1", "cp": "0", "trestbps": "110", "chol": "167", "fbs": "0", "restecg": "0", "thalach": "114", "exang": "1", "oldpeak": "2", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 146 | 147 | 147 |
| 187 | 188 | 188 |
| 398 | 399 | 399 |
| 811 | 812 | 812 |

### Group 121 — 3 occurrences

Key: `{"age": "51", "sex": "0", "cp": "2", "trestbps": "120", "chol": "295", "fbs": "0", "restecg": "0", "thalach": "157", "exang": "0", "oldpeak": "0.6", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 147 | 148 | 148 |
| 449 | 450 | 450 |
| 549 | 550 | 550 |

### Group 122 — 3 occurrences

Key: `{"age": "41", "sex": "1", "cp": "0", "trestbps": "110", "chol": "172", "fbs": "0", "restecg": "0", "thalach": "158", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 148 | 149 | 149 |
| 487 | 488 | 488 |
| 1019 | 1020 | 1020 |

### Group 123 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "3", "trestbps": "152", "chol": "298", "fbs": "1", "restecg": "1", "thalach": "178", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 149 | 150 | 150 |
| 203 | 204 | 204 |
| 577 | 578 | 578 |

### Group 124 — 3 occurrences

Key: `{"age": "39", "sex": "1", "cp": "2", "trestbps": "140", "chol": "321", "fbs": "0", "restecg": "0", "thalach": "182", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 150 | 151 | 151 |
| 479 | 480 | 480 |
| 872 | 873 | 873 |

### Group 125 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "1", "trestbps": "192", "chol": "283", "fbs": "0", "restecg": "0", "thalach": "195", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 152 | 153 | 153 |
| 247 | 248 | 248 |
| 327 | 328 | 328 |

### Group 126 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "125", "chol": "300", "fbs": "0", "restecg": "0", "thalach": "171", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 153 | 154 | 154 |
| 231 | 232 | 232 |
| 688 | 689 | 689 |
| 739 | 740 | 740 |

### Group 127 — 4 occurrences

Key: `{"age": "63", "sex": "1", "cp": "0", "trestbps": "130", "chol": "330", "fbs": "1", "restecg": "0", "thalach": "132", "exang": "1", "oldpeak": "1.8", "slope": "2", "ca": "3", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 155 | 156 | 156 |
| 395 | 396 | 396 |
| 675 | 676 | 676 |
| 743 | 744 | 744 |

### Group 128 — 3 occurrences

Key: `{"age": "40", "sex": "1", "cp": "3", "trestbps": "140", "chol": "199", "fbs": "0", "restecg": "1", "thalach": "178", "exang": "1", "oldpeak": "1.4", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 157 | 158 | 158 |
| 315 | 316 | 316 |
| 586 | 587 | 587 |

### Group 129 — 3 occurrences

Key: `{"age": "67", "sex": "0", "cp": "2", "trestbps": "115", "chol": "564", "fbs": "0", "restecg": "0", "thalach": "160", "exang": "0", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 159 | 160 | 160 |
| 193 | 194 | 194 |
| 465 | 466 | 466 |

### Group 130 — 4 occurrences

Key: `{"age": "41", "sex": "1", "cp": "1", "trestbps": "120", "chol": "157", "fbs": "0", "restecg": "1", "thalach": "182", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 160 | 161 | 161 |
| 218 | 219 | 219 |
| 345 | 346 | 346 |
| 652 | 653 | 653 |

### Group 131 — 3 occurrences

Key: `{"age": "77", "sex": "1", "cp": "0", "trestbps": "125", "chol": "304", "fbs": "0", "restecg": "0", "thalach": "162", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "3", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 161 | 162 | 162 |
| 163 | 164 | 164 |
| 388 | 389 | 389 |

### Group 132 — 4 occurrences

Key: `{"age": "51", "sex": "1", "cp": "2", "trestbps": "100", "chol": "222", "fbs": "0", "restecg": "1", "thalach": "143", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 162 | 163 | 163 |
| 746 | 747 | 747 |
| 776 | 777 | 777 |
| 831 | 832 | 832 |

### Group 133 — 3 occurrences

Key: `{"age": "48", "sex": "1", "cp": "0", "trestbps": "124", "chol": "274", "fbs": "0", "restecg": "0", "thalach": "166", "exang": "0", "oldpeak": "0.5", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 164 | 165 | 165 |
| 727 | 728 | 728 |
| 884 | 885 | 885 |

### Group 134 — 3 occurrences

Key: `{"age": "56", "sex": "1", "cp": "0", "trestbps": "132", "chol": "184", "fbs": "0", "restecg": "0", "thalach": "105", "exang": "1", "oldpeak": "2.1", "slope": "1", "ca": "1", "thal": "1"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 167 | 168 | 168 |
| 565 | 566 | 566 |
| 846 | 847 | 847 |

### Group 135 — 3 occurrences

Key: `{"age": "57", "sex": "0", "cp": "0", "trestbps": "120", "chol": "354", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "1", "oldpeak": "0.6", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 168 | 169 | 169 |
| 423 | 424 | 424 |
| 436 | 437 | 437 |

### Group 136 — 3 occurrences

Key: `{"age": "43", "sex": "1", "cp": "2", "trestbps": "130", "chol": "315", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "1.9", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 169 | 170 | 170 |
| 214 | 215 | 215 |
| 937 | 938 | 938 |

### Group 137 — 3 occurrences

Key: `{"age": "45", "sex": "0", "cp": "1", "trestbps": "112", "chol": "160", "fbs": "0", "restecg": "1", "thalach": "138", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 170 | 171 | 171 |
| 252 | 253 | 253 |
| 713 | 714 | 714 |

### Group 138 — 3 occurrences

Key: `{"age": "43", "sex": "1", "cp": "0", "trestbps": "150", "chol": "247", "fbs": "0", "restecg": "1", "thalach": "171", "exang": "0", "oldpeak": "1.5", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 171 | 172 | 172 |
| 459 | 460 | 460 |
| 576 | 577 | 577 |

### Group 139 — 4 occurrences

Key: `{"age": "56", "sex": "1", "cp": "0", "trestbps": "130", "chol": "283", "fbs": "1", "restecg": "0", "thalach": "103", "exang": "1", "oldpeak": "1.6", "slope": "0", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 172 | 173 | 173 |
| 177 | 178 | 178 |
| 276 | 277 | 277 |
| 654 | 655 | 655 |

### Group 140 — 4 occurrences

Key: `{"age": "56", "sex": "1", "cp": "1", "trestbps": "120", "chol": "240", "fbs": "0", "restecg": "1", "thalach": "169", "exang": "0", "oldpeak": "0", "slope": "0", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 173 | 174 | 174 |
| 784 | 785 | 785 |
| 869 | 870 | 870 |
| 936 | 937 | 937 |

### Group 141 — 3 occurrences

Key: `{"age": "39", "sex": "0", "cp": "2", "trestbps": "94", "chol": "199", "fbs": "0", "restecg": "1", "thalach": "179", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 174 | 175 | 175 |
| 224 | 225 | 225 |
| 559 | 560 | 560 |

### Group 142 — 4 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "110", "chol": "239", "fbs": "0", "restecg": "1", "thalach": "126", "exang": "1", "oldpeak": "2.8", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 175 | 176 | 176 |
| 791 | 792 | 792 |
| 792 | 793 | 793 |
| 893 | 894 | 894 |

### Group 143 — 4 occurrences

Key: `{"age": "56", "sex": "0", "cp": "0", "trestbps": "200", "chol": "288", "fbs": "1", "restecg": "0", "thalach": "133", "exang": "1", "oldpeak": "4", "slope": "0", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 176 | 177 | 177 |
| 295 | 296 | 296 |
| 509 | 510 | 510 |
| 689 | 690 | 690 |

### Group 144 — 4 occurrences

Key: `{"age": "64", "sex": "1", "cp": "0", "trestbps": "120", "chol": "246", "fbs": "0", "restecg": "0", "thalach": "96", "exang": "1", "oldpeak": "2.2", "slope": "0", "ca": "1", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 178 | 179 | 179 |
| 389 | 390 | 390 |
| 757 | 758 | 758 |
| 906 | 907 | 907 |

### Group 145 — 3 occurrences

Key: `{"age": "56", "sex": "0", "cp": "0", "trestbps": "134", "chol": "409", "fbs": "0", "restecg": "0", "thalach": "150", "exang": "1", "oldpeak": "1.9", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 180 | 181 | 181 |
| 642 | 643 | 643 |
| 997 | 998 | 998 |

### Group 146 — 3 occurrences

Key: `{"age": "64", "sex": "1", "cp": "3", "trestbps": "110", "chol": "211", "fbs": "0", "restecg": "0", "thalach": "144", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 182 | 183 | 183 |
| 223 | 224 | 224 |
| 284 | 285 | 285 |

### Group 147 — 4 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "140", "chol": "293", "fbs": "0", "restecg": "0", "thalach": "170", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 183 | 184 | 184 |
| 442 | 443 | 443 |
| 845 | 846 | 846 |
| 989 | 990 | 990 |

### Group 148 — 4 occurrences

Key: `{"age": "42", "sex": "1", "cp": "2", "trestbps": "130", "chol": "180", "fbs": "0", "restecg": "1", "thalach": "150", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 184 | 185 | 185 |
| 250 | 251 | 251 |
| 827 | 828 | 828 |
| 935 | 936 | 936 |

### Group 149 — 3 occurrences

Key: `{"age": "45", "sex": "1", "cp": "1", "trestbps": "128", "chol": "308", "fbs": "0", "restecg": "0", "thalach": "170", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 185 | 186 | 186 |
| 215 | 216 | 216 |
| 1012 | 1013 | 1013 |

### Group 150 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "165", "chol": "289", "fbs": "1", "restecg": "0", "thalach": "124", "exang": "0", "oldpeak": "1", "slope": "1", "ca": "3", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 186 | 187 | 187 |
| 254 | 255 | 255 |
| 477 | 478 | 478 |
| 886 | 887 | 887 |

### Group 151 — 4 occurrences

Key: `{"age": "64", "sex": "1", "cp": "2", "trestbps": "125", "chol": "309", "fbs": "0", "restecg": "1", "thalach": "131", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 190 | 191 | 191 |
| 493 | 494 | 494 |
| 587 | 588 | 588 |
| 659 | 660 | 660 |

### Group 152 — 3 occurrences

Key: `{"age": "41", "sex": "1", "cp": "2", "trestbps": "112", "chol": "250", "fbs": "0", "restecg": "1", "thalach": "179", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 191 | 192 | 192 |
| 208 | 209 | 209 |
| 867 | 868 | 868 |

### Group 153 — 4 occurrences

Key: `{"age": "56", "sex": "1", "cp": "1", "trestbps": "130", "chol": "221", "fbs": "0", "restecg": "0", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 192 | 193 | 193 |
| 711 | 712 | 712 |
| 728 | 729 | 729 |
| 763 | 764 | 764 |

### Group 154 — 3 occurrences

Key: `{"age": "69", "sex": "1", "cp": "3", "trestbps": "160", "chol": "234", "fbs": "1", "restecg": "0", "thalach": "131", "exang": "0", "oldpeak": "0.1", "slope": "1", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 194 | 195 | 195 |
| 456 | 457 | 457 |
| 530 | 531 | 531 |

### Group 155 — 4 occurrences

Key: `{"age": "67", "sex": "1", "cp": "0", "trestbps": "160", "chol": "286", "fbs": "0", "restecg": "0", "thalach": "108", "exang": "1", "oldpeak": "1.5", "slope": "1", "ca": "3", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 195 | 196 | 196 |
| 358 | 359 | 359 |
| 470 | 471 | 471 |
| 951 | 952 | 952 |

### Group 156 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "100", "chol": "234", "fbs": "0", "restecg": "1", "thalach": "156", "exang": "0", "oldpeak": "0.1", "slope": "2", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 197 | 198 | 198 |
| 408 | 409 | 409 |
| 555 | 556 | 556 |
| 676 | 677 | 677 |

### Group 157 — 3 occurrences

Key: `{"age": "45", "sex": "1", "cp": "0", "trestbps": "115", "chol": "260", "fbs": "0", "restecg": "0", "thalach": "185", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 198 | 199 | 199 |
| 722 | 723 | 723 |
| 818 | 819 | 819 |

### Group 158 — 3 occurrences

Key: `{"age": "60", "sex": "0", "cp": "2", "trestbps": "102", "chol": "318", "fbs": "0", "restecg": "1", "thalach": "160", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 199 | 200 | 200 |
| 433 | 434 | 434 |
| 745 | 746 | 746 |

### Group 159 — 3 occurrences

Key: `{"age": "50", "sex": "1", "cp": "0", "trestbps": "144", "chol": "200", "fbs": "0", "restecg": "0", "thalach": "126", "exang": "1", "oldpeak": "0.9", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 200 | 201 | 201 |
| 352 | 353 | 353 |
| 910 | 911 | 911 |

### Group 160 — 4 occurrences

Key: `{"age": "64", "sex": "1", "cp": "3", "trestbps": "170", "chol": "227", "fbs": "0", "restecg": "0", "thalach": "155", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 204 | 205 | 205 |
| 236 | 237 | 237 |
| 540 | 541 | 541 |
| 873 | 874 | 874 |

### Group 161 — 3 occurrences

Key: `{"age": "42", "sex": "1", "cp": "3", "trestbps": "148", "chol": "244", "fbs": "0", "restecg": "0", "thalach": "178", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "2", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 206 | 207 | 207 |
| 316 | 317 | 317 |
| 819 | 820 | 820 |

### Group 162 — 3 occurrences

Key: `{"age": "42", "sex": "1", "cp": "2", "trestbps": "120", "chol": "240", "fbs": "1", "restecg": "1", "thalach": "194", "exang": "0", "oldpeak": "0.8", "slope": "0", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 211 | 212 | 212 |
| 570 | 571 | 571 |
| 928 | 929 | 929 |

### Group 163 — 3 occurrences

Key: `{"age": "50", "sex": "1", "cp": "0", "trestbps": "150", "chol": "243", "fbs": "0", "restecg": "0", "thalach": "128", "exang": "0", "oldpeak": "2.6", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 213 | 214 | 214 |
| 347 | 348 | 348 |
| 646 | 647 | 647 |

### Group 164 — 3 occurrences

Key: `{"age": "49", "sex": "1", "cp": "1", "trestbps": "130", "chol": "266", "fbs": "0", "restecg": "1", "thalach": "171", "exang": "0", "oldpeak": "0.6", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 216 | 217 | 217 |
| 619 | 620 | 620 |
| 632 | 633 | 633 |

### Group 165 — 4 occurrences

Key: `{"age": "65", "sex": "1", "cp": "0", "trestbps": "135", "chol": "254", "fbs": "0", "restecg": "0", "thalach": "127", "exang": "0", "oldpeak": "2.8", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 217 | 218 | 218 |
| 488 | 489 | 489 |
| 917 | 918 | 918 |
| 931 | 932 | 932 |

### Group 166 — 4 occurrences

Key: `{"age": "46", "sex": "1", "cp": "0", "trestbps": "140", "chol": "311", "fbs": "0", "restecg": "1", "thalach": "120", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 219 | 220 | 220 |
| 248 | 249 | 249 |
| 602 | 603 | 603 |
| 729 | 730 | 730 |

### Group 167 — 3 occurrences

Key: `{"age": "57", "sex": "0", "cp": "1", "trestbps": "130", "chol": "236", "fbs": "0", "restecg": "0", "thalach": "174", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "1", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 221 | 222 | 222 |
| 365 | 366 | 366 |
| 657 | 658 | 658 |

### Group 168 — 3 occurrences

Key: `{"age": "51", "sex": "1", "cp": "0", "trestbps": "140", "chol": "261", "fbs": "0", "restecg": "0", "thalach": "186", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 225 | 226 | 226 |
| 460 | 461 | 461 |
| 840 | 841 | 841 |

### Group 169 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "2", "trestbps": "150", "chol": "232", "fbs": "0", "restecg": "0", "thalach": "165", "exang": "0", "oldpeak": "1.6", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 226 | 227 | 227 |
| 262 | 263 | 263 |
| 785 | 786 | 786 |

### Group 170 — 3 occurrences

Key: `{"age": "44", "sex": "0", "cp": "2", "trestbps": "118", "chol": "242", "fbs": "0", "restecg": "1", "thalach": "149", "exang": "0", "oldpeak": "0.3", "slope": "1", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 228 | 229 | 229 |
| 307 | 308 | 308 |
| 506 | 507 | 507 |

### Group 171 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "1", "trestbps": "128", "chol": "205", "fbs": "1", "restecg": "1", "thalach": "184", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 229 | 230 | 230 |
| 446 | 447 | 447 |
| 978 | 979 | 979 |

### Group 172 — 3 occurrences

Key: `{"age": "56", "sex": "1", "cp": "1", "trestbps": "120", "chol": "236", "fbs": "0", "restecg": "1", "thalach": "178", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 232 | 233 | 233 |
| 870 | 871 | 871 |
| 991 | 992 | 992 |

### Group 173 — 3 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "125", "chol": "258", "fbs": "0", "restecg": "0", "thalach": "141", "exang": "1", "oldpeak": "2.8", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 233 | 234 | 234 |
| 575 | 576 | 576 |
| 1022 | 1023 | 1023 |

### Group 174 — 3 occurrences

Key: `{"age": "41", "sex": "0", "cp": "1", "trestbps": "126", "chol": "306", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 234 | 235 | 235 |
| 618 | 619 | 619 |
| 655 | 656 | 656 |

### Group 175 — 3 occurrences

Key: `{"age": "49", "sex": "0", "cp": "0", "trestbps": "130", "chol": "269", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 235 | 236 | 236 |
| 762 | 763 | 763 |
| 957 | 958 | 958 |

### Group 176 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "1", "trestbps": "124", "chol": "261", "fbs": "0", "restecg": "1", "thalach": "141", "exang": "0", "oldpeak": "0.3", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 238 | 239 | 239 |
| 355 | 356 | 356 |
| 668 | 669 | 669 |
| 812 | 813 | 813 |

### Group 177 — 3 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "150", "chol": "244", "fbs": "0", "restecg": "1", "thalach": "154", "exang": "1", "oldpeak": "1.4", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 240 | 241 | 241 |
| 441 | 442 | 442 |
| 773 | 774 | 774 |

### Group 178 — 3 occurrences

Key: `{"age": "54", "sex": "0", "cp": "1", "trestbps": "132", "chol": "288", "fbs": "1", "restecg": "0", "thalach": "159", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 241 | 242 | 242 |
| 489 | 490 | 490 |
| 511 | 512 | 512 |

### Group 179 — 3 occurrences

Key: `{"age": "51", "sex": "1", "cp": "2", "trestbps": "125", "chol": "245", "fbs": "1", "restecg": "0", "thalach": "166", "exang": "0", "oldpeak": "2.4", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 245 | 246 | 246 |
| 495 | 496 | 496 |
| 974 | 975 | 975 |

### Group 180 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "1", "trestbps": "130", "chol": "219", "fbs": "0", "restecg": "0", "thalach": "188", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 246 | 247 | 247 |
| 278 | 279 | 279 |
| 467 | 468 | 468 |

### Group 181 — 4 occurrences

Key: `{"age": "39", "sex": "0", "cp": "2", "trestbps": "138", "chol": "220", "fbs": "0", "restecg": "1", "thalach": "152", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 249 | 250 | 250 |
| 273 | 274 | 274 |
| 458 | 459 | 459 |
| 658 | 659 | 659 |

### Group 182 — 4 occurrences

Key: `{"age": "55", "sex": "1", "cp": "0", "trestbps": "132", "chol": "353", "fbs": "0", "restecg": "1", "thalach": "132", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 253 | 254 | 254 |
| 372 | 373 | 373 |
| 494 | 495 | 495 |
| 585 | 586 | 586 |

### Group 183 — 4 occurrences

Key: `{"age": "35", "sex": "1", "cp": "0", "trestbps": "120", "chol": "198", "fbs": "0", "restecg": "1", "thalach": "130", "exang": "1", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 255 | 256 | 256 |
| 702 | 703 | 703 |
| 712 | 713 | 713 |
| 913 | 914 | 914 |

### Group 184 — 3 occurrences

Key: `{"age": "62", "sex": "0", "cp": "0", "trestbps": "140", "chol": "394", "fbs": "0", "restecg": "0", "thalach": "157", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 256 | 257 | 257 |
| 543 | 544 | 544 |
| 579 | 580 | 580 |

### Group 185 — 4 occurrences

Key: `{"age": "35", "sex": "0", "cp": "0", "trestbps": "138", "chol": "183", "fbs": "0", "restecg": "1", "thalach": "182", "exang": "0", "oldpeak": "1.4", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 257 | 258 | 258 |
| 502 | 503 | 503 |
| 842 | 843 | 843 |
| 847 | 848 | 848 |

### Group 186 — 4 occurrences

Key: `{"age": "38", "sex": "1", "cp": "3", "trestbps": "120", "chol": "231", "fbs": "0", "restecg": "1", "thalach": "182", "exang": "1", "oldpeak": "3.8", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 259 | 260 | 260 |
| 628 | 629 | 629 |
| 920 | 921 | 921 |
| 934 | 935 | 935 |

### Group 187 — 4 occurrences

Key: `{"age": "44", "sex": "1", "cp": "2", "trestbps": "120", "chol": "226", "fbs": "0", "restecg": "1", "thalach": "169", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 261 | 262 | 262 |
| 342 | 343 | 343 |
| 645 | 646 | 646 |
| 749 | 750 | 750 |

### Group 188 — 3 occurrences

Key: `{"age": "48", "sex": "1", "cp": "0", "trestbps": "122", "chol": "222", "fbs": "0", "restecg": "0", "thalach": "186", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 263 | 264 | 264 |
| 361 | 362 | 362 |
| 558 | 559 | 559 |

### Group 189 — 4 occurrences

Key: `{"age": "67", "sex": "1", "cp": "0", "trestbps": "120", "chol": "237", "fbs": "0", "restecg": "1", "thalach": "71", "exang": "0", "oldpeak": "1", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 268 | 269 | 269 |
| 297 | 298 | 298 |
| 379 | 380 | 380 |
| 560 | 561 | 561 |

### Group 190 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "2", "trestbps": "132", "chol": "224", "fbs": "0", "restecg": "0", "thalach": "173", "exang": "0", "oldpeak": "3.2", "slope": "2", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 269 | 270 | 270 |
| 285 | 286 | 286 |
| 382 | 383 | 383 |
| 627 | 628 | 628 |

### Group 191 — 4 occurrences

Key: `{"age": "71", "sex": "0", "cp": "2", "trestbps": "110", "chol": "265", "fbs": "1", "restecg": "0", "thalach": "130", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 270 | 271 | 271 |
| 286 | 287 | 287 |
| 606 | 607 | 607 |
| 770 | 771 | 771 |

### Group 192 — 3 occurrences

Key: `{"age": "43", "sex": "1", "cp": "0", "trestbps": "110", "chol": "211", "fbs": "0", "restecg": "1", "thalach": "161", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 271 | 272 | 272 |
| 464 | 465 | 465 |
| 975 | 976 | 976 |

### Group 193 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "1", "trestbps": "120", "chol": "263", "fbs": "0", "restecg": "1", "thalach": "173", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 272 | 273 | 273 |
| 923 | 924 | 924 |
| 996 | 997 | 997 |

### Group 194 — 4 occurrences

Key: `{"age": "66", "sex": "1", "cp": "0", "trestbps": "160", "chol": "228", "fbs": "0", "restecg": "0", "thalach": "138", "exang": "0", "oldpeak": "2.3", "slope": "2", "ca": "0", "thal": "1"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 275 | 276 | 276 |
| 376 | 377 | 377 |
| 399 | 400 | 400 |
| 758 | 759 | 759 |

### Group 195 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "132", "chol": "207", "fbs": "0", "restecg": "1", "thalach": "168", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 277 | 278 | 278 |
| 881 | 882 | 882 |
| 950 | 951 | 951 |

### Group 196 — 3 occurrences

Key: `{"age": "41", "sex": "0", "cp": "1", "trestbps": "105", "chol": "198", "fbs": "0", "restecg": "1", "thalach": "168", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 280 | 281 | 281 |
| 411 | 412 | 412 |
| 518 | 519 | 519 |

### Group 197 — 4 occurrences

Key: `{"age": "45", "sex": "0", "cp": "1", "trestbps": "130", "chol": "234", "fbs": "0", "restecg": "0", "thalach": "175", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 281 | 282 | 282 |
| 504 | 505 | 505 |
| 633 | 634 | 634 |
| 650 | 651 | 651 |

### Group 198 — 4 occurrences

Key: `{"age": "35", "sex": "1", "cp": "1", "trestbps": "122", "chol": "192", "fbs": "0", "restecg": "1", "thalach": "174", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 282 | 283 | 283 |
| 299 | 300 | 300 |
| 484 | 485 | 485 |
| 667 | 668 | 668 |

### Group 199 — 3 occurrences

Key: `{"age": "41", "sex": "0", "cp": "1", "trestbps": "130", "chol": "204", "fbs": "0", "restecg": "0", "thalach": "172", "exang": "0", "oldpeak": "1.4", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 283 | 284 | 284 |
| 416 | 417 | 417 |
| 508 | 509 | 509 |

### Group 200 — 3 occurrences

Key: `{"age": "64", "sex": "0", "cp": "2", "trestbps": "140", "chol": "313", "fbs": "0", "restecg": "1", "thalach": "133", "exang": "0", "oldpeak": "0.2", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 287 | 288 | 288 |
| 317 | 318 | 318 |
| 472 | 473 | 473 |

### Group 201 — 3 occurrences

Key: `{"age": "71", "sex": "0", "cp": "1", "trestbps": "160", "chol": "302", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "0.4", "slope": "2", "ca": "2", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 288 | 289 | 289 |
| 703 | 704 | 704 |
| 990 | 991 | 991 |

### Group 202 — 3 occurrences

Key: `{"age": "58", "sex": "0", "cp": "2", "trestbps": "120", "chol": "340", "fbs": "0", "restecg": "1", "thalach": "172", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 289 | 290 | 290 |
| 603 | 604 | 604 |
| 638 | 639 | 639 |

### Group 203 — 3 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "128", "chol": "259", "fbs": "0", "restecg": "0", "thalach": "130", "exang": "1", "oldpeak": "3", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 292 | 293 | 293 |
| 541 | 542 | 542 |
| 967 | 968 | 968 |

### Group 204 — 3 occurrences

Key: `{"age": "61", "sex": "1", "cp": "2", "trestbps": "150", "chol": "243", "fbs": "1", "restecg": "1", "thalach": "137", "exang": "1", "oldpeak": "1", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 293 | 294 | 294 |
| 469 | 470 | 470 |
| 490 | 491 | 491 |

### Group 205 — 3 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "150", "chol": "270", "fbs": "0", "restecg": "0", "thalach": "111", "exang": "1", "oldpeak": "0.8", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 298 | 299 | 299 |
| 336 | 337 | 337 |
| 384 | 385 | 385 |

### Group 206 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "1", "trestbps": "120", "chol": "325", "fbs": "0", "restecg": "1", "thalach": "172", "exang": "0", "oldpeak": "0.2", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 300 | 301 | 301 |
| 538 | 539 | 539 |
| 970 | 971 | 971 |

### Group 207 — 3 occurrences

Key: `{"age": "46", "sex": "0", "cp": "1", "trestbps": "105", "chol": "204", "fbs": "0", "restecg": "1", "thalach": "172", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 301 | 302 | 302 |
| 404 | 405 | 405 |
| 759 | 760 | 760 |

### Group 208 — 4 occurrences

Key: `{"age": "51", "sex": "1", "cp": "2", "trestbps": "94", "chol": "227", "fbs": "0", "restecg": "1", "thalach": "154", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "3"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 302 | 303 | 303 |
| 705 | 706 | 706 |
| 733 | 734 | 734 |
| 809 | 810 | 810 |

### Group 209 — 3 occurrences

Key: `{"age": "52", "sex": "0", "cp": "2", "trestbps": "136", "chol": "196", "fbs": "0", "restecg": "0", "thalach": "169", "exang": "0", "oldpeak": "0.1", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 305 | 306 | 306 |
| 942 | 943 | 943 |
| 961 | 962 | 962 |

### Group 210 — 3 occurrences

Key: `{"age": "62", "sex": "1", "cp": "0", "trestbps": "120", "chol": "267", "fbs": "0", "restecg": "1", "thalach": "99", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 306 | 307 | 307 |
| 651 | 652 | 652 |
| 909 | 910 | 910 |

### Group 211 — 3 occurrences

Key: `{"age": "56", "sex": "0", "cp": "1", "trestbps": "140", "chol": "294", "fbs": "0", "restecg": "0", "thalach": "153", "exang": "0", "oldpeak": "1.3", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 310 | 311 | 311 |
| 326 | 327 | 327 |
| 708 | 709 | 709 |

### Group 212 — 3 occurrences

Key: `{"age": "74", "sex": "0", "cp": "1", "trestbps": "120", "chol": "269", "fbs": "0", "restecg": "0", "thalach": "121", "exang": "1", "oldpeak": "0.2", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 314 | 315 | 315 |
| 591 | 592 | 592 |
| 725 | 726 | 726 |

### Group 213 — 3 occurrences

Key: `{"age": "53", "sex": "0", "cp": "2", "trestbps": "128", "chol": "216", "fbs": "0", "restecg": "0", "thalach": "115", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "0"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 320 | 321 | 321 |
| 330 | 331 | 331 |
| 360 | 361 | 361 |

### Group 214 — 3 occurrences

Key: `{"age": "53", "sex": "0", "cp": "0", "trestbps": "130", "chol": "264", "fbs": "0", "restecg": "0", "thalach": "143", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 321 | 322 | 322 |
| 636 | 637 | 637 |
| 955 | 956 | 956 |

### Group 215 — 3 occurrences

Key: `{"age": "48", "sex": "0", "cp": "2", "trestbps": "130", "chol": "275", "fbs": "0", "restecg": "1", "thalach": "139", "exang": "0", "oldpeak": "0.2", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 322 | 323 | 323 |
| 775 | 776 | 776 |
| 871 | 872 | 872 |

### Group 216 — 3 occurrences

Key: `{"age": "45", "sex": "1", "cp": "0", "trestbps": "142", "chol": "309", "fbs": "0", "restecg": "0", "thalach": "147", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "3", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 323 | 324 | 324 |
| 425 | 426 | 426 |
| 980 | 981 | 981 |

### Group 217 — 3 occurrences

Key: `{"age": "66", "sex": "1", "cp": "1", "trestbps": "160", "chol": "246", "fbs": "0", "restecg": "1", "thalach": "120", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "3", "thal": "1"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 324 | 325 | 325 |
| 346 | 347 | 347 |
| 670 | 671 | 671 |

### Group 218 — 4 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "150", "chol": "276", "fbs": "0", "restecg": "0", "thalach": "112", "exang": "1", "oldpeak": "0.6", "slope": "1", "ca": "1", "thal": "1"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 328 | 329 | 329 |
| 413 | 414 | 414 |
| 761 | 762 | 762 |
| 807 | 808 | 808 |

### Group 219 — 4 occurrences

Key: `{"age": "70", "sex": "1", "cp": "0", "trestbps": "130", "chol": "322", "fbs": "0", "restecg": "0", "thalach": "109", "exang": "0", "oldpeak": "2.4", "slope": "1", "ca": "3", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 329 | 330 | 330 |
| 414 | 415 | 415 |
| 547 | 548 | 548 |
| 578 | 579 | 579 |

### Group 220 — 4 occurrences

Key: `{"age": "63", "sex": "0", "cp": "0", "trestbps": "108", "chol": "269", "fbs": "0", "restecg": "1", "thalach": "169", "exang": "1", "oldpeak": "1.8", "slope": "1", "ca": "2", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 332 | 333 | 333 |
| 592 | 593 | 593 |
| 594 | 595 | 595 |
| 977 | 978 | 978 |

### Group 221 — 3 occurrences

Key: `{"age": "37", "sex": "1", "cp": "2", "trestbps": "130", "chol": "250", "fbs": "0", "restecg": "1", "thalach": "187", "exang": "0", "oldpeak": "3.5", "slope": "0", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 333 | 334 | 334 |
| 434 | 435 | 435 |
| 852 | 853 | 853 |

### Group 222 — 3 occurrences

Key: `{"age": "54", "sex": "0", "cp": "2", "trestbps": "110", "chol": "214", "fbs": "0", "restecg": "1", "thalach": "158", "exang": "0", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 334 | 335 | 335 |
| 373 | 374 | 374 |
| 810 | 811 | 811 |

### Group 223 — 4 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "130", "chol": "206", "fbs": "0", "restecg": "0", "thalach": "132", "exang": "1", "oldpeak": "2.4", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 335 | 336 | 336 |
| 517 | 518 | 518 |
| 876 | 877 | 877 |
| 930 | 931 | 931 |

### Group 224 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "2", "trestbps": "125", "chol": "273", "fbs": "0", "restecg": "0", "thalach": "152", "exang": "0", "oldpeak": "0.5", "slope": "0", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 338 | 339 | 339 |
| 417 | 418 | 418 |
| 545 | 546 | 546 |

### Group 225 — 3 occurrences

Key: `{"age": "60", "sex": "1", "cp": "0", "trestbps": "130", "chol": "253", "fbs": "0", "restecg": "1", "thalach": "144", "exang": "1", "oldpeak": "1.4", "slope": "2", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 340 | 341 | 341 |
| 677 | 678 | 678 |
| 823 | 824 | 824 |

### Group 226 — 3 occurrences

Key: `{"age": "65", "sex": "0", "cp": "2", "trestbps": "155", "chol": "269", "fbs": "0", "restecg": "1", "thalach": "148", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 343 | 344 | 344 |
| 532 | 533 | 533 |
| 562 | 563 | 563 |

### Group 227 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "2", "trestbps": "172", "chol": "199", "fbs": "1", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "0.5", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 344 | 345 | 345 |
| 838 | 839 | 839 |
| 972 | 973 | 973 |

### Group 228 — 3 occurrences

Key: `{"age": "43", "sex": "1", "cp": "0", "trestbps": "132", "chol": "247", "fbs": "1", "restecg": "0", "thalach": "143", "exang": "1", "oldpeak": "0.1", "slope": "1", "ca": "4", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 349 | 350 | 350 |
| 429 | 430 | 430 |
| 994 | 995 | 995 |

### Group 229 — 4 occurrences

Key: `{"age": "62", "sex": "0", "cp": "2", "trestbps": "130", "chol": "263", "fbs": "0", "restecg": "1", "thalach": "97", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 350 | 351 | 351 |
| 601 | 602 | 602 |
| 896 | 897 | 897 |
| 952 | 953 | 953 |

### Group 230 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "0", "trestbps": "110", "chol": "201", "fbs": "0", "restecg": "1", "thalach": "126", "exang": "1", "oldpeak": "1.5", "slope": "1", "ca": "0", "thal": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 354 | 355 | 355 |
| 704 | 705 | 705 |
| 888 | 889 | 889 |

### Group 231 — 3 occurrences

Key: `{"age": "46", "sex": "0", "cp": "0", "trestbps": "138", "chol": "243", "fbs": "0", "restecg": "0", "thalach": "152", "exang": "1", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 356 | 357 | 357 |
| 409 | 410 | 410 |
| 641 | 642 | 642 |

### Group 232 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "164", "chol": "176", "fbs": "1", "restecg": "0", "thalach": "90", "exang": "0", "oldpeak": "1", "slope": "1", "ca": "2", "thal": "1"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 357 | 358 | 358 |
| 588 | 589 | 589 |
| 683 | 684 | 684 |

### Group 233 — 4 occurrences

Key: `{"age": "59", "sex": "1", "cp": "3", "trestbps": "134", "chol": "204", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "0.8", "slope": "2", "ca": "2", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 359 | 360 | 360 |
| 544 | 545 | 545 |
| 779 | 780 | 780 |
| 919 | 920 | 920 |

### Group 234 — 3 occurrences

Key: `{"age": "62", "sex": "1", "cp": "2", "trestbps": "130", "chol": "231", "fbs": "0", "restecg": "1", "thalach": "146", "exang": "0", "oldpeak": "1.8", "slope": "1", "ca": "3", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 362 | 363 | 363 |
| 956 | 957 | 957 |
| 986 | 987 | 987 |

### Group 235 — 3 occurrences

Key: `{"age": "53", "sex": "1", "cp": "2", "trestbps": "130", "chol": "246", "fbs": "1", "restecg": "0", "thalach": "173", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "3", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 364 | 365 | 365 |
| 366 | 367 | 367 |
| 447 | 448 | 448 |

### Group 236 — 3 occurrences

Key: `{"age": "58", "sex": "1", "cp": "2", "trestbps": "112", "chol": "230", "fbs": "0", "restecg": "0", "thalach": "165", "exang": "0", "oldpeak": "2.5", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 367 | 368 | 368 |
| 525 | 526 | 526 |
| 843 | 844 | 844 |

### Group 237 — 4 occurrences

Key: `{"age": "48", "sex": "1", "cp": "1", "trestbps": "110", "chol": "229", "fbs": "0", "restecg": "1", "thalach": "168", "exang": "0", "oldpeak": "1", "slope": "0", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 368 | 369 | 369 |
| 475 | 476 | 476 |
| 546 | 547 | 547 |
| 1013 | 1014 | 1014 |

### Group 238 — 3 occurrences

Key: `{"age": "58", "sex": "1", "cp": "2", "trestbps": "105", "chol": "240", "fbs": "0", "restecg": "0", "thalach": "154", "exang": "1", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 369 | 370 | 370 |
| 691 | 692 | 692 |
| 816 | 817 | 817 |

### Group 239 — 3 occurrences

Key: `{"age": "51", "sex": "1", "cp": "2", "trestbps": "110", "chol": "175", "fbs": "0", "restecg": "1", "thalach": "123", "exang": "0", "oldpeak": "0.6", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 370 | 371 | 371 |
| 386 | 387 | 387 |
| 393 | 394 | 394 |

### Group 240 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "1", "trestbps": "120", "chol": "284", "fbs": "0", "restecg": "0", "thalach": "160", "exang": "0", "oldpeak": "1.8", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 374 | 375 | 375 |
| 440 | 441 | 441 |
| 599 | 600 | 600 |
| 851 | 852 | 852 |

### Group 241 — 3 occurrences

Key: `{"age": "46", "sex": "0", "cp": "2", "trestbps": "142", "chol": "177", "fbs": "0", "restecg": "0", "thalach": "160", "exang": "1", "oldpeak": "1.4", "slope": "0", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 375 | 376 | 376 |
| 500 | 501 | 501 |
| 503 | 504 | 504 |

### Group 242 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "1", "trestbps": "140", "chol": "221", "fbs": "0", "restecg": "1", "thalach": "164", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 377 | 378 | 378 |
| 597 | 598 | 598 |
| 1021 | 1022 | 1022 |

### Group 243 — 3 occurrences

Key: `{"age": "64", "sex": "0", "cp": "0", "trestbps": "130", "chol": "303", "fbs": "0", "restecg": "1", "thalach": "122", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "2", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 378 | 379 | 379 |
| 648 | 649 | 649 |
| 783 | 784 | 784 |

### Group 244 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "146", "chol": "218", "fbs": "0", "restecg": "1", "thalach": "105", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 381 | 382 | 382 |
| 580 | 581 | 581 |
| 782 | 783 | 783 |
| 922 | 923 | 923 |

### Group 245 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "110", "chol": "239", "fbs": "0", "restecg": "0", "thalach": "142", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 383 | 384 | 384 |
| 737 | 738 | 738 |
| 995 | 996 | 996 |

### Group 246 — 3 occurrences

Key: `{"age": "35", "sex": "1", "cp": "0", "trestbps": "126", "chol": "282", "fbs": "0", "restecg": "0", "thalach": "156", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 385 | 386 | 386 |
| 696 | 697 | 697 |
| 700 | 701 | 701 |

### Group 247 — 3 occurrences

Key: `{"age": "63", "sex": "1", "cp": "3", "trestbps": "145", "chol": "233", "fbs": "1", "restecg": "0", "thalach": "150", "exang": "0", "oldpeak": "2.3", "slope": "0", "ca": "0", "thal": "1"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 390 | 391 | 391 |
| 400 | 401 | 401 |
| 802 | 803 | 803 |

### Group 248 — 3 occurrences

Key: `{"age": "45", "sex": "1", "cp": "3", "trestbps": "110", "chol": "264", "fbs": "0", "restecg": "1", "thalach": "132", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 392 | 393 | 393 |
| 631 | 632 | 632 |
| 710 | 711 | 711 |

### Group 249 — 3 occurrences

Key: `{"age": "68", "sex": "1", "cp": "2", "trestbps": "180", "chol": "274", "fbs": "1", "restecg": "0", "thalach": "150", "exang": "1", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 397 | 398 | 398 |
| 497 | 498 | 498 |
| 680 | 681 | 681 |

### Group 250 — 3 occurrences

Key: `{"age": "70", "sex": "1", "cp": "1", "trestbps": "156", "chol": "245", "fbs": "0", "restecg": "0", "thalach": "143", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 403 | 404 | 404 |
| 716 | 717 | 717 |
| 817 | 818 | 818 |

### Group 251 — 3 occurrences

Key: `{"age": "42", "sex": "0", "cp": "0", "trestbps": "102", "chol": "265", "fbs": "0", "restecg": "0", "thalach": "122", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 422 | 423 | 423 |
| 899 | 900 | 900 |
| 902 | 903 | 903 |

### Group 252 — 3 occurrences

Key: `{"age": "51", "sex": "0", "cp": "0", "trestbps": "130", "chol": "305", "fbs": "0", "restecg": "1", "thalach": "142", "exang": "1", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 426 | 427 | 427 |
| 481 | 482 | 482 |
| 615 | 616 | 616 |

### Group 253 — 3 occurrences

Key: `{"age": "54", "sex": "0", "cp": "2", "trestbps": "160", "chol": "201", "fbs": "0", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 427 | 428 | 428 |
| 569 | 570 | 570 |
| 948 | 949 | 949 |

### Group 254 — 3 occurrences

Key: `{"age": "57", "sex": "1", "cp": "2", "trestbps": "150", "chol": "168", "fbs": "0", "restecg": "1", "thalach": "174", "exang": "0", "oldpeak": "1.6", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 428 | 429 | 429 |
| 444 | 445 | 445 |
| 492 | 493 | 493 |

### Group 255 — 4 occurrences

Key: `{"age": "47", "sex": "1", "cp": "2", "trestbps": "108", "chol": "243", "fbs": "0", "restecg": "1", "thalach": "152", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 430 | 431 | 431 |
| 457 | 458 | 458 |
| 505 | 506 | 506 |
| 647 | 648 | 648 |

### Group 256 — 4 occurrences

Key: `{"age": "65", "sex": "0", "cp": "0", "trestbps": "150", "chol": "225", "fbs": "0", "restecg": "0", "thalach": "114", "exang": "0", "oldpeak": "1", "slope": "1", "ca": "3", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 432 | 433 | 433 |
| 455 | 456 | 456 |
| 774 | 775 | 775 |
| 798 | 799 | 799 |

### Group 257 — 3 occurrences

Key: `{"age": "41", "sex": "0", "cp": "2", "trestbps": "112", "chol": "268", "fbs": "0", "restecg": "0", "thalach": "172", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 435 | 436 | 436 |
| 679 | 680 | 680 |
| 742 | 743 | 743 |

### Group 258 — 4 occurrences

Key: `{"age": "67", "sex": "1", "cp": "0", "trestbps": "120", "chol": "229", "fbs": "0", "restecg": "0", "thalach": "129", "exang": "1", "oldpeak": "2.6", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 438 | 439 | 439 |
| 738 | 739 | 739 |
| 801 | 802 | 802 |
| 854 | 855 | 855 |

### Group 259 — 4 occurrences

Key: `{"age": "47", "sex": "1", "cp": "2", "trestbps": "130", "chol": "253", "fbs": "0", "restecg": "1", "thalach": "179", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 439 | 440 | 440 |
| 445 | 446 | 446 |
| 605 | 606 | 606 |
| 918 | 919 | 919 |

### Group 260 — 4 occurrences

Key: `{"age": "52", "sex": "1", "cp": "0", "trestbps": "112", "chol": "230", "fbs": "0", "restecg": "1", "thalach": "160", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 450 | 451 | 451 |
| 732 | 733 | 733 |
| 804 | 805 | 805 |
| 861 | 862 | 862 |

### Group 261 — 4 occurrences

Key: `{"age": "63", "sex": "0", "cp": "0", "trestbps": "150", "chol": "407", "fbs": "0", "restecg": "0", "thalach": "154", "exang": "0", "oldpeak": "4", "slope": "1", "ca": "3", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 451 | 452 | 452 |
| 482 | 483 | 483 |
| 686 | 687 | 687 |
| 890 | 891 | 891 |

### Group 262 — 3 occurrences

Key: `{"age": "49", "sex": "0", "cp": "1", "trestbps": "134", "chol": "271", "fbs": "0", "restecg": "1", "thalach": "162", "exang": "0", "oldpeak": "0", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 452 | 453 | 453 |
| 454 | 455 | 455 |
| 940 | 941 | 941 |

### Group 263 — 3 occurrences

Key: `{"age": "69", "sex": "1", "cp": "2", "trestbps": "140", "chol": "254", "fbs": "0", "restecg": "0", "thalach": "146", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "3", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 461 | 462 | 462 |
| 551 | 552 | 552 |
| 626 | 627 | 627 |

### Group 264 — 4 occurrences

Key: `{"age": "58", "sex": "0", "cp": "0", "trestbps": "130", "chol": "197", "fbs": "0", "restecg": "1", "thalach": "131", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 473 | 474 | 474 |
| 561 | 562 | 562 |
| 640 | 641 | 641 |
| 805 | 806 | 806 |

### Group 265 — 3 occurrences

Key: `{"age": "41", "sex": "1", "cp": "2", "trestbps": "130", "chol": "214", "fbs": "0", "restecg": "0", "thalach": "168", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 474 | 475 | 475 |
| 568 | 569 | 569 |
| 701 | 702 | 702 |

### Group 266 — 3 occurrences

Key: `{"age": "58", "sex": "1", "cp": "0", "trestbps": "128", "chol": "216", "fbs": "0", "restecg": "0", "thalach": "131", "exang": "1", "oldpeak": "2.2", "slope": "1", "ca": "3", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 480 | 481 | 481 |
| 706 | 707 | 707 |
| 1016 | 1017 | 1017 |

### Group 267 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "0", "trestbps": "135", "chol": "234", "fbs": "0", "restecg": "1", "thalach": "161", "exang": "0", "oldpeak": "0.5", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 496 | 497 | 497 |
| 900 | 901 | 901 |
| 985 | 986 | 986 |

### Group 268 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "140", "chol": "239", "fbs": "0", "restecg": "1", "thalach": "160", "exang": "0", "oldpeak": "1.2", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 499 | 500 | 500 |
| 824 | 825 | 825 |
| 924 | 925 | 925 |

### Group 269 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "0", "trestbps": "112", "chol": "290", "fbs": "0", "restecg": "0", "thalach": "153", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 513 | 514 | 514 |
| 564 | 565 | 565 |
| 574 | 575 | 575 |

### Group 270 — 4 occurrences

Key: `{"age": "58", "sex": "1", "cp": "1", "trestbps": "125", "chol": "220", "fbs": "0", "restecg": "1", "thalach": "144", "exang": "0", "oldpeak": "0.4", "slope": "1", "ca": "4", "thal": "3"}`

Target counts: {'1': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 522 | 523 | 523 |
| 744 | 745 | 745 |
| 750 | 751 | 751 |
| 832 | 833 | 833 |

### Group 271 — 3 occurrences

Key: `{"age": "67", "sex": "0", "cp": "2", "trestbps": "152", "chol": "277", "fbs": "0", "restecg": "1", "thalach": "172", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 523 | 524 | 524 |
| 723 | 724 | 724 |
| 947 | 948 | 948 |

### Group 272 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "3", "trestbps": "178", "chol": "270", "fbs": "0", "restecg": "0", "thalach": "145", "exang": "0", "oldpeak": "4.2", "slope": "0", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 529 | 530 | 530 |
| 625 | 626 | 626 |
| 897 | 898 | 898 |

### Group 273 — 3 occurrences

Key: `{"age": "60", "sex": "0", "cp": "0", "trestbps": "150", "chol": "258", "fbs": "0", "restecg": "0", "thalach": "157", "exang": "0", "oldpeak": "2.6", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 531 | 532 | 532 |
| 726 | 727 | 727 |
| 889 | 890 | 890 |

### Group 274 — 3 occurrences

Key: `{"age": "53", "sex": "0", "cp": "0", "trestbps": "138", "chol": "234", "fbs": "0", "restecg": "0", "thalach": "160", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 534 | 535 | 535 |
| 566 | 567 | 567 |
| 837 | 838 | 838 |

### Group 275 — 3 occurrences

Key: `{"age": "50", "sex": "0", "cp": "2", "trestbps": "120", "chol": "219", "fbs": "0", "restecg": "1", "thalach": "158", "exang": "0", "oldpeak": "1.6", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 537 | 538 | 538 |
| 616 | 617 | 617 |
| 697 | 698 | 698 |

### Group 276 — 3 occurrences

Key: `{"age": "44", "sex": "1", "cp": "2", "trestbps": "140", "chol": "235", "fbs": "0", "restecg": "0", "thalach": "180", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 542 | 543 | 543 |
| 582 | 583 | 583 |
| 741 | 742 | 742 |

### Group 277 — 3 occurrences

Key: `{"age": "68", "sex": "1", "cp": "2", "trestbps": "118", "chol": "277", "fbs": "0", "restecg": "1", "thalach": "151", "exang": "0", "oldpeak": "1", "slope": "2", "ca": "1", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 550 | 551 | 551 |
| 673 | 674 | 674 |
| 833 | 834 | 834 |

### Group 278 — 3 occurrences

Key: `{"age": "67", "sex": "1", "cp": "0", "trestbps": "125", "chol": "254", "fbs": "1", "restecg": "1", "thalach": "163", "exang": "0", "oldpeak": "0.2", "slope": "1", "ca": "2", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 556 | 557 | 557 |
| 787 | 788 | 788 |
| 1000 | 1001 | 1001 |

### Group 279 — 3 occurrences

Key: `{"age": "50", "sex": "0", "cp": "0", "trestbps": "110", "chol": "254", "fbs": "0", "restecg": "0", "thalach": "159", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 567 | 568 | 568 |
| 993 | 994 | 994 |
| 1024 | 1025 | 1025 |

### Group 280 — 3 occurrences

Key: `{"age": "54", "sex": "0", "cp": "2", "trestbps": "135", "chol": "304", "fbs": "1", "restecg": "1", "thalach": "170", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 571 | 572 | 572 |
| 690 | 691 | 691 |
| 953 | 954 | 954 |

### Group 281 — 3 occurrences

Key: `{"age": "46", "sex": "1", "cp": "1", "trestbps": "101", "chol": "197", "fbs": "1", "restecg": "1", "thalach": "156", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 581 | 582 | 582 |
| 769 | 770 | 770 |
| 856 | 857 | 857 |

### Group 282 — 3 occurrences

Key: `{"age": "55", "sex": "1", "cp": "1", "trestbps": "130", "chol": "262", "fbs": "0", "restecg": "1", "thalach": "155", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 583 | 584 | 584 |
| 751 | 752 | 752 |
| 905 | 906 | 906 |

### Group 283 — 3 occurrences

Key: `{"age": "64", "sex": "1", "cp": "0", "trestbps": "145", "chol": "212", "fbs": "0", "restecg": "0", "thalach": "132", "exang": "0", "oldpeak": "2", "slope": "1", "ca": "2", "thal": "1"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 595 | 596 | 596 |
| 609 | 610 | 610 |
| 1001 | 1002 | 1002 |

### Group 284 — 3 occurrences

Key: `{"age": "63", "sex": "0", "cp": "1", "trestbps": "140", "chol": "195", "fbs": "0", "restecg": "1", "thalach": "179", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "2", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 600 | 601 | 601 |
| 604 | 605 | 605 |
| 694 | 695 | 695 |

### Group 285 — 4 occurrences

Key: `{"age": "66", "sex": "1", "cp": "0", "trestbps": "112", "chol": "212", "fbs": "0", "restecg": "0", "thalach": "132", "exang": "1", "oldpeak": "0.1", "slope": "2", "ca": "1", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 607 | 608 | 608 |
| 699 | 700 | 700 |
| 915 | 916 | 916 |
| 1003 | 1004 | 1004 |

### Group 286 — 4 occurrences

Key: `{"age": "55", "sex": "0", "cp": "0", "trestbps": "128", "chol": "205", "fbs": "0", "restecg": "2", "thalach": "130", "exang": "1", "oldpeak": "2", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 612 | 613 | 613 |
| 717 | 718 | 718 |
| 891 | 892 | 892 |
| 1006 | 1007 | 1007 |

### Group 287 — 3 occurrences

Key: `{"age": "43", "sex": "1", "cp": "0", "trestbps": "115", "chol": "303", "fbs": "0", "restecg": "1", "thalach": "181", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 617 | 618 | 618 |
| 800 | 801 | 801 |
| 858 | 859 | 859 |

### Group 288 — 3 occurrences

Key: `{"age": "69", "sex": "0", "cp": "3", "trestbps": "140", "chol": "239", "fbs": "0", "restecg": "1", "thalach": "151", "exang": "0", "oldpeak": "1.8", "slope": "2", "ca": "2", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 629 | 630 | 630 |
| 943 | 944 | 944 |
| 960 | 961 | 961 |

### Group 289 — 4 occurrences

Key: `{"age": "65", "sex": "1", "cp": "3", "trestbps": "138", "chol": "282", "fbs": "1", "restecg": "0", "thalach": "174", "exang": "0", "oldpeak": "1.4", "slope": "1", "ca": "1", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 630 | 631 | 631 |
| 639 | 640 | 640 |
| 855 | 856 | 856 |
| 1017 | 1018 | 1018 |

### Group 290 — 4 occurrences

Key: `{"age": "61", "sex": "1", "cp": "0", "trestbps": "138", "chol": "166", "fbs": "0", "restecg": "0", "thalach": "125", "exang": "1", "oldpeak": "3.6", "slope": "1", "ca": "1", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 634 | 635 | 635 |
| 661 | 662 | 662 |
| 825 | 826 | 826 |
| 848 | 849 | 849 |

### Group 291 — 3 occurrences

Key: `{"age": "65", "sex": "1", "cp": "0", "trestbps": "120", "chol": "177", "fbs": "0", "restecg": "1", "thalach": "140", "exang": "0", "oldpeak": "0.4", "slope": "2", "ca": "0", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 644 | 645 | 645 |
| 754 | 755 | 755 |
| 944 | 945 | 945 |

### Group 292 — 3 occurrences

Key: `{"age": "66", "sex": "0", "cp": "3", "trestbps": "150", "chol": "226", "fbs": "0", "restecg": "1", "thalach": "114", "exang": "0", "oldpeak": "2.6", "slope": "0", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 653 | 654 | 654 |
| 665 | 666 | 666 |
| 714 | 715 | 715 |

### Group 293 — 3 occurrences

Key: `{"age": "55", "sex": "0", "cp": "1", "trestbps": "135", "chol": "250", "fbs": "0", "restecg": "0", "thalach": "161", "exang": "0", "oldpeak": "1.4", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 692 | 693 | 693 |
| 719 | 720 | 720 |
| 730 | 731 | 731 |

### Group 294 — 4 occurrences

Key: `{"age": "39", "sex": "1", "cp": "0", "trestbps": "118", "chol": "219", "fbs": "0", "restecg": "1", "thalach": "140", "exang": "0", "oldpeak": "1.2", "slope": "1", "ca": "0", "thal": "3"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 695 | 696 | 696 |
| 921 | 922 | 922 |
| 976 | 977 | 977 |
| 982 | 983 | 983 |

### Group 295 — 3 occurrences

Key: `{"age": "60", "sex": "0", "cp": "2", "trestbps": "120", "chol": "178", "fbs": "1", "restecg": "1", "thalach": "96", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 709 | 710 | 710 |
| 794 | 795 | 795 |
| 968 | 969 | 969 |

### Group 296 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "0", "trestbps": "108", "chol": "233", "fbs": "1", "restecg": "1", "thalach": "147", "exang": "0", "oldpeak": "0.1", "slope": "2", "ca": "3", "thal": "3"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 720 | 721 | 721 |
| 963 | 964 | 964 |
| 1004 | 1005 | 1005 |

### Group 297 — 4 occurrences

Key: `{"age": "64", "sex": "1", "cp": "2", "trestbps": "140", "chol": "335", "fbs": "0", "restecg": "1", "thalach": "158", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'0': 4}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 721 | 722 | 722 |
| 747 | 748 | 748 |
| 862 | 863 | 863 |
| 938 | 939 | 939 |

### Group 298 — 3 occurrences

Key: `{"age": "68", "sex": "0", "cp": "2", "trestbps": "120", "chol": "211", "fbs": "0", "restecg": "0", "thalach": "115", "exang": "0", "oldpeak": "1.5", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 724 | 725 | 725 |
| 857 | 858 | 858 |
| 859 | 860 | 860 |

### Group 299 — 3 occurrences

Key: `{"age": "44", "sex": "0", "cp": "2", "trestbps": "108", "chol": "141", "fbs": "0", "restecg": "1", "thalach": "175", "exang": "0", "oldpeak": "0.6", "slope": "1", "ca": "0", "thal": "2"}`

Target counts: {'1': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 734 | 735 | 735 |
| 965 | 966 | 966 |
| 1015 | 1016 | 1016 |

### Group 300 — 3 occurrences

Key: `{"age": "52", "sex": "1", "cp": "0", "trestbps": "128", "chol": "255", "fbs": "0", "restecg": "1", "thalach": "161", "exang": "1", "oldpeak": "0", "slope": "2", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 740 | 741 | 741 |
| 850 | 851 | 851 |
| 853 | 854 | 854 |

### Group 301 — 3 occurrences

Key: `{"age": "59", "sex": "1", "cp": "3", "trestbps": "160", "chol": "273", "fbs": "0", "restecg": "0", "thalach": "125", "exang": "0", "oldpeak": "0", "slope": "2", "ca": "0", "thal": "2"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 844 | 845 | 845 |
| 865 | 866 | 866 |
| 875 | 876 | 876 |

### Group 302 — 3 occurrences

Key: `{"age": "54", "sex": "1", "cp": "0", "trestbps": "120", "chol": "188", "fbs": "0", "restecg": "1", "thalach": "113", "exang": "0", "oldpeak": "1.4", "slope": "1", "ca": "1", "thal": "3"}`

Target counts: {'0': 3}; conflicting labels: False.

| Logical record after header | Physical start line | Physical end line |
|---:|---:|---:|
| 879 | 880 | 880 |
| 998 | 999 | 999 |
| 1025 | 1026 | 1026 |

