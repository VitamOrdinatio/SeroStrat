# Milestone Map: SeroStrat

## Purpose

Build a reproducible clinical cohort engineering pipeline that stratifies pediatric ICU admissions by CMV/EBV serological state, restricts to a clinically motivated infant window, and extracts longitudinal ICU lab trajectories for downstream signal analysis and future seizure-risk modeling.
This repo is built on the PIC database structure, which organizes patient data around PATIENTS, ADMISSIONS, and ICUSTAYS, with large linked tables including LABEVENTS, CHARTEVENTS, PRESCRIPTIONS, and others. The published PIC resource contains 13,449 admissions from 12,881 pediatric patients and over 10 million lab events. 

---

## Terminology

- "cE encoding": two-character infection-state code combining CMV and EBV serological state
- "cohort engineering": the rule-based process of defining analyzable admission groups from raw clinical data
- "longitudinal assay trajectory": time-ordered observations of a selected assay for a retained admission
- "signal characterization": analytical evaluation of temporal patterns without claiming full predictive modeling

---

## Position in the Portfolio

SeroStrat is a translational clinical analytics branch that complements, but does not directly integrate into, the genomics evidence stack.

Genomics spine:
VAP → VDB → interface → GSC / RDGP

Clinical analytics branch:
PIC → serology cohorting → longitudinal assay extraction → substrate preparation for time-series analyses via change-point detection (CPD) + sequential probability ratio test (SPRT)

---

## Strategic Value
SeroStrat signals:
    • clinical data wrangling at real scale 
    • SQL + Python + relational data reasoning 
    • biologically informed cohort construction 
    • longitudinal assay extraction 
    • translational decision-support thinking 
    • readiness for future ML without pretending ML is already solved 
This is a high-differentiation side-branch repo in your portfolio: not genomics-core, but highly relevant to hospital bioinformatics and clinical analytics.


---

## Repo Identity

Expanded title for README:
SeroStrat: Serology-Based Cohort Stratification Engine for Pediatric ICU Data
Core concept:
    • CMV/EBV serology → cE infection-state encoding 
    • cE cohorts → age-filtered, clinically interpretable admissions 
    • retained admissions → longitudinal lab trajectories 
    • trajectories → CPD/SPRT-ready analytical substrate 


---

## Core Output Data Model (v1)

Fields:
- `subject_id`
- `gender`
- `hadm_id`
- `hadm_age_sec`
- `hadm_age_mo`
- `icd10_code_cn`
- `admit_time`
- `discharge_time`
- `ed_reg_time`
- `ed_out_time`
- `icu_stay_id`
- `num_lab_assay_obs`
- `num_lab_assay_types`
- `cE_code`
- `cohort_label`
- `item_id`
- `analyte_name`
- `chart_time`
- `value`
- `value_uom`
- `flag`
- `source_table`
- `run_id`

---

## Example Output (v1)

Fields:
- `subject_id`: 6739
- `gender`: M
- `hadm_id`: 106746
- `hadm_age_sec`: 2040
- `hadm_age_mo`: 0.00077574 
- `icd10_code_cn`: Q24.900
- `admit_time`: 3/24/2093 16:45
- `discharge_time`: 4/3/2093 10:52
- `ed_reg_time`: 3/24/2093 16:45
- `ed_out_time`: 4/3/2093 10:52
- `icu_stay_id`: 12041982
- `num_lab_assay_obs`: 377
- `num_lab_assay_types`: 76
- `cE_code`: nN
- `cohort_label`: doubly-naïve
- `item_id`: 6419
- `analyte_name`: proline, blood
- `chart_time`: 4/3/2093 14:16:32
- `value`: 191.62
- `value_uom`: μmol/L
- `flag`: z (z = normal; within ref range)
- `source_table`: CHARTEVENTS
- `run_id`: 1230481

Note:
This model represents a denormalized longitudinal observation table combining admission-level metadata with assay-level measurements.

---

## Downstream Use

SeroStrat outputs may support:
- time-series signal analysis (CPD / SPRT)
- cohort comparison studies
- feature generation for future predictive modeling
- integration with external clinical or molecular datasets (future work)

---

## Milestones

