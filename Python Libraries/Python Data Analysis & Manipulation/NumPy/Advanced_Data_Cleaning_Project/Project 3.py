import numpy as np 

# Step 1 :- Loading the Data -
data = np.genfromtxt(r"C:/Users/Rehan/Downloads/messy_data.csv", delimiter = ",", dtype = str, skip_header = 1)
print("========================================================================")
print("              MILESTONE 1 : Loading the Data               ")
print("========================================================================")
print("Shape of Data : ",data.shape)
print("\nData has Successfully Loaded !!")

# Step 2 :- Removing Space From Employee Column :-
print("\n========================================================================")
print("              MILESTONE 2 : Removing Space From Employee Column               ")
print("========================================================================")
print("Employee Name Before Removing Space : ", data[:,1])
data[:,1] = np.char.strip(data[:,1])
print("\nEmployee Name After Removing Space : ", data[:,1])
print("\nExtra Space is Removed !!")

# Step 3:- Fixing Missing\Nan Values :-
print("\n========================================================================")
print("              MILESTONE 3 : Fixing Missing/NaN Values               ")
print("========================================================================")

# 1. Fixing Missing / NaN Values of Age Column :-
print("FOR AGE COLUMN :- ")
print("\nBefore Cleaning the Age Column :- ", data[:,2])

age_col = data[:,2]
boolean = [ ]
for age in age_col :
    if age.isdigit() and (int(age) < 100) :
        boolean.append(True)
    else :
        boolean.append(False)

boolean = np.array(boolean)
clean_ages = age_col[boolean].astype(int)

mean_age = int(np.mean(clean_ages))

age_col[~boolean] = str(mean_age)
data[:,2] = age_col
print("\nAfter Cleaning the Age Column :- ",data[:,2])

print("\nMean of Age is : ", int(mean_age))
print("\nAge Column is Totally Fixed !!")

# 2. Fixing Missing / NaN Values of Salary Column :-
print("=" * 72)
print("FOR SALRY COLUMN :- ")
print("\nBefore Fixing Salary Column :- ", data[:,3])

sal_col = data[:,3]
valid_salary_mask = [ ]

for salary in sal_col :
    if salary.isdigit() and (int(salary) > 0) :
        valid_salary_mask.append(True)
    else :
        valid_salary_mask.append(False)

valid_salary_mask = np.array(valid_salary_mask)
salary_col = sal_col[valid_salary_mask].astype(int)

mean_sal = int(np.mean(salary_col))

sal_col[~valid_salary_mask] = str(mean_sal)
data[:,3] = sal_col

print("\nAfter Fixing Salary Column",data[:,3])

print("\nMean of Salary is : ", int(mean_sal))
print("\nSalary Column is Totally Fixed !!")

# 3. Fixing Department Column :-
from collections import Counter
print("=" * 80)
print("For DEPARTMENT COLUMN :- ")
print("\nBefore Fixing Department Column :-",data[:,4])
uni_data = data[:,4]
flat_data = uni_data.flatten().tolist()

uni_data[uni_data == 'NaN'] = 'IT'
data[:,4] = uni_data

print("\nAfter Fixing Department Column :-",data[:,4])
print("\nDEPARTMENT Column is Totally Fixed !!")

#Step 4:- Removing Duplicate Rows -
print("\n========================================================================")
print("              MILESTONE 4 : Removing Duplicate Rows               ")
print("========================================================================")
print("Total Rows of Employee Column before Removing Duplicate Rows = ", len(data))
data = np.unique(data, axis = 0)
print("\nTotal Rows of Employee Column After Removing Duplicate Rows = ", len(data))
print("\nDuplicate Rows is Completely Removed !!")

#Step 5 :- Saving the Data -

print("\n========================================================================")
print("              MILESTONE 5 : Saving the Cleaned Data              ")
print("========================================================================")
header = "Emp_ID,Name,Age,Salary,Department"
np.savetxt('Project3_fully_cleaned_data.csv', data, fmt='%s', delimiter=',', header=header, comments='')
print("\nAll the Data has saved.")