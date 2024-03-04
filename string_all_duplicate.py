from collections import Counter
 
def find_dup_char(input):

    WC = Counter(input)
 
    for letter, count in WC.items():
        if (count > 1):
            print(letter)
 
 

if __name__ == "__main__":
    input = input("Enter the input String: ")
    find_dup_char(input)