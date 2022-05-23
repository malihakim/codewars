#Given an integral number, determine if it's a square number. 

import math
def is_square(n):
    if n >= 0:
        sqrt = math.sqrt(n)
        return sqrt.is_integer()
    return False

    
#BEST:
import math
def is_square2(n):
    return n > -1 and math.sqrt(n) % 1 == 0;


print(is_square(-1))
print(is_square(0))
print(is_square(8))
print(is_square(100))

print(is_square2(-1))
print(is_square2(0))
print(is_square2(8))
print(is_square2(100))
