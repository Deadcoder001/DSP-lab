my_list = [12,33,43,44,55,23,34]
N = int(input("Enter the value of N: "))

if len(my_list) < N:
    print("List should have at least", N ,"elements to find the", N," largest elements.")
else:
    l = sorted(my_list, reverse=True)[:N]

    print("The",N," largest elements in the list are: ",l)
