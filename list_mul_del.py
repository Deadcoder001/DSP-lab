my_list = [12,23,3,4,56,70,9]

elements_to_remove = [12,3,23]

for ele in elements_to_remove:
    my_list = [x for x in my_list if x != ele]

print("List after removing elements:", my_list)
