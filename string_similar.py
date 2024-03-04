def find_matching_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)

    matching_characters = set1.intersection(set2)

    return matching_characters

string1 = "hello"
string2 = "world"

matching_characters = find_matching_characters(string1, string2)
matching_count = len(matching_characters)

print(f"Matching characters between '{string1}' and '{string2}': {matching_characters}")
print(f"Number of matching characters: {matching_count}")
