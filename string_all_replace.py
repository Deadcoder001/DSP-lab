def replace_substring(input_string, old_substring, new_substring):
    modified_string = input_string.replace(old_substring, new_substring)
    return modified_string


original_string = "Hello, World! Hello, Python!"
old_substring = "Hello"
new_substring = "Hi"

result = replace_substring(original_string, old_substring, new_substring)
print(f"Original String: {original_string}")
print(f"Modified String: {result}")
