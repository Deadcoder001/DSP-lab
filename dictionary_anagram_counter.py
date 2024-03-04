from collections import Counter

def largest_anagram_subset(words):
    anagram_counter = Counter(tuple(sorted(word)) for word in words)
    max_subset_size = max(anagram_counter.values(), default=0)
    return max_subset_size


word_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

largest_subset_size = largest_anagram_subset(word_list)

print(f"The size of the largest subset of anagram words is: {largest_subset_size}")
