"""
Deque is a double ended queue. It takes O(1) for inserting elements at start of a deqeue or
deleting elements from the start of a dequeue unlike list which takes O(n)

A deque is a very efficient list-like structure for adding/removing elements from either side of it.

Technically, deleting and inserting elements at the start ot a list has O(n) complexity, 
whereas the deque as O(1) complexity.

By default deques have arbitrary size (just like lists), but can also be declared to be of 
fixed size.

Once a fixed-size deque fills up, any append operation on one end will push an element out of 
the other end.

A deque is essentially a double-ended queue (hence the name deque).

We can use indexing to access elements directly in the deque, but be aware that this access 
can be slower than accessing elements by index in a list (especially in the middle of the deque). 
Accessing the element at the beginning or the end of a deque however is fast.

So there are some tradeoffs, but if you find using a list for queue-like behavior, inserting and 
deleting elements at the beginning of the list, then a deque is usually the better choice.
"""

from timeit import timeit
from collections import deque

# time taken for appeinding 10_000 elements at begining of list
l = list(range(100_000))
time_taken = timeit("l.insert(0,0)", globals=globals(), number=10_000)
print("Time Taken to Append 10,000 elements at beginning of list")
print(time_taken)

# time taken for removing 10_000 elements at begining of list
l = list(range(100_000))
time_taken = timeit("del l[0]", globals=globals(), number=10_000)
print("\n\nTime Taken to remove 10,000 elements at beginning of list")
print(time_taken)

# Using Deque
# defining a dequeue
dq = deque([1, 2, 3, 4, 5])
print("\n\nPrinting a Deque")
print(dq)

# appending elements to deque - all O(1) operations
dq.append(6)
print("\n\nAppending 6 to End of Dq")
print(dq)

dq.appendleft(0)
print("\n\nAppending 0 to Start of Dq")
print(dq)

dq.extend([66, "az"])
print("\n\nExtending [66, 'az'] to End of Dq")
print(dq)

# here first bg gets added and then wq, so wq will be at 0 index not bg
dq.extendleft(["bg", "wq"])
print("\n\nExtending ['bg', 'wq'] to Start of Dq")
print(dq)

# checking time taken for inserting and removing elements at the end
dq = deque(range(100_000))
time_taken = timeit("dq.appendleft(0)", globals=globals(), number=10_000)
print("\n\nTime Taken to Append 10,000 elements at beginning of dq")
print(time_taken)

dq = deque(range(100_000))
time_taken = timeit("dq.popleft()", globals=globals(), number=10_000)
print("\n\nTime Taken to Remove 10,000 elements at beginning of dq")
print(time_taken)

# poping elements in the list
dq = deque([1, 2, 3, 4, 5])
popped = dq.pop()
print("\n\nPopping at End of Dq")
print(dq)
print("Popped:", popped)

dq = deque([1, 2, 3, 4, 5])
popped = dq.popleft()
print("\n\nPopping at Start of Dq")
print(dq)
print("Popped:", popped)

# Finite Dequeues
dq = deque([1, 2, 3, 4, 5], maxlen=5)
print("\n\nDq of finite length 5", dq)
print("Adding 0 to Start")
dq.appendleft(0)
print(dq)

dq = deque([1, 2, 3, 4, 5], maxlen=5)
print("\n\nDq of finite length 5", dq)
print("Adding 6 to End")
dq.append(6)
print(dq)

# converting deque to list
dq = deque([1, 2, 3, 4, 5])
l = list(dq)
print("\n\nConverting Deque to list")
print(dq)
print(l)

"""
The takeaway here is to always use the most appropriate data structure for your particular 
circumstance. And if you need to continuously insert/delete elements from the left of a list, 
you should really look at using a deque instead - the performance improvements can be substantial.

If you find that you really need slicing or direct access to elements inside the deque (not the 
left or right elements), then you should careful time your code and see which structure will 
perform better. Or you could even have hybrid approaches, where you can perform the 
insertions/deletions on your deque in a first phase, then, assuming the dequeue is not stable, 
extract the dequeue elements as a list, and in a second phase do your slicing and index lookups.
"""
