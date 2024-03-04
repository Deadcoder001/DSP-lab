tuple_list = [(1, 5), (2, 3), (3, 8), (4, 1), (5, 6)]

sorted_tuples = sorted(tuple_list, key=lambda x: x[1])

print("Original List of Tuples:", tuple_list)
print("Sorted List of Tuples by Second Item:", sorted_tuples)
