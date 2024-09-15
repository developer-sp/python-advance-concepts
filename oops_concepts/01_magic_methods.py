'''
Magic methods are methods that have double underscores at the beginning and end of their names. These are called dunder methods too

On a side note, the word “Dunder” is short for Double Underscore.
'''

# ---------------------------------------- __init__ Method ---------------------------------------------------

# The __init__ method is automatically called every time an object is instantiated. It is also called a class’ constructor.
# The primary purpose of the __init__ is to initialize the instance-level attributes (discussed above) of an object.

# ---------------------------------------- __new__ Method -------------------------------------------------------

# Most think that the __init__() magic method is responsible for creating a new object, i.e., allocating memory to it. but it aint true
# __init__() method does not allocate memory to the object when created, it only assigned values to the object's attributes
# Instead, Python invokes the __new__() method first to create a new object and allocate memory to it. Then __init__ is ran to assign values

# In what Scenarios can we use the Dunder Method?
# For instance, by implementing the __new__() method, you can apply data checks. 
# This ensures that your program allocates memory only when certain conditions are met.

# First, Python creates the object if the specified condition is true. Next, it instantiates the new object.
# If the condition is false, we can avoid an unnecessary memory allocation.
# Other common use cases involve defining singleton classes (classes with only one object)



from typing import Any


class Point3D:
    def __new__(cls, x, y, z):
    
        if isinstance(x, int) and isinstance(y, int) and isinstance(z, int):
            # Allocate memory and return a new object
            # only when the if-condition is True
            print("Creating the Object!")
            return super().__new__(cls) # Return new object
        else:
            raise ValueError("All of x, y and z must be integers")
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print("Object is Initialized!")

# Uncomment and Run this. We get an Error
# new_point = Point3D(1,2,'3')





# ------------------------------------------ __repr__ Method --------------------------------------------------------

# We use this dunder method to display what will be printed when we print the object
# We use the magic method to resolve this and generate a readable and useful representation 
# whenever an object is printed__repr__

# mostly used to print the object in a human readable / interpretable format
class Point4D:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        # here we return a personalized representation of the calling object
        return f"Point4D(w = {self.w}, x={self.x}, y={self.y}, z={self.z})"
    
my_point = Point4D(1,2,3,4)
print(my_point) 

# Without __repr__ the print statement would print something like
# <__main__.Point4D object at 0x779e309cfe00>





# ------------------------------------ __eq__ Method --------------------------------------------------

# We can implement this function to compare two objects. Let's say have a Point2D class with which we create 
# two objects having their own x and y values and we want to compare these values to see if the two objects
# are equal. Then we need to implement this method, else we cannot compare them

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other): # here other is the other object that we are comparing
        # the below will return true if self and the other object has some x and y values same
        return self.x == other.x and self.y == other.y
    
point1 = Point2D(1, 2)
point2 = Point2D(1, 2)
point3 = Point2D(2, 3)

print(point1 == point2) # True
print(point2 == point3) # False
# point1 == point2 is same as point1.__eq__(point2)

point1 = Point4D(1, 2, 3, 4)
point2 = Point4D(1, 2, 3, 4)

print(point1 == point2) # will return False even though they are same, as __eq__ is not implemented

# Why the above returns False?
#  If the two objects are distinct instances but with the same attributes, the default behavior when comparing them using == is 
# to check if they are the same objects in memory.

# As they are different objects, they will be considered different, and hence we get the output False.
# We can print their memory locations

print(id(point1))
print(id(point2))

# To resolve this, we define the __eq__ method in Python classes. As the name suggests, 
# it allows us to define the conditions for comparing two objects using ==.






# --------------------------------------- __call__ Method ------------------------------------------- 

# The objective of this dunder method is to make a class object callable, i.e., behave like a function.
# This magic method allows you to define the behavior of the class object when it is invoked like a function (like this: object()).

class Greeting:
    def __init__(self, greeting_words):
        self.greeting_words = greeting_words 

    def __call__(self, user_name):
        print(f"{self.greeting_words} {user_name}")
    
hello_greeting = Greeting(greeting_words="Hola")

# we can now call the hello_greeting as a function
hello_greeting("Lucifer") # Hola Lucifer

