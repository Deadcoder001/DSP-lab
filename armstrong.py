num = int(input("Enter a number: "))

sum = 0

for digit in str(num):
    sum += int(digit) ** 3
    
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")