# ========================================================================
# PORTFOLIO PROJECT 2: CLINICAL PATIENT HEALTH COHORT ANALYZER
# DEVELOPER: DATA SCIENCE SPECIALIST
# ========================================================================

import numpy as np
import pandas as pd

# --- INITIALIZATION BLOCK ---
clinical_records = {
    "patient_id": [101, 102, 103, 101, 104, 102, 105],
    "blood_pressure_sys": [120, 145, np.nan, 115, 160, 145, np.nan],
    "cholesterol_mg_dl": ["210", "195", "240", "180", "290", "195", "310"],
    "smoker_status": [
        "Non-Smoker",
        np.nan,
        "Smoker",
        "Non-Smoker",
        "Smoker",
        np.nan,
        "Smoker",
    ],
}
patient_df = pd.DataFrame(clinical_records)


# --- MILESTONE 1: INTEGRITY GUARD & DEDUPLICATION PASS ---
# Dropping exact duplicate entries and filtering out rows missing critical blood pressure logs
drop_df = patient_df.drop_duplicates()
clean_patient_df = drop_df[drop_df["blood_pressure_sys"].notna()].copy()


# --- MILESTONE 2: DIAGNOSTIC TYPE MUTATION & BEHAVIORAL DATA PATCH ---
# Converting string text lab readings to integer types and filling missing smoker logs with 'Unknown'
clean_patient_df["cholesterol_mg_dl"] = clean_patient_df[
    "cholesterol_mg_dl"
].astype(int)
clean_patient_df["smoker_status"] = clean_patient_df["smoker_status"].fillna(
    "Unknown"
)


# --- MILESTONE 3: MULTI-CONDITION RISK COHORT EVALUATION MATRIX ---
# Deploying parenthetical bitwise conditions within numpy to tag high-risk cardiovascular profiles
clean_patient_df["clinical_risk_tier"] = np.where(
    (clean_patient_df["blood_pressure_sys"] > 140)
    & (clean_patient_df["cholesterol_mg_dl"] > 200),
    "Critical Priority Tier",
    "Standard Monitoring Tier",
)

print("========================================================================")
print("             MILESTONE 3 REPORT: CLINICAL AUDIT MATRIX                  ")
print("========================================================================")
print(clean_patient_df)
print("========================================================================")


