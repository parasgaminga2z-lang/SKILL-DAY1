# जब तुम multiple values एक साथ function में भेजते हो, उसे group passing कहते हैं
def show(ls):
    for i in ls:
        print (i)
print("enter the num")
ls=[x for x in input().split(' ')]
show(ls)

#----------------------------------------
def calculate(lst):
    n= len(lst)
    sum=0
    for i in lst:
        sum+=i
    avg= sum/n
    return sum, avg
print("enter the num seprate by space")
lst = [int(x) for x in input().split(' ')]
x,y = calculate(lst)
print('total ', x)
print('avg',y)                   

#___________________________________________
