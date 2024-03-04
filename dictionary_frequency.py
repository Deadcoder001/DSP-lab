def count_frequencies(input_list):
    frequency_dict = {}

    for element in input_list:
        frequency_dict[element] = frequency_dict.get(element, 0) + 1

    return frequency_dict


input_list = [1, 2, 3, 1, 2, 1, 4, 5, 4, 3, 2]

result = count_frequencies(input_list)

print("Original List:", input_list)
print("Frequencies:", result)
