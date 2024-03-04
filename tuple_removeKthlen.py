tuple_list = [(1, 2, 3), ('a', 'b'), (4, 5, 6, 7), ('x', 'y', 'z')]

k = 3

filtered_tuples = [tup for tup in tuple_list if len(tup) != k]

print("Original List of Tuples:", tuple_list)
print(f"Tuples after removing length {k}:", filtered_tuples)
