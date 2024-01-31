from collections import defaultdict

cache = {}

def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
        cache[n] = result
        return result

n = 10 # Change this to the desired value of n
fibonacci(n)

for i in range(n, -1, -1):
    count = sum(1 for key in cache if cache[key] == i)
    print(f"Fibonacci of {i} is called {count} times")