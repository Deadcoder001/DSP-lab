my_list = [24,35,68,9,11,77,54,10]
index1 = int(input("Enter the index of the first element to swap: "))
index2 = int(input("Enter the index of the second element to swap: "))

if 0 <= index1 < len(my_list) and 0 <= index2 < len(my_list):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

    print("List after swapping elements at indices {} and {}:".format(index1, index2), my_list)
else:
    print("Invalid indices. Make sure indices are within the range of the list.")
