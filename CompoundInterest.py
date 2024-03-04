principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time in years: "))
n = float(input("Enter number of times interest applied per time period: "))

amount = principal * (pow((1 + rate / n), n * time))
CI = amount - principal
print("Compound interest is", CI)