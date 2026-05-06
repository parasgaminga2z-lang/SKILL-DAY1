# global variable ko function ke ander modify krne ke liye global keyword ka use hota hai
# kyoki function ke ander variabl ko local treat kiya jata hai py 
x=10
def fun():
    # x+=5 #error
    print("inside fun ", x) 
fun()
print("out side fun", x)

#__________________________________________________________________
x=10
def fun():
    global x
    x+=5 
    print("inside fun ", x) 
fun()
print("out side fun", x)

#program to get a copy of globle variable into afunction and work with it
a=1
def myfunction ():
    a=2   # a is local var
    x= globals()['a'] # get globale var into x
    print('global var a=', x)
    print('local var a=', a)
myfunction()
print('global var a=', a)