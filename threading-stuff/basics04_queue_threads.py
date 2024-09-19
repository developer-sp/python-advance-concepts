'''
In Python's queue module, the queue.task_done() method is used in conjunction with queues, particularly 
when multiple threads are processing tasks from a shared queue. It signals that a formerly enqueued task is complete, 
allowing the queue to track the progress of its tasks and know when all have been processed.

-------------- Importance of Task Done ---------------------
Purpose of queue.task_done()

- When you put a task into a queue using queue.put(), you are adding a unit of work for worker threads. 
- After a worker thread finishes processing a task, it should call task_done() to signal that the task is complete. 
- Without calling task_done(), the queue.join() method, which waits for all tasks to finish, would never return, leading to 
potential deadlocks in your program.
'''

import threading
import queue
import time

# A queue to hold tasks
# We create a queue task_queue to store tasks. Each task is a simple string representing the task name ("Task 1", "Task 2", etc.).
task_queue = queue.Queue()

# Worker function that processes tasks
def worker():
    while True:
        task = task_queue.get()
        if task is None:
            break  # Exit when a None task is received
        print(f"Processing task: {task}")
        time.sleep(2)  # Simulate time-consuming task
        task_queue.task_done()  # Mark the task as done

# Create a few worker threads
# We start 3 worker threads. Each thread pulls tasks from the queue using task_queue.get() and processes them. 
# Once a task is completed, the thread calls task_queue.task_done() to signal the task's completion.
num_worker_threads = 3
threads = []
for _ in range(num_worker_threads):
    thread = threading.Thread(target=worker)
    thread.start()
    threads.append(thread)

# Adding tasks to the queue
# The main thread adds 10 tasks to the queue using task_queue.put().
for i in range(10):
    task_queue.put(f"Task {i+1}")

# Wait for all tasks to be processed
# The task_queue.join() call blocks the main thread until all tasks in the queue have been marked 
# as done (i.e., all worker threads have called task_done() for each task).
task_queue.join()  # This blocks until all tasks have been marked as done

print("All tasks are completed!")

# Stopping worker threads by sending a 'None' signal
# After all tasks are processed, we add None to the queue for each worker thread, 
# signaling them to stop, and then we join() them to ensure they finish cleanly.
for _ in range(num_worker_threads):
    task_queue.put(None)

# Wait for all threads to terminate
for thread in threads:
    thread.join()
