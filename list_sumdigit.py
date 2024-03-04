def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def sum_of_digits_in_list(lst):
    return [sum_of_digits(num) for num in lst]

my_list = [123, 45, 678, 9]
result = sum_of_digits_in_list(my_list)
print(result)
