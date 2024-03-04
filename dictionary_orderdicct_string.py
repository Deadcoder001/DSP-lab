from collections import OrderedDict 
def checkOrder(string, pattern): 
    dic = OrderedDict.fromkeys(string) 
    ptr = 0
    for key,value in dic.items(): 
        if (key == pattern[ptr]): 
            ptr = ptr + 1
        if (ptr == (len(pattern))): 
            return 'True'
    return 'False'

string = 'Study tonight'
pattern = 'stu'
print (checkOrder(string,pattern))

string2= 'Welcome'
pattern2= 'cm'
print (checkOrder(string2,pattern2)) 