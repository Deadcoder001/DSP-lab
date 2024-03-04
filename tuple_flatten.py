from itertools import chain

tuple_of_lists = ([1, 2, 3], ['a', 'b', 'c'], [4, 5, 6])

flattened_tuple = tuple(chain(*tuple_of_lists))

print("Original Tuple of Lists:", tuple_of_lists)
print("Flattened Tuple:", flattened_tuple)
