# store in tupple
def addnum(*args):
    print(args)
    total= sum(args)
    print(total)
addnum(1,4,5)

def addnum(*args):
    total = 0
    for num in args:
        total += num
    return total

print(addnum(1, 4, 5))

def fun (*args):
    print(args)
fun("hell welcome para")