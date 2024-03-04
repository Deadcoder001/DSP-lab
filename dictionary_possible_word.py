def Countchar(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict
def find_words(word_list, charSet):
    for word in word_list:
        flag = 1
        chars = Countchar(word)
        for key in chars:
            if key not in charSet:
                flag = 0
            else:
                if charSet.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)
            
word_list = ['mat', 'boy', 'bat', 'goal', 'get', 'got', 'orange']
charSet = ['e', 'o', 'b', 'a', 'g', 'l', 't']
find_words(word_list, charSet)