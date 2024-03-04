def remove_character(input_str, index):
    return input_str[:index] + input_str[index+1:]

original_string = "example"
index_to_remove = int(input("Enter the index to remove: "))
result = remove_character(original_string, index_to_remove)

print("Original String:", original_string)
print(f"String after removing character at index {index_to_remove}:", result)
