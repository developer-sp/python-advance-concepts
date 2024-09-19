### Why CPU is not required to Process I/O Requests?

It would help to understand the role of 3 important aspects of I/O in computer architecture: Interrupts, DMA, and Hardware Controllers.

When the CPU issues an I/O request to the hard disk, the hard disk has its own specialized chip called a device (or hardware) controller designed solely for processing commands from the CPU, such as reading from the disk. Originally these were simple chips that performed specific operations for the CPU, but modern hardware controllers are basically their own microprocessors with firmware and everything, so they are capable of very complex operations without the main CPU's help. While the hard drive's controller is busy performing the request, the main CPU is free to do whatever it wishes, such as execute process 2 in your example. The controller is able to read and write directly to and from system RAM using what is called a Direct Memory Access (DMA) controller, a special unit that transfers data from the hardware controller to main RAM without the CPU needing to do anything.

When the hard drive is done with the request and the relevant data has been loaded into RAM through DMA, it issues an interrupt request which informs the CPU that the data has been loaded into RAM. At this point the CPU can transfer control back to process 1. Thus, the CPU does not need to micromanage all tasks involved with I/O. At one time this used to be the case, but these tricks (interrupts, DMA, special controllers) were invented in order to improve CPU performance and make things more efficient.

### Daemon Threads

A daemon thread runs in the background and is killed once the main program exits. By default, threads are non-daemon, meaning the program waits for them to finish. You can set a thread to daemon mode using thread.setDaemon(True).

## Multithreading vs MultiProcessing vs Asynchronous

### 1. **Multithreading**

**Multithreading** involves running multiple threads (smaller units of a process) concurrently within the same process. Threads share the same memory space, which makes communication between them faster. However, Python's **Global Interpreter Lock (GIL)** can limit the performance of CPU-bound tasks when using threads, because it prevents multiple threads from executing Python bytecodes simultaneously.

- **Best for**: I/O-bound tasks (waiting for I/O like file operations, network requests, etc.)
- **Not ideal for**: CPU-bound tasks (tasks requiring heavy computation)

#### Example of Multithreading:

```python
import threading
import time

def print_numbers():
    for i in range(5):
        print(f'Number: {i}')
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(f'Letter: {letter}')
        time.sleep(1)

# Creating two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Starting threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()
print("Done")
```

In this example, the two functions `print_numbers` and `print_letters` are executed concurrently. While waiting for `time.sleep()`, the threads alternate execution, which makes this efficient for I/O-bound tasks.

### 2. **Multiprocessing**

**Multiprocessing** involves running multiple processes, each with its own memory space. Unlike threads, each process runs in its own memory space, which avoids issues with the GIL, making it more suitable for CPU-bound tasks. However, communication between processes is slower compared to threads because they do not share memory directly and must communicate via inter-process communication (IPC) mechanisms like pipes, queues, or shared memory.

- **Best for**: CPU-bound tasks (heavy computations, parallelizable workloads)
- **Not ideal for**: Tasks requiring shared memory, where overhead from IPC may slow things down.

#### Example of Multiprocessing:

```python
import multiprocessing
import time

def print_numbers():
    for i in range(5):
        print(f'Number: {i}')
        time.sleep(1)

def print_letters():
    for letter in 'ABCDE':
        print(f'Letter: {letter}')
        time.sleep(1)

if __name__ == "__main__":
    # Creating two processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)

    # Starting processes
    process1.start()
    process2.start()

    # Wait for processes to complete
    process1.join()
    process2.join()
    print("Done")
```

Here, each function runs in its own process, meaning both are completely independent and can be run truly in parallel. So here two processes are spawned. This is well-suited for tasks that are computationally intensive, like matrix multiplication or large dataset processing.

### 3. **Asynchronous Programming**

