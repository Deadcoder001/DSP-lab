array = [23,45,67,89,10]
rotation_count = 3

n = len(array)
rotation_count = rotation_count % n 

rotated_array = array[rotation_count:] + array[:rotation_count]

print(f"The array after {rotation_count} left rotations is: {rotated_array}")