# we can check if our object is callable
print(callable(hello_greeting))
# In a gist, the callable() method in Python is a built-in function that returns True if the object 
# passed as an argument can be invoked like a function, and False otherwise




# ----------------------------------------- __add__ Method -----------------------------------------------
# __add__ magic method is used to define the behavior of the + operator for a class’ objects.

# Thus, when the + operator is used between two objects, Python automatically calls the __add__ method of the 
# left-hand operand object and passes the right-hand operand object as an argument.

# In this similar fashion, there are other arithmetic dunder methods like __sub__, __mul__, __div__ 
# which work in similar fashion

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y

        return Point2D(new_x, new_y)
    
    def __repr__(self) -> str:
        return f'Point2D(x={self.x}, y={self.y})'
    
point1 = Point2D(1, 2)
point2 = Point2D(3,4)
point3 = point1 + point2
# the above is same as the below, the above gets converted to below
# point3 = point1.__add__(point2)

print(point1)
print(point2)
print(point3)




# ----------------------------------------- __contains__ Method -----------------------------------------------
# When you use "in", under the hood, Python looks for the __contains__ method in the class implementation of the object and executes it.
# Thus, when dealing with user-defined classes, the __contains__ magic method allows you to define the behavior of the "in" operator 
# for objects of a class.

# When the in operator is used with an object, Python invokes the __contains__ method and passes the operand as an argument.
class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        
class Company:
    def __init__(self, employees):
        self.employees = employees

    # this method lets us check if an employee is a part of that company or not
    def __contains__(self, employee):
        for emp in self.employees:
        
            # Match Name and Designation
            match_name  = (emp.name  == employee.name)
            match_designation = (emp.designation == employee.designation)
            
            if match_name and match_designation:
                return True
                
        return False
    
emp1 = Employee('Luci','FrontEnd')
emp2 = Employee('Dave','BackEnd')
emp3 = Employee('Gan','FullStack')

company = Company([emp1, emp2, emp3])

# Let's search if this person is a part of that employee
search_employee = Employee('Luci','FrontEnd')

if search_employee in company: # here, the __contains__() is invoked
    print(search_employee.name, "is a part of that company")
else:
    print(search_employee.name, "is not a part of that company")

# Let's search if this person is a part of that employee
search_employee = Employee('Caren','FullStack')

if search_employee in company: # here, the __contains__() is invoked
    print(search_employee.name, "is a part of that company")
else:
    print(search_employee.name, "is not a part of that company")

# -------- We can also use "not in" -----------------
# Let's search if this person is not a part of that employee
search_employee = Employee('Fisher','FullStack')

if search_employee not in company: # here, the __contains__() is invoked
    print(search_employee.name, "is not a part of that company")
else:
    print(search_employee.name, "is a part of that company")



# ------------------------------------ __bool__ method -------------------------------------------------------
# We can use this dunder method is to determine whether the object evaluates to True or False.

# Let's implement this for our Company class which lets us check if the Company has any employees or not
# The __bool__ method is extremely useful when you want to define the criteria to determine the truth value of your custom objects.

class Employee:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        
class Company:
    def __init__(self, employees=[]):
        self.employees = employees

    def __bool__(self):
        if len(self.employees) == 0:
            return False        
        return True
    
emp1 = Employee('Luci','FrontEnd')
emp2 = Employee('Dave','BackEnd')
emp3 = Employee('Gan','FullStack')

company = Company([emp1, emp2, emp3])

if company: # internnaly runs company.__bool__()
    print('Company has employees')
else:
    print('Company has no employees')

# Let's define another company with no employees
company_another = Company()

if company_another:  # internnaly runs company_another.__bool__()
    print('Company has employees')
else:
    print('Company has no employees')

# --------- Note --------------

# internally, when we say "if any_object", python checks if it implements __bool__() and if it does, then it calls that
# if the object doesnt implement bool, it checks if it implements __len__(), if it does, then it calls that, and if
# __len()__ returns 0, the "if any_object" evaluates to True and if its non zero, then it evaluates to False. And finally
# if it neither implements __bool__() nor implements __len__(), then it simply returns True

# example of object that has no __bool__() and no __len__(), thus it evaluates to truer

emp = Employee('Lucira','PyDev')

if emp:
    print("Employee") # this is printed 
else:
    print("Not an Employee")