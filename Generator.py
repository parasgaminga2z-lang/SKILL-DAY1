#_______________________________
# () → generator represent
def count():
    yield 1
    yield 2
    yield 3

gen = count()

print(next(gen))
print(next(gen))
print(next(gen))

#_________________________________
def count(n):
    for i in range(n+1):
        yield i

for i in count(5):
    print(i)
#___________________________
def gen():
    yield from [1, 2, 3]

#_______________________________
# Generator once exhausted → फिर reuse नहीं होता
gen = count()

for i in gen:
    print(i)

for i in gen:
    print(i)   # nothing print होगा

def mygen(x,y):
    while x<=y:
        yield x
        x+=1
g = mygen(5,10)

#+________________________________
nums = (x * 2 for x in range(5))

print(next(nums))   # step 1
input("Press Enter...")

print(next(nums))   # step 2
input("Press Enter...")

print(next(nums))   # step 3


'''👉 अब क्या होगा?

0
(you press enter)
2
(you press enter)
4

👉 अब दिखा? 😎
👉 यही है “wait” (on demand generation)'''

def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i

a = sq_numbers(3)

print("The square of numbers 1, 2, 3 are:")
print(next(a))
print(next(a))
print(next(a))