list_of_dicts = [
    {'name': 'Alice', 'age': 25, 'score': 90},
    {'name': 'Bob', 'age': 30, 'score': 85},
    {'name': 'Charlie', 'age': 22, 'score': 95}
]

sorted_list = sorted(list_of_dicts, key=lambda x: x['score'])

print("Sorted List:")
for item in sorted_list:
    print(item)
