# ---------------------------- LRU Cache -------------------------------
# This decorator will cache the result of a function call.

from functools import lru_cache
import time

# the maxsize = 1024 implies that we will cache at most 1024 function calls
@lru_cache(maxsize=1024)
def waiting_time(wait_time: int):
    time.sleep(wait_time)
    print("Waited for", wait_time, "seconds")

# calling the function the first time
start = time.time()
waiting_time(4)
end = time.time()
print("Executing First time with wait_tim 4 took:", end - start, "seconds.")

# calling the function the second time
start = time.time()
waiting_time(4)
end = time.time()
print("Executing Second time with wait_tim 4 took:", end - start, "seconds.")

# calling the function the third time with a different value of wait_time
start = time.time()
waiting_time(2)
end = time.time()
print("Executing Third time with different wait_tim i.e 2 took:", end - start, "seconds.")