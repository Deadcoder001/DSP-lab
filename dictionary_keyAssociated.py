def keys_for_value(dictionary, value):
    keys_list = [key for key, val in dictionary.items() if val == value]
    return keys_list


my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}

value_to_find = 1
result_keys = keys_for_value(my_dict, value_to_find)

print(f"Keys associated with value {value_to_find}: {result_keys}")
