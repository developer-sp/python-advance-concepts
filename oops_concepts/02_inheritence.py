'''
---------------------------- Inheritence -------------------------------
- Inheritance is defined as creating a new class by extending an existing class.
- From a Base Class, we create a new class called Dervied Class. Base Class
is called called Super Class

------- Why Inheritence

- When different classes require same components, we can create one class for that
component and create different derived classes
- And updating the common code in Base Class will update all the derived classes, 
hence removing the need to update code in each class separately
'''

class BaseClass:
    def __init__(self, value):
        self.base_value = value
        # creating a private attribute
        # these are not transferred to derived class
        self.__my_private_attribute = 20

class DerivedClass(BaseClass):
    def __init__(self, value):
        # if we do not initialize the BaseClass, we cannot
        # use its attributes
        BaseClass.__init__(self, value)

derived_class = DerivedClass(12)
print("Accessing BaseClass Value: ",derived_class.base_value)

try:
    print("Accessing BaseClass Private Value:",derived_class.__my_private_attribute)
except Exception as e:
    print(e) # 'DerivedClass' object has no attribute '__my_private_attribute'

# Private Attributes / Methods can be accessed via name mangling
print("Accessing BaseClass Private Value:",derived_class._BaseClass__my_private_attribute)

# More on the above in name_mangling.py

# --------------- Overiding Attributes ------------------
class BaseClass:
    def __init__(self, value):
        self.base_value = value

class DerivedClass(BaseClass):
    def __init__(self, value):
        BaseClass.__init__(self, value)
        
        self.base_value = 2*value

derived_object = DerivedClass(10)

print(derived_object.base_value)

# --------------- Overiding Methods ------------------
class BaseClass:
    def __init__(self, value):
        self.base_value = value

    # static decorator tells that its a static method
    # this allows us to call the method without passing any parameters
    @staticmethod
    def print_hello():
        print("Henlo")

class DerivedClass(BaseClass):
    def __init__(self, value):
        BaseClass.__init__(self, value)

    # overriding the base class
    @staticmethod
    def print_hello():
        print("No Henlo")
    
    # creating function without static method
    def print_hello_2():
        print("No Henlo 2")

    # creating func without static but with self
    def print_hello_3(self):
        print("Henlo 3")

derived_object = DerivedClass(10)

derived_object.print_hello()

# This gives an error, Because calling .print_hello_2() with dervied_object
# will pass the "self", i.e. the object itself to the print_hello_2() function
# but the print_hello_2() doesn't expect any arguments, hence it will fail
# this is the reason we use @staticmethod()
try:
    derived_object.print_hello_2()
except Exception as e:
    print(e)
    # DerivedClass.print_hello_2() takes 0 positional arguments but 1 was given
    # Implies calling the above will pass derived_object i.e. "self" to the func

# this works because in class definition, the function takes self as parameter
derived_object.print_hello_3()


# ---------------------------- Types of Inheritence ---------------------

# There are many types of inheritence. Above, we saw single inheritence

# ----------------------------- Multiple Inheritence --------------

class BaseClass1:
    def __init__(self,val):
        self.val = val

class BaseClass2:
    def __init__(self,val):
        self.val = val

class DerviedClassMixed(BaseClass1, BaseClass2):
    def __init__(self):
        BaseClass1.__init__(self, 10)
        BaseClass2.__init__(self, 20)

# the above and below are different
# if both base classes have same function, then if we run the function
# from derived class, the function of the base class that appeared first
# in class definition will run. Here it will be BaseClass2's function
class DerviedClassMixed2(BaseClass2, BaseClass1):
    def __init__(self):
        BaseClass1.__init__(self, 10)
        BaseClass2.__init__(self, 20)

derived_mixed = DerviedClassMixed()

# -------------------------- Multi-Level Inheretence ------------------
class BaseClass:
    pass 

class DerivedClass(BaseClass):
    pass

class DerivedDerivedClass(DerivedClass):
    pass 

# -------------------------- Hierarchical Inheritence --------------------
# This is, when multiple classes inherit from same parent

class BaseClass:
    pass 

class DerivedClass1(BaseClass):
    pass

class DerivedClass2(BaseClass):
    pass

# --------------------- Diamond Inheritence -----------------------
# Its called diamond because it creates biamon shaped inheritence hierarchy
# So its a hierarchical followed by multiple inheritence

class BaseClass:
    pass 

class DerivedClass1(BaseClass):
    pass

class DerivedClass2(BaseClass):
    pass

class FinalClass(DerivedClass1, DerivedClass2):
    pass
