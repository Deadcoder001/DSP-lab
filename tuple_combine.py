from itertools import product

tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3)

pair_combinations = list(product(tuple1, tuple2))

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("All Pair Combinations using itertools.product():", pair_combinations)
