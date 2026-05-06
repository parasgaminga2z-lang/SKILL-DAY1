def greet(name="World"):# default parameter
    print("Hello",name) #
greet() # Default Argument

def greet(name): # positional parameter
    print("Hello", name)  
greet("Paras")  # Positional Argument
 #-----------------------------------------------
def multiply(a, b):   # a and b → parameters
    return a * b
print(multiply(4, 5))
'''Features:

Function call directly print ho raha hai

Short, fast, simple

Useful jab sirf ek baar output chahiye

❗ Limitation:

Result store nahi hota

You cannot reuse the result later'''

def multiply(a, b):   # a and b → parameters
    return a * b
result = multiply(4, 5)   # function call / 4 and 5 → arguments
print(result)
'''Features:

Result store ho gaya result variable me

Aap result ko multiple places par use kar sakte ho

Code clean & readable hota hai

Future operations possible'''
#----------------------------------------------------------------
def multiply(a, b):   # a and b → parameters
    return a * b 
print(multiply) # function object reference/ garbage value

def multiply(a=4, b=3):   # a and b →  defualt parameters
    return a * b
print(multiply())