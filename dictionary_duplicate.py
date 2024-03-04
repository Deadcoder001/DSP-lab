def remove_duplicate_words(sentence):
    words = sentence.split()
    unique_words = set(words)
    result_sentence = ' '.join(unique_words)
    return result_sentence


input_sentence = "This is a sample sentence with duplicate words. This is a sample."

result = remove_duplicate_words(input_sentence)

print("Original Sentence:", input_sentence)
print("Sentence without Duplicate Words:", result)
