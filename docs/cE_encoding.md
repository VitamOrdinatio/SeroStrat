# cE Encoding in SeroStrat

## Purpose

The `cE` encoding system is the core cohort-definition logic used in **SeroStrat**.

It converts pediatric ICU admissions with CMV and EBV serological data into a compact, biologically interpretable infection-state code that supports:

- cohort construction
- age-restricted clinical stratification
- longitudinal lab extraction
- downstream signal analysis
- future CPD / SPRT / ML-ready workflows

In SeroStrat, `cE` is not a cosmetic label. It is the **primary patient-state abstraction** used to transform raw serology observations into clinically meaningful cohorts.

---

## Conceptual Overview

The `cE` code is a **two-character code**:

- **first character** = **CMV serological state**
- **second character** = **EBV serological state**

Each character can take exactly one of three mutually exclusive state values:

- `N` = naïve
- `P` = primary
- `R` = recurrent

This yields **9 theoretical cohort categories**:

- `nN`
- `nP`
- `nR`
- `pN`
- `pP`
- `pR`
- `rN`
- `rP`
- `rR`

SeroStrat uses this coding system to classify admissions after serology extraction and before downstream cohort restriction and longitudinal lab retrieval.

---

## Biological Interpretation

### CMV component
The first character describes whether the admission is interpreted as:

- **naïve to CMV**
- exhibiting a **primary CMV response**
- exhibiting a **recurrent CMV response**

### EBV component
The second character describes whether the admission is interpreted as:

- **naïve to EBV**
- exhibiting a **primary EBV response**
- exhibiting a **recurrent EBV response**

For EBV, the interpretation is informed by serological evidence including:

- **VCA-directed assays**
- **EBNA-directed assays**

This is important because:

- **VCA** is associated with EBV lytic-stage serology
- **EBNA** is associated with EBV latent-stage serology

The `cE` system quickly encodes a patient's immunological status to the common gammaherpesviruses, CMV and EBV, and is biologically meaningful rather than merely administrative.

---

## Intended Use in SeroStrat

The `cE` system exists to support a specific translational workflow:

1. extract admissions with relevant CMV / EBV serology
2. assign each eligible admission a `cE` state
3. filter to clinically motivated age and survival windows
4. retain sufficiently populated cohorts
5. extract longitudinal ICU lab trajectories for the retained admissions

This allows SeroStrat to move from:

- raw PIC database rows

to

- infection-state cohorts with interpretable downstream analytical value

---

## The Nine Theoretical cE Categories

| cE code | CMV state | EBV state | Interpretation |
|---|---|---|---|
| `nN` | naïve | naïve | naïve to both CMV and EBV |
| `nP` | naïve | primary | naïve to CMV, primary EBV response |
| `nR` | naïve | recurrent | naïve to CMV, recurrent EBV response |
| `pN` | primary | naïve | primary CMV response, naïve to EBV |
| `pP` | primary | primary | primary response to both CMV and EBV |
| `pR` | primary | recurrent | primary CMV response, recurrent EBV response |
| `rN` | recurrent | naïve | recurrent CMV response, naïve to EBV |
| `rP` | recurrent | primary | recurrent CMV response, primary EBV response |
| `rR` | recurrent | recurrent | recurrent response to both CMV and EBV |

---

## Worked Examples

### `nN`
A patient labeled `nN` is interpreted as:

- **naïve to CMV**
- **naïve to EBV**

This patient is immunologically naive to both EMV and EBV. This is especially important in neonatal epilepsy / seizure cases as an `nN` state rules out CMV and EBV as the likely etiological agents of involuntary convulsions. An `nN` patient exhibiting involuntary convulsions thus warrants examination of other root causes, including rare genetic disorders (e.g., mitochondrial diseases) or environmental factors (e.g., nutrient deprivation).

### `nR`
A patient labeled `nR` is interpreted as:

- **naïve to CMV**
- **recurrent for EBV**

This is clinically interesting because it isolates admissions where EBV-associated biology may be active without evidence for CMV exposure in the same framework.

### `rN`
A patient labeled `rN` is interpreted as:

- **recurrent for CMV**
- **naïve to EBV**

This provides the complementary contrast for CMV-linked infection-state reasoning.

### `rR`
A patient labeled `rR` is interpreted as:

- **recurrent for CMV**
- **recurrent for EBV**

This is the most direct “double recurrent infection-state” cohort in the framework and is especially relevant to the broader hypothesis that standard ICU labs may contain signals of clinically important infectious states.

