test_dict = {"a" : 1, "b" :  3, "c" : 2}
 
print("The original dictionary is : " ,test_dict)
 
res = list(test_dict.keys()) + list(test_dict.values())
 
print("The ordered keys and values : ",res)