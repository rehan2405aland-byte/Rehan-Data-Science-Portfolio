# Mini-Project 1: The Sensor Data Cleaning Pipeline 🛠️📊 :-


# Step 1: Clean a Messy Filename (Strings) -

raw_filename = "raw_sensor_data_2026.csv"
data_year = raw_filename[16:20]

# Step 2: Remove Duplicate Sensor Codes (Sets) -

raw_codes = ["Alpha", "Beta", "Alpha", "Gamma", "Beta"]

unique_codes = set(raw_codes)

# Step 3: Process the Metric Readings (Loops & Conditions) -

moisture_readings = [0.45, 0.12, 0.88]
for readings in moisture_readings :
    percentage_moisture_readings = readings * 100
    print("-"*10,"CHECKING STATUS","-"*10)

    if percentage_moisture_readings > 50.0 :
        print("Status: Wet", percentage_moisture_readings)
    else :
        print("Status: Dry", percentage_moisture_readings)
    
# Step 4: Store Final Meta Information (Dictionaries) -

pipeline_summary = {
    "Year" : data_year,
    "Total_unique_sensors" : len(unique_codes),
    "Pipeline_complete" : True
}
print("-"*10,"FINAL PIPELINE SUMMARY","-"*10)
print(pipeline_summary)
