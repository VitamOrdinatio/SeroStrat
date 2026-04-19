# methodology



1. Get citi training for controlled access to pic database
2. Download pic database
3. Apply sql database construction patches
4. Run pic sql via postgresql locally
5. Run SeroStrat (/run_pipeline.py)
   - get cE-encoded cohorts
   - remove `mortality: true` cases to arrive at self-limiting cases
   - filter for young neonates (<= 10 mo) using age extrapolation without de-identifying patient
   - obtain cE-encoded cohort labs
   - run example CPD/SPRT analysis module for cE-encoded cohort

We use CPD/SPRT to explore whether infection-state cohorts exhibit detectable shifts in ICU lab trajectories.

# Future methodology directions:
1. Normalize probable patient infection pathology windows
2. Prepare cE-encoded lab observations for ML training (test/train split) + model fit

Overall goal of ML training:
- SeroStrat AI should be able to suggest a possible cE-encoded state for a patient when given ICU lab metrics over time during a patient's hospital stay
- answer if there exists a pathology-defined lab assay observation behaviorial permutation / pattern that is predictive of `cE` status in a neonate, especially for those presenting with epilepsy / seizure / involuntary convulsions

Important Limitations: 
- possibly too much noise for ML training on raw data
- pathology alignment window is likely key to reducing noise
- ML training likely need SPRT or CPD to act as training anchor to maximize predicion of patient `cE` status using ICU lab assay performance alone