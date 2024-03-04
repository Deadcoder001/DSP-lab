start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print("The positive numbers are:")
for num in range(start, end+1):
    if num >= 0:
        p=num
        print(p)

