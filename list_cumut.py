import numpy as np

def cumulative_sum_np(lst):
    return np.cumsum(lst)

my_list = [1, 2, 3, 4, 5]
result = cumulative_sum_np(my_list)
print(result)
