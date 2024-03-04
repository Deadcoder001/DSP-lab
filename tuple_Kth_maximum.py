import heapq

my_tuple = (4, 2, 7, 1, 9, 3)
k_value = 3


max_k_elements_heapq = heapq.nlargest(k_value, my_tuple)
min_k_elements_heapq = heapq.nsmallest(k_value, my_tuple)

print(f"The maximum {k_value} elements using heapq are: {max_k_elements_heapq}")
print(f"The minimum {k_value} elements using heapq are: {min_k_elements_heapq}")
