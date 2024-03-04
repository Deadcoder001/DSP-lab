my_list = [1, 2, 3]
my_tuple = (4, 5, 6)

my_list.extend(my_tuple)

print("List after adding tuple:", my_list)

resulting_tuple = tuple(my_list) + my_tuple

print("Tuple after adding list:", resulting_tuple)
