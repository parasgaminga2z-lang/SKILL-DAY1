msg = "py is awersome"
def myfun():
    a="para"
    print("goloble var", msg)
    print("local var",a)
myfun()
print(msg) # msg is global variable

#____________________________________________________________
#esko bhi pyton me global ki thr trit krte hai
def fun():
    print("inside f", s)
s="python" # indentation ki vjh se golobal scope ban gya 
fun()
print("outside ",s)

#___________________________________________________________
a=1
def myfunction():
    b=2
    print('a=',a)
    print('b=',b)
myfunction()
print(a)
# print(b) # error