li = [(3, 1), (9, 10), (1, 6), (10, 13), (45, 56)]
  
print("List: ",li)
  
tup, K = (10, 12), 1
 
min_dif, res = 999999999, None
for i, val in enumerate(li):
    dif = abs(tup[K - 1] - val[K - 1])
    if dif < min_dif:
        min_dif, res = dif, i
         
print("The nearest tuple to Kth index element is: " ,li[res])