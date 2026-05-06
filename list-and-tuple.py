# list any type
def show(data):
    print(data)

print("Enter numbers:")
t = [x for x in input().split()]

show(t)

#tuple
def show(data):
    print(data) # yha se print ho rha  hai

print("Enter numbers:")
t = tuple(int(x) for x in input().split())

show(t)