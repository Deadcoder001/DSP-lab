import re

def has_url(input_string):
    url_pattern = re.compile(r'https?://\S+|www\.\S+')

    match = re.search(url_pattern, input_string)

    return bool(match)


input_text = "This is a sample text with a URL: https://www.example.com"
if has_url(input_text):
    print("The string contains a URL.")
else:
    print("No URL found in the string.")
