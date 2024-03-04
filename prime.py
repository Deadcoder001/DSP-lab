start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print(f"Prime numbers in the interval [{start}, {end}]:")
for number in range(start, end + 1):
    if number > 1:
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                break
        else:
            print(number)
