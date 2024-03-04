my_list = [22,22,34,45,22,33,34]

duplicates = {num for num in my_list if my_list.count(num) > 1}
print("Duplicates in the list are:", list(duplicates))