### M1 — Source Data Reconstruction + Database Readiness

Rebuild and document the PIC source environment needed for the project.

Includes:
    • local PIC relational database setup 
    • documentation of relevant PIC tables 
    • confirmation of identifier logic: 
        ◦ SUBJECT_ID 
        ◦ HADM_ID 
        ◦ ICUSTAY_ID 
    • mapping of relevant serology and lab item IDs 
The PIC paper explicitly describes the three-key hospitalization model and the importance of joining structured tables through those identifiers. 

Goal:
A reproducible local environment where SeroStrat can query the PIC database reliably.

### M2 — Serology Case Identification Layer

Implement reproducible extraction of admissions with relevant CMV/EBV serological measurements.

Includes identification of:
    • CMV IgG 
    • CMV IgM 
    • EBV VCA IgG 
    • EBV VCA IgM 
    • EBV EBNA IgG 
    • EBV EBNA IgM 

This should be driven by:
    • explicit SQL logic 
    • item ID mappings 
    • saved intermediate tables/files 

Goal:
A reproducible set of admissions with serology evidence sufficient for infection-state classification.

### M3 — cE Encoding Engine

Implement the core cE infection-state classification system.

Definition:
    • first character = CMV state 
    • second character = EBV state 
    • each state ∈ {N, P, R} 
    • total theoretical categories = 9: 
        ◦ nN, nP, nR, pN, pP, pR, rN, rP, rR 

This is the conceptual centerpiece of the repo and should be documented clearly.

Goal:
Every eligible admission receives a biologically interpretable cE code.

### M4 — Clinical Cohort Restriction Layer

Reproduce the clinically motivated filtering steps that turn the broad PIC population into the target cohort universe.

Includes:
    • exclusion of expired admissions / non-self-limiting cases 
    • age-window estimation and restriction to 10 months or younger 
    • justification tied to literature-grounded seizure presentation window 
    • retention of adequately powered cohorts 

Your current retained cohorts are:
    • nN = 772 hadms 
    • nR = 77 hadms 
    • rN = 2,423 hadms 
    • rR = 227 hadms 
for a total of 3,499 admissions.

Goal:
A finalized set of four clinically meaningful cohorts for downstream extraction and comparison.

### M5 — Lab Item Mapping + Target Assay Layer

Formalize the extraction target set of ICU lab assays associated with the retained cohort admissions.

Includes:
    • documentation of the 76 retained PIC lab item IDs 
    • any manual or literature-informed mapping logic used to justify them 
    • stable lookup tables linking item IDs to analyte meaning 
    • separation of serology-defining assays from downstream longitudinal assays 

Your prior workflow and status tree show substantial existing work here, including shared lab-item identification, PedSAP-linked interpretation work, and many assay-specific outputs.

Goal:
A reproducible, documented assay universe for extraction.

### M6 — Longitudinal Observation Extraction

Implement reproducible extraction of hadm-specific longitudinal lab trajectories for the retained cohort admissions.

Includes:
    • all observations for each retained HADM_ID 
    • all target lab item IDs 
    • timestamps / ordering fields as available 
    • cohort labels attached to each observation 
    • encounter-level and assay-level outputs 

The repo should make clear that the PIC database includes large structured tables with very high event counts, especially LABEVENTS, and that the work here is a targeted extraction from that large source environment. 

Goal:
A clean, structured longitudinal dataset ready for descriptive analysis and signal modeling.

### M7 — Cohort Summary + Visualization Layer

Produce reproducible summary outputs that explain what SeroStrat has built.

Includes:
    • cohort size tables 
    • age distributions 
    • assay coverage summaries 
    • sex distribution if useful 
    • selected per-assay descriptive plots 
    • pipeline/status summary figures 

Your existing tree and PowerPoint already suggest a strong base of cohort histograms, pie charts, sample size summaries, and assay-level figures.

Goal:
An external reviewer can immediately understand:
    • what the cohorts are 
    • how many admissions are in each 
    • what data were extracted 
    • what the next analytical step would be 

### M8 — CPD / SPRT Analytical Module

Implement a reproducible signal-analysis component as part of the pipeline.

This is now a formal milestone, not just a demo.

