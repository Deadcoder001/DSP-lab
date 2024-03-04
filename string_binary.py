def is_binary_string(input_string):
    return all(char == '0' or char == '1' for char in input_string)


binary_string = "1010101"
non_binary_string = "10102"

is_binary1 = is_binary_string(binary_string)
is_binary2 = is_binary_string(non_binary_string)

print(f"{binary_string} is {'a binary' if is_binary1 else 'not a binary'} string.")
print(f"{non_binary_string} is {'a binary' if is_binary2 else 'not a binary'} string.")
