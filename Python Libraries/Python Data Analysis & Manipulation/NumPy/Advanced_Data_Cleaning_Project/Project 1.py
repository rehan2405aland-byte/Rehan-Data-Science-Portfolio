# PROJECT 1 :-

import numpy as np 

# STEP 1 :- Loading the File :-
data = np.loadtxt(r"C:/Users/Rehan/Downloads/numpy_raw_matrix.txt", delimiter = ",")
print("========================================================================")
print("              MILESTONE 1 : Shape of Data               ")
print("========================================================================")
print("Shape : ",data.shape)

# STEP 2 :- Analyzing Outliers & Zeroes :-
count_outliers = np.sum(data == 9999.00)
count_zeroes = np.sum(data == 0.00)
print("\n========================================================================")
print("              MILESTONE 2 : Analyzing Outliers & Zeroes               ")
print("========================================================================")
print("Outliers : ", count_outliers, "\nZeroes : ", count_zeroes)

# STEP 3 :- Cleaning the Data :-
clean_data = data.copy()
clean_data[(clean_data == 0) | (clean_data == 9999)] = np.nan
col_means = np.nanmean(clean_data, axis=0)
inds = np.where(np.isnan(clean_data))
clean_data[inds] = np.take(col_means), inds[1]
print("\n========================================================================")
print("              MILESTONE 3 : Cleaned Data               ")
print("========================================================================")
print("How Much Nan Value is Left : ", np.isnan(clean_data).any())
print("How Much 9999 Value is Left:", np.sum(clean_data == 9999))

# STEP 4 :- Statistical Analysis
col_mean = np.mean(clean_data, axis = 0)
col_median = np.median(clean_data, axis = 0)
col_std = np.std(clean_data, axis = 0)
print("\n========================================================================")
print("              MILESTONE 4 : Statistical Analysis               ")
print("========================================================================")
print("Mean = ", col_mean)
print("Median = ", col_median)
print("Standard Deviation = ", col_std)

#STEP 5 :- Saving the Data -

print("\n========================================================================")
print("              MILESTONE 5 : Saving the Cleaned Data              ")
print("========================================================================")
#np.savetxt('Project1_fully_cleaned_data.csv', clean_data, fmt='%s', delimiter=',', comments='')
print("\nAll the Data has saved.")