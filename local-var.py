# variable declare inside in the function, 
# access only in the function and function is termenate the locl variable is remove from the memory
def greet():
    msg="hell of world" # lcalvariab;e
    print(msg)
greet()

def myfun():
    a=1
    #print(a)
    a+=1
    print(a)
myfun()
 # print(a) error