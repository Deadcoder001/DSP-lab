array = [12,23,34,45,56,67,78,89,90]
split_index = int(input("Enter the index to split the array: "))

if 0 < split_index < len(array):
    array[:] = array[split_index:] + array[:split_index]

print(f"The array after splitting at index {split_index} and adding the first part to the end is: {array}")
