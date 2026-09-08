# The Enterprise Data Wrangling & Analytics Pipeline! 🐼💼 :-

import pandas as pd

# ==============================================================================
# 📊 STAGE 1: INGESTION & STRUCTURAL INSPECTION
# ==============================================================================
print("\n" + "╔" + "═" * 58 + "╗")
print("║ 📂 DATA PIPELINE INITIALIZED: LOADING ACCOUNTING LEDGERS ║")
print("╚" + "═" * 58 + "╝")

raw_df = pd.read_csv("company_activities.csv")

print("\n -> [SNAPSHOT: TOP 3 RAW RECORDS]")
print("-" * 40)
print(raw_df.head(3))
print("-" * 40)

# ==============================================================================
# 🧼 STAGE 2: INTEGRITY SCAN & MISSING DATA SCRUBBING
# ==============================================================================
print("\n" + "╔" + "═" * 58 + "╗")
print("║ 🔍 RUNNING HEALTH INTEGRITY SCAN: IDENTIFYING DATA GAPS ║")
print("╚" + "═" * 58 + "╝")

print(" -> [NULL MATRIX SUMMARY COUNT]:")
print(raw_df.isna().sum())

raw_df["Session_Duration"] = raw_df["Session_Duration"].fillna(0.0)
print("\n -> [HEALTH STATUS: CLEANED DATA ARCHITECTURE]")
print("-" * 40)
print(raw_df)
print("-" * 40)

# ==============================================================================
# 🎯 STAGE 3: SLICING & HIGH-VALUE ROW FILTERING
# ==============================================================================
print("\n" + "╔" + "═" * 58 + "╗")
print("║ ⚡ BOOSTER GATE: FILTERING HIGH-VALUE ENTERPRISE TARGETS ║")
print("╚" + "═" * 58 + "╝")

high_value_df = raw_df[raw_df["Total_Spend"] > 150]

print(f" -> [ALGORITHM ALERT]: Extracted {len(high_value_df)} Active High-Value Profiles")
print("-" * 40)
print(high_value_df)
print("-" * 40)

# ==============================================================================
# 📊 STAGE 4: CATEGORICAL GROUPING & PERFORMANCE AGGREGATIONS
# ==============================================================================
print("\n" + "╔" + "═" * 61 + "╗")
print("║ 📈 ANALYTICS REPORT: SYSTEM ENGAGEMENT BY BUSINESS DEPARTMENTS ║")
print("╚" + "═" * 61 + "╝")

high_value_df2 = high_value_df.groupby("Department")["Session_Duration"].mean()
print(" -> [FINAL SUMMARY MATRIX]:")
print("-" * 40)
print(high_value_df2)
print("-" * 40)

print("\n 🚀 [SUCCESS] AUTOMATED PIPELINE PIPELINE TRACKING RUN COMPLETELY 100% BLOCKED\n")
