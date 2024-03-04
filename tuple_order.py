tuple_list = [('apple', 2), ('orange', 1), ('banana', 3), ('grape', 4)]

order_list = ['orange', 'apple', 'banana', 'grape']

ordered_tuples = sorted(tuple_list, key=lambda x: order_list.index(x[0]))

print("Original List of Tuples:", tuple_list)
print("Order List:", order_list)
print("Ordered List of Tuples based on Order List:", ordered_tuples)
