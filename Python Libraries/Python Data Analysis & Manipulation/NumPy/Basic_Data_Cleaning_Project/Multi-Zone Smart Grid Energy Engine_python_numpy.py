# Multi-Zone Smart Grid Energy Engine :-


import numpy as np

# --- MILESTONE 1: STRUCTURE THE TELEMETRY CANVAS ---
raw_energy_logs = [
    45, 120, 85, 310, 90, 65, 
    410, 150, 75, 500, 210, 95, 
    130, 80, 600, 110, 420, 175, 
    95, 320, 85, 70, 520, 140
]
raw_energy_logs_1 = np.array(raw_energy_logs)
energy_grid = raw_energy_logs_1.reshape(4, 6)
print("--- 2D Smart Grid Matrix ---")
print(energy_grid)

# --- MILESTONE 2: OVERLOAD FILTERING PASS ---
energy_spikes = energy_grid[energy_grid > 400]
print("\n--- Overload Energy Spikes (>400 MWh) ---")
print(energy_spikes)

# --- MILESTONE 3: EXECUTIVE STATISTICAL SUMMARY ---
total = np.sum(energy_grid)
print("\n--- Executive Summary Metrics ---")
print(f"Total Cumulative Consumption: {total} MWh")
print(f"Grid Operational Mean: {np.mean(energy_grid):.2f} MWh")
print(f"Absolute Peak Sensed Load: {np.max(energy_spikes)} MWh")
