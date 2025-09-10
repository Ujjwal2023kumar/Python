import numpy as np
import statistics as stats

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
arr3 = np.array([50, 40, 30, 10])
arr4 = np.array([1,2,2,3,3,3,4,4,4,4])

print("Add:", np.add(arr1, arr2))
print("Subtract:", np.subtract(arr1, arr2))
print("Multiply:", np.multiply(arr1, arr2))
print("Divide:", np.divide(arr1, arr2))
print("Power:", np.power(arr1, arr2))
print("Mod:", np.mod(arr1, arr2))

# Concatenate arrays
print("Concatenate:", np.concatenate((arr1, arr2)))

# Sorting (only one array can be sorted at a time)
print("Sort arr1:", np.sort(arr1))
print("Sort arr2:", np.sort(arr2))

# Stacking
print("Horizontal stack:", np.hstack([arr1, arr2]))
print("Vertical stack:\n", np.vstack([arr1, arr2]))

# Splitting array (must specify number of splits)
print("Split arr3 into 2 parts:", np.array_split(arr3, 2))

# Append elements (append needs values to append)
print("Append to arr1:", np.append(arr1, [20, 30]))

# Insert value at index
print("Insert 20 at index 3:", np.insert(arr3, 3, 20))

# Delete element
print("Delete index 1:", np.delete(arr3, 1))

# Where conditions
print("Where arr1 == 3:", np.where(arr1 == 3))
print("Where arr1 is even:", np.where(arr1 % 2 == 0))

# Searchsorted (returns index to maintain sorted order)
print("Searchsorted 6:", np.searchsorted(arr1, 6))
print("Searchsorted 3:", np.searchsorted(arr1, 3))

#Aggregating functions
print("Sum: ", np.sum(arr1))
print("Max: ", np.max(arr1))
print("Min: ", np.min(arr1))
print("Size: ", np.size(arr1))
print("Cumsum: ", np.cumsum(arr1))
print("Cumsum of 2 Arrays: ", np.cumsum([arr1, arr2]))
print("Cumprod: ", np.cumprod(arr1))
print("Mean: ", np.mean(arr1))
print("Median: ", np.median(arr1))
print("Mode: ", stats.mode(arr4))
print("Standard Deviation: ", np.std(arr1))
print(np.corrcoef([arr1, arr2]))
