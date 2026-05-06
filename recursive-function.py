'''l=30.33
print(type(l))
'''
def fun(n=3):
    if n==0:
        return
    print("helo")
    fun(n-1)
fun(3)

#________________________________________
def func(n):
    if n == 0:
        return
    func(n - 1)
    print("Hello")
fun(3)
#___________________________________________-
#Fibonacci series print / Simple Iterative Code
def fibo(n):
    a, b=0,1
    for i in range(n):
        print(a, end=" ")
        a, b=b, a+b
fibo(8)
# ptint(fibo(8)) nhi likh skte kyo ki last me None aye ga 