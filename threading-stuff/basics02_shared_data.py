'''
Thread Synchronization: Lock

When multiple threads access shared data, they can corrupt it because threads run concurrently. 
Python provides a Lock object to ensure that only one thread can access shared data at a time.
'''

import threading

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    # for _ in range(1000):
    #     lock.acquire()
    #     counter += 1
    #     lock.release()

    # # We can also use context manager
    # for _ in range(1000):
    #     with lock:
    #         counter += 1

threads = []
for _ in range(10):  # Creating 10 threads
    thread = threading.Thread(target=increment_counter)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")

'''
Explanation:

- Global Counter: Multiple threads attempt to increment a shared counter variable.
- Lock: The lock.acquire() and lock.release() ensure that only one thread increments the counter at a time, avoiding data corruption.
'''
