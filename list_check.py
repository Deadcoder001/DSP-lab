my_list = [12,24,5,67,33,77,73,9,8]

n = int(input("Enter the element to check in the list: "))

if n in my_list:
    print(f"{n} is present in the list.")
else:
    print(f"{n} is not present in the list.")
