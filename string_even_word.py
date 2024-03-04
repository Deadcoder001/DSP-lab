def even_length_words(input_str):
    words = input_str.split()

    for word in words:
        if len(word) % 2 == 0:
            print(word)

user_input = input("Enter a string: ")
even_length_words(user_input)
