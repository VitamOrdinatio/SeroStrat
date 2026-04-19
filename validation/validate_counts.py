## Conceptually, it should answer:
# 1. does any HADM_ID appear in more than one retained cohort?
# 2. does any HADM_ID appear twice within the same cohort file?
# 3. does every retained admission have exactly one cE code?
# 4. are all retained cE codes one of nN, nR, rN, rR?

# validation steps:
# 1. collect all cohort rows
# 2. group by HADM_ID
# 3. assert each HADM_ID maps to one cohort only
# 4. assert no duplicate rows unless duplicates are expected and documented

# toy code to show what validation should ultimately do:
expected = {"nN": 772, "nR": 77, "rN": 2423, "rR": 227}
observed = ...
assert observed == expected