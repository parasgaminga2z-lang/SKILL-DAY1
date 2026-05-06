# class Count:
#     def __init__(self, n):
#         self.n = n
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.i < self.n:
#             val = self.i
#             self.i += 1
#             return val
#         else:
#             raise StopIteration
# c = Count(3)

# for i in c:
#     print(i)
def qustion (n):
    num =n
    sum=0
    product=0
    while num>0:
        num=num%10
        sum+=num
        product *=num
        num//=10
    return product - sum
print(qustion(23389))