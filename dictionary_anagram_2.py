def set_bit_count(num) :
   cnt = 0
   while num:
      cnt += num & 1
      num >>= 1
   return cnt
def solve(x, y) :
   if set_bit_count(x) == set_bit_count(y):
      return True
   return False
x = 9
y = 12
print(solve(x, y))