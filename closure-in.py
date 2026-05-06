def outer():
    x=10
    def inner ():
        print(x)

    return inner
func = outer()
func()

#Real Example
def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15

'''समझो:
double = multiplier(2)

👉 n = 2 store हो गया

triple = multiplier(3)

👉 n = 3 store हो गया

👉 हर function अपना अलग memory रखता है'''