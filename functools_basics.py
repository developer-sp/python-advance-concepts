# ------------------ functools cache ----------------
from functools import cache
import time

@cache
def fib(n):
    time.sleep(0.5)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
# no previously cached result, so it will make 11 calls to the function
start = time.time()
res = fib(10)
end = time.time()
print("Time taken to calculate fibonacci series for value 10: ", end - start,"\n")
# just one call made because of cache decorator
start = time.time()
res = fib(5)
end = time.time()
print("Time taken to calculate fibonacci series for value 5: ", end - start,"\n")
# makes five recoursive calls, other 10 are cached
start = time.time()
res = fib(15)
end = time.time()
print("Time taken to calculate fibonacci series for value 15: ", end - start,"\n")


# ------------------ functools lru_cache ----------------
from functools import lru_cache
import time

# lru_cache is same as cache but with a limit on number of items in cache
# here we are using maxsize=24 which means that cache can hold maximum of 24 calls
# and when we reach that limit then oldest/first called item in cache is removed and new item is added
@lru_cache(maxsize=24)
def fibannoci(n):
    time.sleep(0.5)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibannoci(n-1) + fibannoci(n-2)
    
# no previously cached result, so it will make 11 calls to the function
start = time.time()
res = fibannoci(10)
end = time.time()
print("Time taken to calculate fibonacci series for value 10: ", end - start,"\n")
# just one call made because of cache decorator
start = time.time()
res = fibannoci(5)
end = time.time()
print("Time taken to calculate fibonacci series for value 5: ", end - start,"\n")
# makes five recoursive calls, other 10 are cached
start = time.time()
res = fibannoci(15)
end = time.time()
print("Time taken to calculate fibonacci series for value 15: ", end - start,"\n")