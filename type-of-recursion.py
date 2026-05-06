# simple / direct recursion
def print_n(n):
    if n == 0:
        return
    print(n)
    print_n(n-1) 
print_n(5)

#__________________________
def A(n):
    if n <= 0:
        return
    print("A:", n)
    B(n-1)

def B(n):
    if n <= 0:
        return
    print("B:", n)
    A(n-1)
B(5)
A(5)

#_______________________________________-
def is_even(n):
    if n == 0:
        return True
    return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    return is_even(n - 1)

print(is_even(4))   # True
print(is_odd(0))    # True