def contains_all_vowels(input_str):
    cleaned_str = input_str.lower()

    return all(cleaned_str.count(vowel) > 0 for vowel in 'aeiou')

user_input = input("Enter a string: ")

if contains_all_vowels(user_input):
    print(f"The string '{user_input}' contains all vowels.")
else:
    print(f"The string '{user_input}' does not contain all vowels.")