**Asynchronous programming** allows you to write code that executes tasks asynchronously (non-blocking) by using **`asyncio`** in Python. This is highly useful when dealing with tasks that spend time waiting, like network I/O or file I/O, without needing multiple threads or processes.

- **Best for**: I/O-bound tasks, where tasks wait on I/O operations (e.g., downloading files, making API calls, reading files)
- **Not ideal for**: CPU-bound tasks that need heavy processing.

Unlike multithreading, asynchronous programming uses an **event loop** to switch between tasks that are waiting for I/O. This allows it to handle thousands of concurrent connections in one thread.

#### Example of Asynchronous Programming:

```python
import asyncio

async def print_numbers():
    for i in range(5):
        print(f'Number: {i}')
        await asyncio.sleep(1)

async def print_letters():
    for letter in 'ABCDE':
        print(f'Letter: {letter}')
        await asyncio.sleep(1)

async def main():
    # Running tasks concurrently
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())

    # Wait for both tasks to complete
    await task1
    await task2

# Running the asyncio event loop
asyncio.run(main())
```

In this example, `print_numbers` and `print_letters` are asynchronous functions. The `await` keyword tells the event loop that it can switch to another task while the current task waits (in this case, for `asyncio.sleep`). This way, we can run both functions concurrently without needing multiple threads or processes.

### **Comparison**

| Aspect               | Multithreading                             | Multiprocessing                            | Async Programming                           |
|----------------------|--------------------------------------------|--------------------------------------------|---------------------------------------------|
| **Memory**           | Shared memory between threads              | Separate memory spaces                     | Shared memory within the event loop         |
| **Best for**         | I/O-bound tasks                            | CPU-bound tasks                            | I/O-bound tasks                             |
| **Concurrency Model**| Cooperative multitasking (Separate processes)                  | Parallelism                               | Cooperative multitasking                    |
| **Python GIL**       | Affected by GIL                            | Not affected by GIL                        | Not affected by GIL                         |
| **Overhead**         | Low (context switching within threads)     | High (each process is independent)         | Low (event loop overhead)                   |
| **Communication**    | Easy (shared memory)                       | Complex (Inter-process communication)      | No explicit communication needed            |
| **Example Tasks**    | Web servers, downloading files, network I/O | Large dataset processing, matrix computations | File I/O, network I/O, API calls           |

### **When to Use Which?**

- **Use Multithreading** when your tasks are primarily I/O-bound (e.g., reading/writing files, making network requests) and involve waiting for input/output operations.
- **Use Multiprocessing** for CPU-bound tasks that need parallel execution, such as complex computations, data analysis, or mathematical modeling.
- **Use Asynchronous Programming** when you have many I/O-bound tasks that can benefit from non-blocking, cooperative multitasking in a single thread.

This distinction can help you optimize the performance of your Python applications based on the nature of the tasks they perform.

### Detailed Comparision

