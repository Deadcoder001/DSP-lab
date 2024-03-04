def reverse(text):
    rev=""
    for i in text:
        rev=i+rev
    return rev

def pal(text):
    rever=reverse(text)
    if rever==text:
        return("Plindrome")
    else:
        return("Not Palindrome")
    
pallin=pal("basab")
print(pallin)


    