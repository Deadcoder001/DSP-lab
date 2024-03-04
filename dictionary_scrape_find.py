import requests
from bs4 import BeautifulSoup

def find_ordered_words(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    words = [word.text.strip() for word in soup.find_all('li')]

    ordered_words = [word for word in words if all(word[i] <= word[i+1] for i in range(len(word)-1))]

    return ordered_words


dictionary_url = 'https://www.yourdictionary.com/word-lists/words-that-begin-with'
ordered_words_list = find_ordered_words(dictionary_url)

print("Ordered Words:")
for word in ordered_words_list[:10]:  # Display the first 10 ordered words
    print(word)
