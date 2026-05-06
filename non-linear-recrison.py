def traverse(n):
    if n <= 0:
        return
    print(n)
    traverse(n-1)   # left
    traverse(n-1)   # right

traverse(3)

#____________________________________Optimized (Memoization)
#Fibonacci + memoization (Dynamic Programming) ka exmple
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]
print(fib(7))

#____________________________
# Ye calculate karta hai: xn=x×x(n−1)
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n - 1)
print(power(2,6))