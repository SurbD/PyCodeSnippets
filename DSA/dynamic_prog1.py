# <!-- Dynamic Programming -->

from time import perf_counter, time, pro
from contextlib import contextmanager
import functools


# <!-- Runtime Decorator Function -->
def get_runtime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()
        elapsed = end_time - start_time
        print(f'[Program Runtime]: { elapsed }')
        return result
    return wrapper


# <!-- Runtime Context Manager Function -->
@contextmanager
def runtime_fib():
    try:
        start_time = time()
        yield
    finally:
        end_time = time()
        

# <!-- RECURSION -->
# Use Context Manager instead of the Decorator because of Recursion -->
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

# <!-- MEMOIZATION-->
def fib_memo(n, memo):
    if memo[n] != None:
        return memo[n]
    if n <= 2:
        result = 1
    else:
        result = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    memo[n] = result
    return result

def fib2(n):
    memo = [None] * (n+1)
    return fib_memo(n, memo)


# <!-- BOTTOM UP -->
@get_runtime
def fib_bottom_up(n):
    if n == 2 or n == 1:
        return 1
    bottom_fib = [None] * (n+1)
    bottom_fib[1] = 1
    bottom_fib[2] = 1
    for i in range(3, n+1):
        bottom_fib[i] = bottom_fib[i-1] + bottom_fib[i-2]
    return bottom_fib[n]


with runtime_fib():
    result = fib_bottom_up(4000)

print(result)
fib_bottom_up(5)