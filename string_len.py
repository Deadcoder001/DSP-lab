string_example = "Hello, World!"

length1 = len(string_example)
print("Length using len():", length1)

length2 = 0
for char in string_example:
    length2 += 1
print("Length using a loop:", length2)

length3 = string_example.count('')
print("Length using count():", length3 - 1)

length4 = sum(1 for char in string_example)
print("Length using sum() and generator:", length4)