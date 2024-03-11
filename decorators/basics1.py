# -----------------------Simple Decorator Example ---------------------------------
# Decorator function
def my_decorator(func):
    def wrapper():
        print("\nSomething is happening before the function is called.")
        func()  # Call the original function
        print("Something is happening after the function is called.")
    return wrapper

# Function to be decorated
@my_decorator
def say_hello():
    print("Hello!")

# Call the decorated function
say_hello()

# ----------------------- Simple Decorator Example with Arguments -----------------------
# Define a decorator that takes an argument 'factor'
def multiply_by(factor):
    # Define the actual decorator function that wraps the original function
    def decorator(func):
        # Define the wrapper function that will replace the original function
        def wrapper(*args, **kwargs):
            # Call the original function with any arguments passed to it
            result = func(*args, **kwargs)
            # Multiply the result by the factor passed to the decorator
            return result * factor
        # Return the wrapper function
        return wrapper
    # Return the decorator function
    return decorator

# Apply the multiply_by decorator with argument 3 to the add function
@multiply_by(3)
def add(a, b):
    # Original function: add two numbers
    return a + b

# Call the decorated add function with arguments 2 and 3
print("\nDecorator with Arguments")
print(add(2, 3))  # Output: 15 (because (2 + 3) * 3 = 15)
