from collections import OrderedDict

def kth_non_repeating_char(input_str, k):
    char_count = OrderedDict()

    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1

    non_repeating_chars = [char for char, count in char_count.items() if count == 1]

    return non_repeating_chars[k - 1] if len(non_repeating_chars) >= k else None


input_string = "programming"
k_value = 4

result = kth_non_repeating_char(input_string, k_value)

if result:
    print(f"The {k_value}th non-repeating character is: {result}")
else:
    print(f"There are not enough non-repeating characters.")
