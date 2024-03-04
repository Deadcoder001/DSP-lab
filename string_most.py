def least_frequent_character(input_str):
    char_frequency = {}
    
    for char in input_str:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    least_frequent_char = max(char_frequency, key=char_frequency.get)

    return least_frequent_char


user_input = input("Enter a string: ")
result = least_frequent_character(user_input)

print(f"Least frequent character in '{user_input}': {result}")
