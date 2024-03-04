test_dict = {'a': [7, 6, 3], 
             'b': [2, 10, 3], 
             'c': [19, 4]}
 
print("The original dictionary is : ",test_dict)
 
res = dict()
for key in sorted(test_dict):
    res[key] = sorted(test_dict[key])

print("The sorted dictionary : ",res)