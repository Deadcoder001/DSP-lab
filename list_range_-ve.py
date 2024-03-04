start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print("The negative numbers are:")
for num in range(start, end+1):
    if num < 0:
        n=num
        print(n)

