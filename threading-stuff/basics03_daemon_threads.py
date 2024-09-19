'''
Daemon Threads
A daemon thread runs in the background and is killed once the main program exits. 
By default, threads are non-daemon, meaning the program waits for them to finish. You can set a thread to daemon mode using thread.setDaemon(True).
'''

import threading
import time

# This task will print for every 2 seconds forever
def background_task():
    while True:
        print("Background task running")
        time.sleep(2)

# Creating a daemon thread
thread = threading.Thread(target=background_task)
# # Depricated
# thread.setDaemon(True)
thread.daemon = True
thread.start()

time.sleep(5)  # Main program waits for 5 seconds
print("Main program finished!")
# Since Main Thread is finished, the corresponding daemon thread will die

# The background task will keep printing every 2 seconds, 
# but since it's a daemon thread, it will stop as soon as the main program exits after 5 seconds.

