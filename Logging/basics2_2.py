import logging  # Importing logging module for logging functionality
import basics2_1  # Importing basics2_1 module

# Creating a logger object specific to the current module
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Setting the logging level to DEBUG

# Creating a formatter object to define the log message format
formatting = logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s",
                              datefmt="%Y-%m-%d %H:%M:%S")

# Creating a file handler to log messages to a file named 'sample.log'
# The sample.log only logs the Errps
file_handler = logging.FileHandler('errors.log')
file_handler.setLevel(logging.ERROR)  # Setting the logging level for the file handler to ERROR
file_handler.setFormatter(formatting)  # Setting the formatter for the file handler

# Creating a stream handler to log messages to the console, this logs anything on and above DEBUG
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatting)  # Setting the formatter for the stream handler

# Adding the file handler to the logger to capture ERROR level messages to the file
logger.addHandler(file_handler)
# Adding the stream handler to the logger to capture all messages to the console
logger.addHandler(stream_handler)

# Function to add two numbers
def add(a, b):
    """
    Add two numbers.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of a and b.
    """
    return a + b

# Function to divide two numbers
def div(a, b):
    """
    Divide two numbers.

    Args:
        a (int): The numerator.
        b (int): The denominator.

    Returns:
        float: The result of a divided by b.
    """
    try:
        res = a / b
    except ZeroDivisionError:
        # Logging an exception message when division by zero is attempted
        # The exception Log also adds the traceback
        logger.exception('Trying to divide by 0')
    else:
        return res

# Test values
a = 10
b = 0

# Performing addition and division operations
add_result = add(a, b)
div_result = div(a, b)

# Logging debug messages to show the results of addition and division operations
logger.debug('Add: {} + {} = {}'.format(a, b, add_result))
logger.debug('Div: {} / {} = {}'.format(a, b, div_result))
