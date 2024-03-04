multiple = int(input("Enter the number to find its multiples in the Fibonacci series: "))
n = int(input("Enter the position (n) of the multiple to find: "))

a, b = 0, 1
for _ in range(n - 1):  
    a, b = b, a + b

while a % multiple != 0:
    a, b = b, a + b

print(f"The {n}-th multiple of {multiple} in the Fibonacci series is: {a}")
