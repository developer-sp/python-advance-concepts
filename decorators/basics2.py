'''
Issue with Decorators: Logging Metadata Lost

One common issue with decorators, particularly when used for logging, is that the metadata associated with the original function can be lost. 
This includes the function name, its docstring, and other attributes. However, this problem can be addressed by using the functools.wraps decorator.

The functools.wraps decorator is a decorator for updating the attributes of the wrapper function to look like the original function. 
This way, when you apply a decorator to a function, the wrapper function will retain the metadata of the original function.
'''
import functools

# Decorator function
def my_logger(func):
    # try running the code by commenting out the @functools.wraps decorator
    @functools.wraps(func)  # Ensure that metadata of 'func' is preserved
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__}")
        # to check the arguments and keyword arguments
        print(args,kwargs)
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished execution")
        return result
    return wrapper

# Function to be decorated
@my_logger
def example_function(x, y):
    """This is an example function."""
    return x + y

# Calling the decorated function
print(example_function.__name__)  # Output: example_function
print(example_function.__doc__)   # Output: This is an example function.
print(example_function(5,10))