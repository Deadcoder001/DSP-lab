def find_uncommon_words(str1, str2):
    words1 = set(str1.split())
    words2 = set(str2.split())

    uncommon_words = words1.symmetric_difference(words2)

    return uncommon_words


string1 = "This is the first string."
string2 = "This is the second string with some different words."

uncommon_words_result = find_uncommon_words(string1, string2)

print("String 1:", string1)
print("String 2:", string2)
print("Uncommon words:", uncommon_words_result)
