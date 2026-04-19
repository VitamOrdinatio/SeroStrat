# traceable_cases
Pick 2–3 admissions that you can follow from:

- raw serology rows in PIC
- your cE assignment logic
- the final extracted longitudinal lab output

Two clean cases to demonstrate SeroStra is likely sufficient.

## What to show for each case

For each selected HADM_ID, make a tiny markdown case file, maybe in:

```text
docs/traceable_cases/
    hadm_12345.md
    hadm_67890.md
```

For each example, include:

### A. Raw PIC evidence

A small table of the relevant serology rows only, such as:

- CMV IgG
- CMV IgM
- EBV VCA IgG
- EBV VCA IgM
- EBV EBNA IgG
- EBV EBNA IgM

Only include the rows needed to understand a particular example's `cE` status.

### B. Derived cE code

A short explanation like:

- CMV pattern supports recurrent
- EBV pattern supports naive
therefore rN


### C. Extracted lab trajectory

Show one or two example downstream assay series for that same HADM_ID, such as:

- sodium
- pH
- lactate

This proves the end-to-end chain works.

### Why this matters

Demonstrates:
- raw source evidence
- classification decision
- downstream extracted result

That demonstrates auditability.