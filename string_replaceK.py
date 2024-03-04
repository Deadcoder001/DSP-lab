def replace_multiple_words(input_string, words_to_replace):
    for word in words_to_replace:
        input_string = input_string.replace(word, 'K')
    return input_string


input_string = "This is a sample sentence with some words to replace."
words_to_replace = ["sample", "words", "replace"]

result_string = replace_multiple_words(input_string, words_to_replace)

print("Original string:", input_string)
print("String with replaced words:", result_string)
