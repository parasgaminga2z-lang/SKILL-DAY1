def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))

#_______________________________________________
def fact(n):
    if n == 1:
        return 1
    
    result = n * fact(n - 1)
    print(result)   # har step ka result print hoga
    return result

print("Final Answer:", fact(5))

#________________________________________________
def fact(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    return 1 if n <= 1 else n * fact(n-1)

print(fact(6))  
print(fact(-3))

#_________________________________________
def count(n):
    if n == 0:
        return
    print(n)
    count(n-1)
print(count(5))