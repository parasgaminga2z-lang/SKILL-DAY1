#Unstructured Program
num = 9

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")


#Structured Programming
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


def main():
    num = 7
    
    if is_prime(num):
        print("Prime")
    else:
        print("Not Prime")


main()
# Structured Programming 
# program to calculat the gross salary and net salary
def da(basic):
    da = basic*80/100
    return da

def hra(basic):
    hra=basic*15/100
    return hra

def pf(basic):
    pf=basic*12/100
    return pf

def itax(gross):
    tax=gross*0.1
    return tax
basic = float(input("enter basic salary"))
gross= basic+da(basic)+hra(basic)
print("your gross salary:{:10.2f}".format(gross))

net= gross - pf(basic) - itax(gross)
print("you net salary :{:10.2f}".format(net))