# Simple Addition
add=lambda a, b: a + b
print(add(3,4))
print((lambda a,b:a+b)(5,5)) # one line


#Without storing in variabl (direct use)
print((lambda x: x + 10)(5))

f=lambda X:X*X
value=f(5)
print("squre of num", value)

# find max number 
max = lambda x,y: x if x>y else y
a, b=[int(n) for n in input("enter num").split()]
print("bigerr num", max(a,b))