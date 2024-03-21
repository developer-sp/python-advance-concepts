"""
The itertools module provides us with a wealth of additional functions to help perform operations \
involving iteration.
"""

# mapping functions to lists

l = [0, 2, 4, 6, 8]


def cube(x):
    return x**3


# using map function
res = map(cube, l)
# Now, res is not a list - it is an iterator. This means that the mapping is "lazy" and does not
# happen until we actually iterate over the elements of res:

print("\nMap Object")
print(res)

# iterating over map object
for ele in res:
    print(ele, end=" ")

# We could easily achieve a similar thing using a list comprehension, but if we want to have an
# iterator (with lazy evaluation) instead of the storage and initial CPU upfront cost, we could
# use a generator expression as well.

res = (cube(ele) for ele in l)
print("\n\nGenerator Object from Generator Expression")
print(res)

# iterating over generator object
for ele in res:
    print(ele, end=" ")

# now what if our function takes two arguements
from math import pow

l = [(3, 0), (3, 1), (3, 2), (3, 3)]
res = map(pow, l)
# print(list(res))
# throws an error, as functions in map can accept only 1 parameter

# we can use generator expression for this
res = (pow(a, b) for a, b in l)  # again a generator object generated that is lazy
# res = (pow(*args) for args in l) # this also works
print("\n\nApplying Function that takes multiple inputs to Lists")
print(list(res))

# another way is to use starmap from itertools
from itertools import starmap

# starmap can accept functions that take multiple inputs
res = starmap(pow, l)
print("\n\nUsing Starmap to map Function with multiple args to a list")
print(res)  # starmap also gives out an object, a lazy evaluation
print(list(res))

# there's nothing wrong with generator expression above, but starmap looks cleaner

# -------------------------------------- Chain Function -------------------------------------
"""
Chain function is helpful for iterating across multiple iterables without haiving to create
a temporary union of all iterables
"""

# lets start with an example
a1 = [3, 4, 5, 6]
a2 = 12, 98, 81  # this is a tuple
a3 = "cfzg"

# now let's say we want to iterate over the ele of a1, a2 and a3, in this order
# one way is
a = a1 + list(a2) + list(a3)

print("\n\nManual Iteration over multiple lists")
for ele in a:
    print(ele, end=" ")

# in the above not only we are doing extra work, but we are creating a new variable "a" which
# takes in additonal memory space

# a simpler method is to use chains from itertools
from itertools import chain

print("\n\nUsing Chains to iterate across mutliple lists")
for ele in chain(a1, a2, a3):
    print(ele, end=" ")

# the approach above looks much cleaner and simpler
# now lets say we have below list
a = [[4, 8, 1, 19], "hsyq", (0, 12, 48)]

# if we use the below
# for ele in chain(a):
#     print(ele, end=" ")
# Output: [4,8,1,19] hsyq (0, 12, 48)

# so the above doesn't give the desire result where we want to iterate each ele from sub list
print("\n\nUsing chain.from_iterable to iterate over list of iterables")
for ele in chain.from_iterable(a):
    print(ele, end=" ")

# ----------------------------- islice ---------------------------
# iterators cannot be sliced, for example
l = [0, 2, 4, 6, 8]
res = map(cube, l)
# print(res[:3]) # results in an error
print("\n\nIndexing a Map")
try:
    res[0]
except TypeError as ex:
    print(ex)

# it doesnt work with generators as well
l = (ele * 3 for ele in range(5))
# print(l[:3]) # results in an error
print("\n\nSlicing a Generator")
try:
    l[:5]
except TypeError as ex:
    print(ex)

# so here comes islice, which helps in slicing map and generator objects
from itertools import islice

l = (ele * 3 for ele in range(10))

print("\n\nSlicing and iterating a Generator with islice")
# here we start with index 1, end at index 6 with step size 2
for ele in islice(l, 1, 6, 2):
    print(ele, end=" ")

# redefining the generator because they can be iterated only once
l = (ele * 3 for ele in range(10))
print("\n\nSlicing and iterating a Generator with islice")
# here we start at index 3, None implies we go till last index and with step 3
for ele in islice(l, 3, None, 3):
    print(ele, end=" ")

# redefining the generator because they can be iterated only once
l = (ele * 3 for ele in range(10))
print("\n\nSlicing and iterating a Generator with islice")
# here we start at index 0(we can also use None here), go till index 6 and with step 3
# if we don't provide step size, it assumes as 1
for ele in islice(l, 0, 6, 3):
    print(ele, end=" ")
