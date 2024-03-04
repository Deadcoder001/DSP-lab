import string

def contains_special_characters(input_str):
    special_characters = set(string.punctuation)
    
    return any(char in special_characters for char in input_str)

user_input = input("Enter a string: ")

if contains_special_characters(user_input):
    print(f"The string '{user_input}' contains special characters.")
else:
    print(f"The string '{user_input}' does not contain any special characters.")
