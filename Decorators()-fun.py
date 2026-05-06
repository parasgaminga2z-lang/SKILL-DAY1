def decor(fun):
    def inner():
        value=fun()
        return value+2
    return inner
def num():
    return 10
result=decor(num)
print(result())

#_____________________________
def deco(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@deco
def say():
    print("Hello")

say()
#______________________________
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")
    return wrapper
def say_hello():
    print("Hello")
say_hello = my_decorator(say_hello)
say_hello()

# same code but use @
def my_decorator(func):
    def wrapper():
        print("Before func")
        func()
        print("After func")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()

#___________________________________
#Authentication Example
def auth(func):
    def wrapper(user):
        if user == "admin":
            return func(user)
        else:
            return "Access Denied"
    return wrapper
@auth
def dashboard(user):
    return f"Welcome {user} to dashboard"

# Test cases
print(dashboard("admin"))   # allowed
print(dashboard("guest"))   # not allowed

'''Step-by-Step समझ
1. Decorator क्या कर रहा है?
def auth(func):

👉 ये original function को input में लेता है (यहाँ dashboard)

2. Wrapper function
def wrapper(user):

👉 ये actual function को replace कर देता है
👉 अब dashboard() call करने पर wrapper() चलेगा

3. Condition check
if user == "admin":

👉 अगर user admin है → access allow
👉 नहीं तो → block'''