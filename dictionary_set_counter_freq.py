from collections import Counter

def can_frequencies_become_same(input_str):
    char_count = Counter(input_str)

    unique_frequencies = set(char_count.values())

    return len(unique_frequencies) == 1 or (len(unique_frequencies) == 2 and 1 in unique_frequencies)


test_string1 = "xyyzz"
test_string2 = "xxyyzz"

result1 = can_frequencies_become_same(test_string1)
result2 = can_frequencies_become_same(test_string2)

print(f"Can frequencies of characters in '{test_string1}' become the same? {result1}")
print(f"Can frequencies of characters in '{test_string2}' become the same? {result2}")
