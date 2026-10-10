# PROJECT 4 :-

import numpy as np

# STEP 1 :- Loading the File -
data = np.genfromtxt(r"C:/Users/Rehan/Downloads/dirty_data.csv", delimiter= ",", dtype= str, skip_header=1)
print("========================================================================")
print("              MILESTONE 1 : Loading of Data               ")
print("========================================================================")
print("Data ka shape hai:", data.shape) 
print("\nData has Successfully Loaded !!")

# STEP 2 :- Handling Missing NaN Values -

# 1. Price_INR Column -
print("\n========================================================================")
print("              MILESTONE 2 : Handling Missing NaN Values              ")
print("========================================================================")
print("Fixing Missing / NaN Values of Price_INR Column :-")
print("\nBefore Cleaning the Price_INR Column = ", data[2:9,3])

price_col = data[:,3]
valid_price_mask = [ ]

for price in price_col :
    if price.isdigit( ) and 0 < int(price) < 900000:
        valid_price_mask.append(True)
    else :
        valid_price_mask.append(False)

valid_price_mask = np.array(valid_price_mask)
clean_price = price_col[valid_price_mask].astype(int)

meadian_price = int(np.median(clean_price))

price_col[~valid_price_mask] = str(meadian_price)
data[:,3] = price_col

print("After Cleaning the Price_INR Column = ", data[2:9,3])
print("\nMedian of Price_INR Column is : ", meadian_price)
print("\nPrice_INR Column is Totally Fixed !!")

print("-" * 100)

# 2. Quantity Column -
print("Fixing Missing / NaN Values of Quantity Column :-")
print("\nBefore Cleaning the Quantity Column = ", data[10:15,4])

quant_col = data[:,4].astype(int)
quantity = np.abs(quant_col)

data[:,4] = quantity

print("After Cleaning the Quantity Column = ", data[10:15,4]) 
print("\nQuantity Column is Totally Fixed !!")

# STEP 3 :- Standardizing city names to Title Case...
print("\n========================================================================")
print("              MILESTONE 3 : Standardizing city names to Title Case              ")
print("========================================================================")
print("Before Standardizing city names to Title Case :", data[0:6,1])
city = data[:,1]
city_col = np.char.title(city)

data[:,1] = city_col

print("After Standardizing city names to Title Case :", data[0:6,1])
print("\nStandardizing City Rows is Done")

print("\n========================================================================")
print("              MILESTONE 5 : Saving the Cleaned Data              ")
print("========================================================================")
header = "Transaction_ID,City,Product,Price_INR,Quantity"
np.savetxt("Project4_fully_cleaned_data.csv", data, fmt='%s', delimiter=',', header=header, comments='')
print("\nAll the Data has saved.")