start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print("The odd numbers are:")
for num in range(start, end+1):
    if num % 2 != 0:
        odd=num
        print(odd)

