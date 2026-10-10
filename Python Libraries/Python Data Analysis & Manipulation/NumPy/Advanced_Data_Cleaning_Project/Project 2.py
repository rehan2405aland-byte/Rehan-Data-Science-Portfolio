import numpy as np

# Step 1 : Loading the Data :-
data = np.genfromtxt(r"C:/Users/Rehan/Downloads/messy_data_large.csv", delimiter= ",", dtype= str, skip_header=1)
print("========================================================================")
print("              MILESTONE 1 : Shape of Data               ")
print("========================================================================")
print("Shape of Data : ",data.shape)

# Step 2:- Removing Extra Spaces -
print("\n========================================================================")
print("              MILESTONE 2 : Removing Extra Spaces              ")
print("========================================================================")
print("Before Cleaning the Data 2nd Name:", data[1, 1])
print("Before Cleaning the Data 4th Name:", data[3, 1])

data[:,1] = np.char.strip(data[:,1])

print("\nAfter Cleaning 2nd Name:", data[0, 1])
print("After Cleaning 4th Name:", data[3, 1])
print("\nExtra Space is Removed !!! ")

# Step 3 :- Removing Duplicate Rows :-
print("\n========================================================================")
print("              MILESTONE 3 : Removing Duplicate Rows              ")
print("========================================================================")
print("Rows Before Removing Duplicates: ", len(data))

cleaned_data = np.unique(data, axis=0)

print("Rows After Removing Duplicates: ", len(cleaned_data))
print("\nDuplicate Rows are Removed !!")

# Step 4 :- Cleaning the AGE Column :-
print("\n========================================================================")
print("              MILESTONE 4 : Cleaning The Age Column              ")
print("========================================================================")
print("Before Cleaning the Age Column :- ", cleaned_data[13])
age_col = cleaned_data[:, 2]
valid_age_mask = []
for age in age_col:
    if age.isdigit() and (0 < int(age) < 100):
        valid_age_mask.append(True)
    else:
        valid_age_mask.append(False)

valid_age_mask = np.array(valid_age_mask)
clean_ages = age_col[valid_age_mask].astype(int)

mean_age = int(np.mean(clean_ages))
print("\nMean of Age = ",mean_age)

age_col[~valid_age_mask] = str(mean_age)
cleaned_data[:,2] = age_col
print("\nAfter Cleaning the Age Column :- ", cleaned_data[13])
print("\nAge Column is Cleaned !!")

# Step 5 :- Cleaning The Salary Column -
print("\n========================================================================")
print("              MILESTONE 5 : Cleaning The Salary Column              ")
print("========================================================================")
print("Before Cleaning the Salary Column :- ", cleaned_data[92])
print("Before Cleaning the Salary Column :- ", cleaned_data[8])

salary_col = cleaned_data[:, 3]
valid_salary_mask = []
for sal in salary_col:
    if sal.isdigit() and int(sal) > 0 and int(sal) != 99999999 :
        valid_salary_mask.append(True)
    else:
        valid_salary_mask.append(False)

valid_salary_mask = np.array(valid_salary_mask)
clean_salaries = salary_col[valid_salary_mask].astype(float)

median_salary = int(np.median(clean_salaries))
print("\nSalary Median = ", median_salary)

salary_col[~valid_salary_mask] = str(median_salary)

cleaned_data[:, 3] = salary_col

print("\nAfter Cleaning the Salary Column :- ", cleaned_data[92])
print("After Cleaning the Salary Column :- ", cleaned_data[8])
print("\nSalary Column is Cleaned !!")

# Step 6 :- Cleaning The Department Column -
print("\n========================================================================")
print("              MILESTONE 6 : Cleaning The Department Column              ")
print("========================================================================")
print("\nBefore Cleaning the Department Column :- ", cleaned_data[102])
print("Before Cleaning the Department Column :- ", cleaned_data[88]) 
print("Before Cleaning the Department Column :- ", cleaned_data[45])

from collections import Counter

dep_col = cleaned_data[:,4]
clean_dep_col = dep_col.flatten().tolist()
print("\nChecking Department Column :- ", Counter(clean_dep_col))

dep_col[dep_col == "NULL"] = "Data Scientist"
dep_col[dep_col == "NaN"] = "Data Scientist"
dep_col[dep_col == ""] = "Data Scientist"

cleaned_data[:,4] = dep_col
print("\nAfter Cleaning the Department Column :- ", cleaned_data[102])
print("After Cleaning the Department Column :- ", cleaned_data[88])
print("After Cleaning the Department Column :- ", cleaned_data[45])
print("\nDepartment Column is Cleaned !!")

#Step 6 :- Saving the Data -

print("\n========================================================================")
print("              MILESTONE 6 : Saving the Cleaned Data              ")
print("========================================================================")
header = "Emp_ID,Name,Age,Salary,Department"
np.savetxt('Project2_fully_cleaned_data.csv', cleaned_data, fmt='%s', delimiter=',', header=header, comments='')
print("\nAll the Data has saved.")
