my_list = [(1, 2), (), (3, 4), (), (5, 6), (), (7, 8, 9)]

fl = [t for t in my_list if t]

print("List after removing empty tuples:", fl)
