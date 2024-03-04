def remove_ith_character(input_string, i):
    return input_string[:i] + input_string[i+1:] if 0 <= i < len(input_string) else "Invalid index"

input_string = input("Enter a string: ")

i = int(input("Enter the index of the character to be removed: "))

result = remove_ith_character(input_string, i)
print(result)
