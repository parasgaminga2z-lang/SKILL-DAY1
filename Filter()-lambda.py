nums = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)

#__________________________________________________
# without lambda same code 
def even_check(x):
    return x % 2 == 0

nums = [1,2,3,4,5,6]
even = tuple(filter(even_check, nums))
print(even)

#_____________________________________________________
nums = [10, 15, 20, 25, 30]

result = list(filter(lambda x: x > 18, nums))
print(result)

#__________________________________________________
def is_even(x):
    if x%2==0:
        return True
    else:
        return Fals
    
lst =[10,23,46,70,99]
lst1=list(filter(is_even,lst))
print(lst)