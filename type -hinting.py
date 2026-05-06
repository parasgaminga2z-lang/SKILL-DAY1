def add (a,b):
    return a+b
print(add(4,5))

#________________________
def add (a:int,b:int) -> int:
    return a+b
print(add(2,3))
print(add("2", "3"))  # works tipe hinting


def process(data: int) -> int:
    return data * 2

print(process(5))

#___________________________________
def add(a: int, b: int) -> int:
    return str(a + b)   # intentionally wrong

print(add(2, 3))
