'''
Useful for I/O-bound operations, where tasks like file reading, writing, or network requests can be performed concurrently 
without blocking the main program.

------------ NOTE -----------------

Async vs Threading

Threading uses multiple threads and does context switching between the threads

Async uses a single thread, but switches between the tasks using an event loop

So the Below for Below examples, we can also use Async

'''
import threading
import time

# This takes a total of 6 seconds to run
def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)  # Simulate work

# This takes a total of 6 secconds to run
def print_letters(word):
    for letter in word:
        print(letter)
        time.sleep(1)  # Simulate work

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters, args=('ABCDE',)) # we need to specify "," if there is only 1 element in tuple

# Starting threads
thread1.start()
thread2.start()

# The below print statements runs before even the tasks are completed
print("The threads are not yet completed")

# Wait for both threads to complete
thread1.join()
thread2.join()

print("Both threads are finished!")

# So overall we have done both the tasks combined in 6 seconds
