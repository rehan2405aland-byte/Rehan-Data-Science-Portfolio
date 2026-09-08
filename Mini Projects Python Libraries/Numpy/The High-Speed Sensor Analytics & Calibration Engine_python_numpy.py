# The High-Speed Sensor Analytics & Calibration Engine ⚡📡 :-

print("\n" + "=" * 60)
print("The High-Speed Sensor Analytics & Calibration Engine ⚡📡 :")
print("=" * 60)

import numpy as np 

# 1. Array Construction & Inspection :-

print("\n" + "=" * 70)
print("1. Array Construction & Inspection")
voltage = [1.2, 4.5, 0.0, 3.8, 8.1, 0.0, 5.4]
raw_telemetry = np.array(voltage)
print(" -> Seven Sensor Voltage Entries : ",raw_telemetry)
print("=" * 70)

# 2. Element-Wise Calibration Math :-

print("\n" + "=" * 70)
print("2. Element-Wise Calibration Math")
calibrated_telemetry = raw_telemetry * 10 + 1.5
print(" -> Calibrated Telemetry : ",calibrated_telemetry)
print("=" * 70)

# 3. Surgical Slicing :-

print("\n" + "=" * 70)
print("3. Surgical Slicing ")
peak_window = calibrated_telemetry[2:6]
print(" ->  Middle Chunk of Data : ",peak_window)
print("=" * 70)

# 4. Conditional Outlier Filtering :-

print("\n" + "=" * 70)
print("4. Conditional Outlier Filtering")
surges = calibrated_telemetry[calibrated_telemetry > 40.0]
print(" -> Electrical Surge Anomaly : ",surges)
print("=" * 70)

# 5. Statistical Diagnostics :-

print("\n" + "=" * 70)
print("5. Statistical Diagnostics : ")
avg_calibrated_telemetry = np.mean(calibrated_telemetry)
print(" -> Mean Average Value : ",avg_calibrated_telemetry)
print("=" * 70)

print("\n[⚡ CALIBRATED PIPELINE COMPLETE]")

