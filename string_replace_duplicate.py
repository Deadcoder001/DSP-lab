def replace_duplicate_occurrence(input_string):
    char_count = {}
    result = []

    for char in input_string:
        if char in char_count:
            char_count[char] += 1
            if char_count[char] == 2:
                result.append('$')  
            else:
                result.append(char)
        else:
            char_count[char] = 1
            result.append(char)

    return ''.join(result)


input_string = "programming"
result_string = replace_duplicate_occurrence(input_string)

print("Original string:", input_string)
print("String with replaced duplicate occurrences:", result_string)
