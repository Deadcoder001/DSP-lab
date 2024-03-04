my_dict = {'hi' : [5,3,8, 0],
   'there' : [22, 51, 63, 77],
   'how' : [7, 0, 22],
   'are' : [12, 11, 45],
   'you' : [56, 31, 89, 90]}

print("The dictionary is : ")
print(my_dict)

my_result = list(sorted({elem for val in my_dict.values() for elem in val}))

print("The unique values are : ")
print(my_result)


