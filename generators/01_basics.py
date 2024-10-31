'''
Generators in Python are a special type of iterator, defined using a function and the yield statement, rather than return. 
They allow you to iterate over a sequence of values without storing the entire sequence in memory. 
This is especially useful for handling large datasets or streams of data, as generators yield one item at a time, making them memory-efficient.
'''

# ------------------------ Simple Generators ------------------------
def simple_generator():
    print("First value")
    yield 1
    print("Second value")
    yield 2
    print("Third value")
    yield 3

# Create a generator object
gen = simple_generator()

# Iterating through the generator
for value in gen:
    print("Received:", value)

# When iterated, the generator yields values one by one and stops at each yield. 
# When the next value is requested, it resumes from where it last left off.
# This allows for a "lazy" production of values, one at a time, rather than all at once.



# -------------------- Generator expression ----------------------------
# A generator expression is similar to a list comprehension, but it produces values one at a time rather than creating a complete list in memory.
gen_expr = (x * x for x in range(5))

# Iterating through the generator expression
for value in gen_expr:
    print(value)

# This expression is memory-efficient, as it doesn’t create an entire list in memory but yields each value as needed.



# ---------------------- Generator with yield and send -----------------------------
# Generators can receive input through the send() method, allowing for more interactive generator behavior.

def interactive_generator():
    total = 0
    while True:
        value = yield total  # Yield the current total and wait for a new value
        if value is not None:  # Check if a new value was sent
            total += value

gen = interactive_generator()
print(next(gen))  # Initialize the generator, output: 0
print(gen.send(10))  # Add 10, output: 10
print(gen.send(5))   # Add 5, output: 15
print(gen.send(3))   # Add 3, output: 18

# interactive_generator keeps a running total.
# When send() is called, the generator resumes, and value gets updated.
# The generator can maintain state between yields, allowing for complex data processing.