| Aspect               | Multithreading                                              | Multiprocessing                                              | Asynchronous Programming                                      |
|----------------------|-------------------------------------------------------------|--------------------------------------------------------------|---------------------------------------------------------------|
| **Concurrency Model** | Uses multiple **threads** within a **single process**. Each thread shares the same memory space. Threads run concurrently but are constrained by the **Global Interpreter Lock (GIL)** in Python for CPU-bound tasks. | Uses multiple **processes**, each with its **own memory space**. Processes run independently and in parallel. Not constrained by the **GIL**, making it ideal for CPU-bound tasks. | Uses a **single thread** with an **event loop** to handle multiple tasks concurrently. Tasks yield control back to the event loop when waiting for I/O (non-blocking operations). |
| **Memory**           | Threads **share memory**, allowing for faster communication between them, but they must be carefully synchronized to avoid race conditions. | Processes have **separate memory spaces**, so communication between processes requires more overhead, typically using inter-process communication (IPC) mechanisms (e.g., pipes, queues). | **Shared memory** within the single thread and event loop. Since tasks run cooperatively (non-blocking), synchronization issues are less common. |
| **Parallelism**       | **Concurrency**, but not true parallelism for CPU-bound tasks due to the GIL. Best suited for I/O-bound tasks where threads can operate while others are waiting on I/O. | **True parallelism**. Each process runs independently, meaning multiple CPU cores can be utilized efficiently. Great for CPU-bound tasks (e.g., heavy computations, parallel data processing). | **Concurrency**, but not parallelism. Tasks take turns running on the same thread, yielding when waiting on I/O. Good for I/O-bound tasks, such as network or file operations. |
| **Python GIL**        | **Affected by GIL**. Only one thread can execute Python bytecode at a time, so it's not efficient for CPU-bound tasks (e.g., calculations). However, it works well for I/O-bound tasks. | **Not affected by GIL**. Each process has its own Python interpreter and memory space, so the GIL doesn't limit multiprocessing. Efficient for CPU-bound tasks. | **Not affected by GIL**. Since tasks are non-blocking and executed in an event loop, GIL constraints do not impact performance. Suitable for I/O-bound tasks. |
| **Best for**          | **I/O-bound tasks** (e.g., file reading/writing, network requests, databases). Since threads can switch during I/O waits, it improves efficiency for I/O-bound operations. | **CPU-bound tasks** (e.g., parallel data processing, image processing, scientific computations). Processes run truly in parallel across multiple CPU cores. | **I/O-bound tasks** (e.g., API calls, downloading files, reading files). Works best when tasks spend time waiting on I/O, as tasks can give up control during wait time. |
| **Number of Threads/Processes** | Multiple **threads** within one process. Threads share the process's resources but must be synchronized. | Multiple **processes** running independently. Each process has its own resources and does not interfere with others. | **Single thread**, multiple concurrent tasks using an event loop. Tasks are asynchronous and take turns running, based on when they need to wait for I/O. |
| **Overhead**          | **Low overhead** for context switching between threads because they share memory, but there’s potential for overhead when dealing with thread synchronization (locks, etc.). | **Higher overhead** due to independent memory spaces. Each process has its own interpreter and memory, leading to more memory and resource usage. | **Low overhead**. Tasks are cooperative, and context switching happens only during I/O waits, which reduces overhead compared to threading and multiprocessing. |
| **Communication**     | Easy, since threads share memory. However, you need to manage synchronization to avoid race conditions (e.g., using locks, semaphores). | Complex, as processes don’t share memory. Communication requires **inter-process communication (IPC)** mechanisms like queues, pipes, or shared memory. | No explicit communication required, as tasks run sequentially but concurrently within the same event loop. |
| **Scalability**       | Limited by the **GIL**, meaning not all threads can run simultaneously on multiple cores. Ideal for tasks involving waiting (I/O-bound). | Scales well across multiple CPU cores. Each process can run on a different core, allowing for true parallelism and better CPU utilization. | Scales efficiently for I/O-bound tasks but limited by a single thread. Multiple I/O operations can be handled concurrently, but for CPU-bound tasks, it won’t improve performance. |
| **Example Tasks**     | Web servers, file downloading, I/O-bound network operations (e.g., web scraping, API calls). | Large data processing, matrix computations, parallelizable algorithms (e.g., machine learning model training). | Network I/O (e.g., handling many API calls), concurrent file operations, non-blocking socket servers. |

### **Key Takeaways**:
- **Multithreading** is best for tasks that involve **waiting** on I/O operations, but it is constrained by Python's GIL for CPU-bound tasks.
- **Multiprocessing** is the go-to for CPU-bound tasks that benefit from **parallel execution** on multiple cores, overcoming the limitations of the GIL.
- **Asynchronous programming** excels at managing large numbers of **concurrent I/O-bound tasks** using a single thread, with minimal overhead, but it does not offer parallelism.

This table should give you a more nuanced understanding of when to use each approach, depending on your specific requirements.