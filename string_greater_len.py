def find_long_words(input_str, k):
    words = input_str.split()
    long_words = [word for word in words if len(word) > k]
    return long_words


user_input = input("Enter a string: ")
length_threshold = int(input("Enter the length threshold (k): "))

result = find_long_words(user_input, length_threshold)

print(f"Words greater than length {length_threshold}: {result}")
