test_str = 'Hello_world_to_all'
 
print("The original string is : " ,test_str)
 
# Convert Snake case to Pascal case
# Using title() + replace()
res = test_str.replace("_", " ").title().replace(" ", "")
 
# printing result 
print("The String after changing case : " ,res)