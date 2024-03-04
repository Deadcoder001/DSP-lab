from collections import Counter

def make_string_with_deletion_and_rearrangement(target_str, available_chars):
    target_count = Counter(target_str)
    available_count = Counter(available_chars)

    common_chars = target_count & available_count

    result_str = ''.join(common_chars.elements())

    return result_str


target_string = "abcde"
available_characters = "aabbccdddee"

result = make_string_with_deletion_and_rearrangement(target_string, available_characters)

print("Target String:", target_string)
print("Available Characters:", available_characters)
print("Resulting String:", result)
