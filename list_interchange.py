my_list = [21,32,43,56,89,86]

if len(my_list) >= 2:
    my_list[0], my_list[-1] = my_list[-1], my_list[0]

    print("List after interchanging first and last elements:", my_list)
else:
    print("List should have at least two elements for interchange.")