Includes:
    • one selected method stack, e.g. CPD and/or Wald’s SPRT 
    • explicit choice of assay(s) and cohort comparison context 
    • documented parameterization 
    • reproducible example runs 
    • clear statement that this is signal characterization / methodological proof-of-concept, not a full clinical classifier 

This belongs in the repo because it demonstrates your analytical headspace and turns SeroStrat from pure wrangling into a clinically aware longitudinal analysis system.

Goal:
At least one fully reproducible time-series signal workflow operating on SeroStrat outputs.

### M9 — Validation Strategy

Define how SeroStrat will establish that cohorting and extraction are correct.

Validation should include:

Cohort logic validation
    • counts match expected intermediate outputs 
    • cE assignment logic matches manual spot checks 
    • retained four cohorts match known totals 

Data extraction validation
    • selected HADM_ID trajectories can be traced back to source tables 
    • assay counts and timestamps behave as expected 
    • no silent duplication or loss in joins 

Clinical sanity validation
    • age restriction behaves as intended 
    • retained cohorts remain clinically interpretable 
    • selected assay trajectories look plausible for ICU data 

Method validation for CPD/SPRT
    • deterministic reruns give identical outputs 
    • selected assay traces produce stable example results under fixed parameters 

Goal:
The repo is defensible under scrutiny, not just computationally productive.

### M10 — Assumptions, Limitations, Edge Cases, Implementation Notes

This repo must fully comply with your newer research standards.

Assumptions
    • serology item mappings are correct 
    • cE state logic is clinically meaningful for cohorting 
    • age estimation logic is adequate for this use case 
    • the selected 76 lab item IDs are appropriate downstream signals 

Limitations
    • single-center Chinese pediatric ICU source 
    • cohorting depends on available serology testing 
    • some categories have limited sample sizes 
    • v1 stops before full predictive modeling 
    • infection-state inference is bounded by observed assays, not direct causal proof 

Edge cases
    • missing serology results 
    • repeated admissions per patient 
    • conflicting or partial serology patterns 
    • multiple observations per assay per encounter 
    • irregular time spacing 
    • sparse trajectories 
    • expired admissions filtering logic 
    • deidentified date handling in source PIC database 

The PIC publication itself notes uneven table coverage and data completeness differences across tables, which supports explicit limitation handling. 

Implementation notes
    • PIC database reconstruction 
    • SQL + SQLAlchemy orchestration 
    • Python looping / extraction logic 
    • structured outputs at cohort, admission, and assay levels 
    • reproducible file organization and run tracking 

Goal:
The repo reads like serious clinical data work.


---

## Release Gate (Public v1.0)

SeroStrat is portfolio-ready when all of the following are true:
    • PIC source environment and required tables are documented 
    • serology extraction is reproducible 
    • cE encoding is implemented and documented 
    • the four retained cohorts are reproduced 
    • the 76 target assays are documented and extracted longitudinally 
    • summary tables and figures exist 
    • at least one CPD/SPRT module runs reproducibly 
    • README and docs clearly include: 
        ◦ objective 
        ◦ approach 
        ◦ assumptions 
        ◦ limitations 
        ◦ edge cases 
        ◦ validation strategy 
        ◦ implementation details 

At that point, SeroStrat becomes a strong public-facing repo.


---

## Future Upgrades (Post v1.0)

These belong later, not in the first public release:
    • fuller temporal normalization framework 
    • richer multi-assay CPD pipelines 
    • ML-ready feature matrix generation 
    • seizure-risk model prototype 
    • clinician-oriented alert logic 
    • integration with broader infectious disease or metabolics contexts 
    • generalization beyond CMV/EBV if justified 


---

## How SeroStrat Fits the Portfolio

Best positioning:
    • not core genomics spine 
    • not completely standalone either 
    • a translational clinical analytics branch that complements the genomics system 

Narrative:
VAP/VDB/RDGP show how you reason from molecular evidence.
SeroStrat shows how you reason from messy real-world clinical ICU data.
That combination is powerful.


---

## One-Sentence Summary
SeroStrat engineers infection-state pediatric ICU cohorts from serology and longitudinal lab data, creating a reproducible substrate for downstream signal detection and future seizure-risk modeling.

