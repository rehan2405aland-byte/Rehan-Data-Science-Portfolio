# ========================================================================
# PORTFOLIO PROJECT 2: CORPORATE SUPPLY CHAIN LOGISTICS & FREIGHT ENGINE
# DEVELOPER: DATA ENGINEERING SPECIALIST
# ========================================================================

import pandas as pd

# --- MILESTONE 1: ENGINEERING THE CORE FREIGHT LEDGER ---
# Establishing the production data sandbox framework with balanced index lists
shipment_data = {
    'shipment_id': [1,2,3,4,5,6],
    'origin_hub': ['Mumbai', 'Delhi', 'Bangalore', 'Mumbai', 'Delhi', 'Bangalore'],
    'transit_days': [3, 7, 2, 5, 8, 3],
    'freight_cost': [1200.50, 4500.00, 950.00, 2100.25, 5200.00, 1800.75],
    'carrier_tier': ['Express', 'Standard', 'Express', 'Standard', 'Standard', 'Express']
}

# Constructing the master dataframe object
logistics_df = pd.DataFrame(shipment_data)

# Chaining sort and column slicing execution layers into a single reporting view
core_ledger_view = logistics_df.sort_values('freight_cost', ascending=False)[['shipment_id', 'freight_cost', 'carrier_tier']]

print("========================================================================")
print("              MILESTONE 1 REPORT: HIGH-EXPENDITURE LEDGER               ")
print("========================================================================")
print(core_ledger_view)


# --- MILESTONE 2: THE LOGISTICS BOTTLENECK AUDIT ---
# Deploying parenthetical bitwise condition gates to capture high-cost delays
bottleneck_df = logistics_df[(logistics_df['transit_days'] > 4) & (logistics_df['freight_cost'] > 3000.00)]

print("\n========================================================================")
print("              MILESTONE 2 REPORT: CRITICAL TRANSIT BOTTLENECK HUBS       ")
print("========================================================================")
print(bottleneck_df)


# --- MILESTONE 3: THE EXECUTIVE REGIONAL COST SUMMARY ---
# Executing a multi-metric aggregate pass using structural dictionary mapping
regional_summary = logistics_df.groupby('origin_hub').agg({
    'freight_cost': 'sum',
    'transit_days': 'max'
}).rename(columns={'freight_cost': 'total_regional_spend', 'transit_days': 'peak_transit_delay'})

print("\n========================================================================")
print("              MILESTONE 3 REPORT: REGIONAL CAPITAL DISTRIBUTION METRICS ")
print("========================================================================")
print(regional_summary)
print("========================================================================")
