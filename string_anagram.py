def group_anagrams(words):
    anagram_dict = {}

    for word in words:

        key = tuple(sorted(word))

        anagram_dict.setdefault(key, []).append(word)

    return list(anagram_dict.values())

word_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
result = group_anagrams(word_list)

for group in result:
    print(group)