---

## SeroStrat v1 Cohort Restriction

Although the `cE` system defines 9 theoretical categories, **SeroStrat v1 does not retain all 9 categories for downstream analysis**.

After cohort construction, exclusions, and sample-size review, the v1 analysis retains the following four age-restricted cohorts:

- `nN`
- `nR`
- `rN`
- `rR`

These represent the four main cohorts with sufficient utility for the current project scope.

### Current retained 10-month cohort sizes
Based on the current project definition:

- `nN` = **772** unique `HADM_ID`s
- `nR` = **77** unique `HADM_ID`s
- `rN` = **2,423** unique `HADM_ID`s
- `rR` = **227** unique `HADM_ID`s

Total retained admissions:

- **3,499** unique `HADM_ID`s

These counts are one of the main validation anchors for the repo.

---

## Why Primary Categories Were Not Retained in v1

The `P` categories remain conceptually valid, but they are not central to the current v1 cohort set because:

- some primary-response groups were too small
- current project emphasis is on retained cohorts with usable downstream analytical volume
- the repo stops at robust cohort engineering and longitudinal extraction rather than overextending into underpowered comparisons

This is an important design choice, not a failure of the encoding system.

---

## Relationship to Age Restriction

The `cE` code alone does not define final cohort membership.

SeroStrat applies additional cohort restriction logic after `cE` encoding, including:

- exclusion of expired admissions to enrich for self-limiting cases
- age restriction to **10 months or younger**
- retention of clinically interpretable and adequately populated cohorts

The 10-month cutoff is tied to literature-guided reasoning around self-limiting neonatal / infant seizure presentation windows in the infection context that motivated the project.

---

## Data Requirements for cE Assignment

To assign a valid `cE` code, SeroStrat requires admissions with sufficient serological evidence from the PIC source environment.

At minimum, the repo should document which serology item IDs are used for:

- CMV IgG
- CMV IgM
- EBV VCA IgG
- EBV VCA IgM
- EBV EBNA IgG
- EBV EBNA IgM

The exact rule implementation may evolve in code, but the conceptual meaning of the `cE` system should remain stable.

---

## Role in the Pipeline

The `cE` engine sits in the middle of the SeroStrat workflow:

1. **PIC source database setup**
2. **serology extraction**
3. **cE encoding**
4. **cohort restriction**
5. **lab item mapping**
6. **longitudinal lab extraction**
7. **summary outputs**
8. **CPD / SPRT module**

Without `cE`, the project would be a broad serology query workflow.  
With `cE`, it becomes a **cohort-engineering system**.

---

## Validation Strategy

The `cE` system should be validated at multiple levels.

### 1. Logic validation
- admissions with known serology patterns should map to expected `cE` states
- the same admission should always receive the same state under fixed rules
- mutually exclusive states must remain mutually exclusive

### 2. Count validation
- cohort counts after encoding should match saved intermediate results
- retained v1 cohort totals should match expected values

### 3. Spot-check validation
- selected admissions should be manually traceable from raw serology rows to final `cE` code

### 4. Pipeline reproducibility
- re-running the encoding stage on the same source data should produce identical cohort assignments

---

## Assumptions

The current `cE` system assumes:

- the selected serology assays correctly represent CMV and EBV exposure states
- the rule set used to infer naïve / primary / recurrent states is biologically meaningful
- available serology coverage is sufficient for useful cohort construction
- admissions lacking sufficient serology should not be forced into a `cE` category

---

## Limitations

The `cE` encoding system has important limitations:

- it depends on which serology assays were ordered and recorded
- serological interpretation is a simplification of underlying infection biology
- small category sizes limit some comparisons
- `cE` does not itself prove seizure causality or predict outcomes
- the repo’s current utility lies in **cohort engineering and analytical substrate generation**, not final clinical diagnosis

---

## Edge Cases

SeroStrat should explicitly account for edge cases such as:

- incomplete serology panels
- repeated admissions for the same patient
- conflicting assay patterns
- admissions with ambiguous evidence for `P` vs `R`
- admissions with sufficient serology for one virus but not the other
- date-shifted or deidentified source timing inherited from PIC

Edge-case handling should be documented in code and validation notes rather than hidden in ad hoc script logic.

---

## One-Sentence Summary

The `cE` encoding system is the core abstraction in SeroStrat that converts raw CMV/EBV serological observations into clinically meaningful pediatric ICU infection-state cohorts suitable for longitudinal lab extraction and downstream signal analysis.
