def is_symmetrical(input_str):
    
    cleaned_str = ''.join(input_str.split()).lower()

    return cleaned_str == cleaned_str[::-1]

def is_palindrome(input_str):

    cleaned_str = ''.join(input_str.split()).lower()

    return cleaned_str == cleaned_str[::-1]

user_input = input("Enter a string: ")

if is_symmetrical(user_input):
    print("The string is symmetrical.")
else:
    print("The string is not symmetrical.")

if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
