import pandas as pd
import numpy as np

# --- PROJECT 1: LEGACY FLIGHT OPERATIONS TELEMETRY SANDBOX ---
flight_logs_data = {
    'flight_number': ['AI-101', 'AI-102', 'AI-103', 'AI-101', 'AI-104', 'AI-105', 'AI-102'],
    'destination_hub': ['London', 'New York', np.nan, 'London', 'Tokyo', 'Paris', 'New York'],
    'passenger_count': [245.0, np.nan, 180.0, 245.0, 310.0, np.nan, 285.0],
    'ticket_revenue_usd': ['85000', '120000', '64000', '85000', '145000', '92000', '120000']
}

flight_df = pd.DataFrame(flight_logs_data)
print("\n--- Raw Legacy Flight Log Grid Loaded ---")
print(flight_df)

# --- MILESTONE 1 ---
# 1. Drop all duplicate rows
drop_df = flight_df.drop_duplicates()

# 2. Keep rows where destination hub is logged
clean_df = drop_df[drop_df['destination_hub'].notna()].copy() # Added .copy() to preserve memory streams
print("\n--- Cleaned Aviation Fleet Ledger ---")
print(clean_df) 

# --- MILESTONE 2 ---
# 3. Mutate data type from text string to integer
clean_df['ticket_revenue_usd'] = clean_df['ticket_revenue_usd'].astype(int)

# 4. Calculate column mean and fill empty fields smoothly
mean_df = clean_df['passenger_count'].mean()
clean_df['passenger_count'] = clean_df['passenger_count'].fillna(mean_df)

print("\n--- Milestone 2 Processed Dataset ---")
print(clean_df)


# --- MILESTONE 3: THE GRAND ROUTE PERFORMANCE SUMMARY ---
# Group the dataset by destination and aggregate sums and means simultaneously
final_executive_report = clean_df.groupby('destination_hub').agg({
    'ticket_revenue_usd': 'sum',
    'passenger_count': 'mean'
})

print("\n========================================================================")
print("             MILESTONE 3 REPORT: AVIATION HUB AGGREGATES               ")
print("========================================================================")
print(final_executive_report)
print("========================================================================")

