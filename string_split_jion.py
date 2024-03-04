def split_and_join(input_string):
    words_list = input_string.split()

    result_string = ' '.join(words_list)

    return words_list, result_string


input_string = "Hello, this is a sample string."

words, joined_string = split_and_join(input_string)

print("Original string:", input_string)
print("Split into words:", words)
print("Joined back into a string:", joined_string)
