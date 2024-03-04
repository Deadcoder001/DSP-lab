test_str = input("Enter the string: ")
 
print("The original string is : ",test_str)
 
res = {key: test_str.count(key) for key in test_str.split()}

print("The words frequency : ",res)