# find a squre of number in list
def squar(x):
    return x*x
lst=[1,2,3,4]
lst1=list(map(squar,lst))
print(lst1)

#_____________________________________
# using lambda fun
num=[1,2,3,4]
lst1=list(map(lambda x:x*x,num))
print(lst1)

#__________________________________________
# find a product of tow diffrent list
lst1=[1,2,3,4]
lst2=[2,2,2,2]
lst=tuple(map(lambda x,y:x*y,lst1,lst2))
print(lst)