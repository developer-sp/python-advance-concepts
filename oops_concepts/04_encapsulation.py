'''
Encapsulation in OOP refers to bundling the data and the methods of a class within a single unit. 
This way, we keep the internal workings of an object hidden from the outside world.
'''

class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def calc(self, x):
        return self.a*(x**2) + (self.b)*x + self.c
    

# Encapsulation provides an interface to access the required variable/method without providing 
# full-fledged access to all variables of a class to the program.

# For instance, to evaluate the above quadratic, one has to only interact with 
# the calc() method and provide the input x.

quad = Quadratic(1, 2, 4)
print(quad.calc(2))

# A major benefit of encapsulation is that it also allows us to add a layer of security to the class objects.
# This is done by programmatically restricting access to certain components of an object, 
# such as its attributes and methods, and only exposing the necessary parts to the outside world.
# We do this to ensure that the objects and the data they hold are secure, maintainable, and easy to use.

# ---------- Why encapsulation? ------------------
# Encapsulation came as a response to enabling data protection support in software programs and creating appropriate protocols for data access.
# Traditional programming and object-oriented programming without appropriate encapsulation lacked data protection. 
# Thus, it allowed programs to access and modify data directly from outside the class or module.
# Consequently, limited data protection made it difficult to ensure that the data was valid and consistent across the entire program.

# Data protection is achieved by declaring what methods and attributes can be accessed from outside the class 
# and what not using the private, protected and public members. These are called access modifiers


# --------------------- Access Modifiers -----------------------
class MyClass:
    def __init__(self):
    
        self.public_attr     = "I'm public attribute"    ## 0 underscore prefixes
        self._protected_attr = "I'm protected attribute" ## 1 underscore prefix
        self.__private_attr  = "I'm private attribute"   ## 2 underscore prefixes
        
    def public_method(self):           ## 0 underscore prefixes
        return "I'm public method" 
        
    def _protected_method(self):       ## 1 underscore prefix
        return "I'm protected method"
        
    def __private_method(self):        ## 2 underscore prefixes
        return "I'm private method"
    
#1) Public
# Public members are accessible from anywhere in the program. 
# In Python, all class members are public by default. They are also inherited by child classes.
# these can be accessed outside the class

my_obj = MyClass()          ## create object

print("Printing Public Attribute and Methods")
print(my_obj.public_attr)      ## access attribute
print(my_obj.public_method())  ## access method 

# 2) Protected
# The theoretical notion behind protected members is that these members should only be accessible 
# within the class and all its child classes, as illustrated below:

class MyClass:
    def __init__(self):
        self._protected_attr = "I'm protected attribute"
        
    def _protected_method(self):
        return "I'm protected method"

my_obj = MyClass()          ## create object

print("\nPrinting Protected Attribute and Methods")
print(my_obj._protected_attr)      ## access attribute
print(my_obj._protected_method())  ## access method 

# ----- What's the Difference ? We are able to access it outside too ? -----
# The creation and accessibility of protected members in Python are purely based on conventions.
# In other words, even though protected members can be accessed like public members, it’s only by convention 
# that a variable declared with a single underscore prefix shouldn’t be used outside the class.
# What’s more, the declaration of a protected member is typically used to convey to other users that its 
# use should only be limited to the class and its child class(es).

# 3) Private
# The theoretical notion behind private members is that these members should only be 
# accessible within the class. In Python, private members are denoted by a double underscore (__) prefix 
# before the member name, as demonstrated below:

class MyClass:
    def __init__(self):
        self.__private_attr = "I'm private attribute"
        
    def __private_method(self):
        return "I'm private method"

my_obj = MyClass()          ## create object

print("\nPrinting Private Attribute and Methods")
try:
    print(my_obj.__private_attr)      ## access attribute
    print(my_obj.__private_method())  ## access method 
except Exception as e:
    print(e)
# 'MyClass' object has no attribute '__private_attr'

# passing to a child class

class MySubclass(MyClass):
    def __init__(self):
        super().__init__()
        
    def access_parent_attr(self):
        print(self.__private_attr)
        
    def access_parent_method(self):
        print(self.__private_method())

my_obj = MySubclass()          ## create object

print("\nPrinting Private Attribute and Methods through Child Class")
try:
    print(my_obj.access_parent_attr())      ## access attribute
    print(my_obj.access_parent_method())  ## access method 
except Exception as e:
    print(e)
# 'MySubclass' object has no attribute '_MySubclass__private_attr'

# ------------ Private Attributes can be only Accessed via Name Mangling.--------------------
# More on Name Mangling in the name_mangling.py


# ------------------ Final Notes --------------------------
# 1. Although private members (declared with a double underscore prefix: __member) can be accessed anywhere in the program 
# using name mangling, they should be accessed only within the class that defined it.

# 2. Protected members (declared with a single underscore prefix: _member) can be accessed anywhere in the program directly with their name. 
# However, they should be accessed only within the class that defined it and its subclasses.