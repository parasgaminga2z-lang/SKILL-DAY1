from functools import reduce

nums = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, nums)

print(result)
#_________________________________________|
# find factroial in easy way with reduce()
from functools import reduce
lst=[1,2,3,4,5]
result=reduce(lambda x,y:x*y,lst)
print(result)

#all combind
from functools import reduce

nums = [1, 2, 3, 4, 5]

# double → filter even → sum
result = reduce(
    lambda x, y: x + y,
    filter(lambda x: x % 2 == 0,
           map(lambda x: x * 2, nums))
)

print(result)