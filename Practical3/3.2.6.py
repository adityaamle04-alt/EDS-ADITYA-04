import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Find indices where value matches in array1
indices=np.where(array1 == search_value)
print(indices[0])
# Count occurrences in array1
count = (array1 == count_value).sum()
print(count)
# Broadcasting addition
result_array = array1 + broadcast_value
print(result_array)
# Sort the first array
sorted_array = np.sort(array1)
print(sorted_array)