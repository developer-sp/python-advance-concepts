"""
------------------------------- Name Mangling ------------------------------

Name mangling in Python is a technique used to protect class-private attributes from being accidentally overridden or accessed in subclasses. 
This is achieved by prefixing the attribute name with two underscores (__). 
Python internally changes the name of the attribute by adding a _ClassName prefix to it. This process is called "name mangling."

To make the private variables and methods less accessible from outside the class, Python uses a technique called name mangling. 
When a variable or method name is prefixed with double underscores, Python internally changes the name to include the class name, 
making it harder to accidentally access it from outside the class.

For example, if you have a private variable named __private_variable in a class MyClass, 
Python will internally change its name to _MyClass__private_variable.
"""

# ---------------------------------- Single Class Example ---------------------------------------
print(
    "---------------------------------- Single Class Example ---------------------------------------\n"
)


class MyClass:
    def __init__(self):
        self.__private_attr = 42  # Name mangled attribute
        self.public_attr = 100

    def __private_method(self):  # Name mangled method
        print("This is a private method")


# Create an instance of the class
obj = MyClass()

# Attempt to access the private attribute
try:
    print("Trying to access __private_attr using obj.__private_attr")
    print(obj.__private_attr, "\n")
except AttributeError as e:
    print("Got an Error")
    print(e, "\n")  # This will raise an AttributeError

# Accessing the mangled name
print("Trying to access __private_attr using obj._MyClass__private_attr")
print(obj._MyClass__private_attr, "\n")  # Output: 42

# Attempt to call the private method
try:
    print("Trying to access __private_method() using obj.__private_method()")
    obj.__private_method()
except AttributeError as e:
    print("Got an Error")
    print(e, "\n")  # This will raise an AttributeError

# Calling the private method using the mangled name
print("Trying to access __private_attr using obj._MyClass__private_method")
obj._MyClass__private_method()  # Output: "This is a private method"

explanation = """
Explanation:
- __private_attr and __private_method are attributes that Python will mangle to _MyClass__private_attr and _MyClass__private_method.
- Attempting to access obj.__private_attr directly raises an AttributeError because the attribute name has been mangled.
- You can access the mangled attribute by using the full mangled name, _MyClass__private_attr.
- The same applies to methods, where obj._MyClass__private_method() successfully calls the method, whereas obj.__private_method() does not.
"""

print(f"\n {explanation} \n")

# ---------------------------------- Multi Class Example ---------------------------------------
print(
    "\n---------------------------------- Multi Class Example ---------------------------------------\n"
)


class ParentClass:
    def __init__(self):
        self.__private_attr = "Parent Private"  # Name mangled attribute
        self.public_attr = "Parent Public"

    def __private_method(self):  # Name mangled private method
        print("Parent's private method 1")

    def __private_method2(self):  # Name mangled private method 2
        print("Parent's private method 2")

    def get_private_attr(
        self,
    ):  # This will let us fetch the __private_attr of parent when passed to the child
        return self.__private_attr


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()
        self.__private_attr = "Child Private"  # Attempting to create a private attribute in the child class, that is trying to override parent's __private_attr
        self.public_attr = "Child Public"

    def call_parent_private_method(self):
        self.__private_method()  # calling parent's __private_method() in child
        # self._ParentClass__private_method() # calling the ParentClass's __private_method() with the mangled name will work

    def __private_method2(self):  # trying to override parent's __private_method2()
        print("Child's private method 2")


# Create an instance of the ChildClass
child = ChildClass()

# Accessing the public attribute
print("Accessing Child's public attr, child.public_attr")
print(child.public_attr, "\n")  # Output: "Child Public"

# Accessing the parent's private attribute using the method provided by ParentClass
print(
    "Accessing the parent's private attribute from child using the method provided by ParentClass"
)
print(child.get_private_attr(), "\n")  # Output: "Parent Private"

# Attempting to access the private attribute directly
try:
    print("Attempting to access Child's __private_attr the private attribute directly")
    print(child.__private_attr)
except AttributeError as e:
    print("Got an Error")
    print(e, "\n")  # This will raise an AttributeError

# Accessing the child class's private attribute using the mangled name
print(
    "Accessing the child class's private attribute .__private_attr using the mangled name child._ChildClass__private_attr"
)
print(child._ChildClass__private_attr, "\n")  # Output: "Child Private"

# Accessing the parent class's private attribute using the mangled name
print(
    "Accessing the child class's private attribute .__private_attr using the mangled name child._ParentClass__private_attr"
)
print(child._ParentClass__private_attr, "\n")  # Output: "Parent Private"

# Attempting to call the Parents's private method __private_method() directly from child
try:
    print(
        "Attempting to call the Parents's private method __private_method() directly from child child.call_parent_private_method"
    )
    child.call_parent_private_method()
except AttributeError as e:
    print("Got an Error")
    print(e)  # This will raise an AttributeError
    print(
        "To fix this, go to the ChildClass `def call_parent_private_method()` and change self.__private_method() to self._ParentClass__private_method() which is the mangled name\n"
    )

# Attempting to call the child's private method 2 directly
try:
    print("Attempting to call the child's private method __private_method2() directly")
    child.__private_method2()
except AttributeError as e:
    print("Got an Error")
    print(e, "\n")  # This will raise an AttributeError

# Calling the child's private method using the mangled name
print(
    "Attempting to call the child's private method 2 __private_method2() with mangled name child._ChildClass__private_method2()"
)
child._ChildClass__private_method2()  # Output: "Child's private method"

# Calling the parent's private method 2 using the mangled name
print(
    "\nAttempting to call the parent's private method __private_method2() with mangled name child._ParentClass__private_method2()"
)
child._ParentClass__private_method2()  # Output: "Parent's private method"

explanation = """
Key Points:

Name Mangling in Parent and Child Classes:

- The private attribute __private_attr in ParentClass is mangled to _ParentClass__private_attr.
- The private attribute __private_attr in ChildClass is mangled to _ChildClass__private_attr.
- This ensures that the two attributes do not interfere with each other, even though they have the same name in different classes.

Accessing Mangled Names:

- The mangled name of ParentClass's private attribute is accessible as _ParentClass__private_attr.
- Similarly, ChildClass's private attribute is accessible as _ChildClass__private_attr.

Method Overriding:

- The ChildClass can define its own version of __private_method, which does not interfere with the ParentClass's __private_method due to name mangling.

Accessing Private Members:

- Direct access to __private_attr or __private_method using the original names will raise an AttributeError.
- However, accessing them using their mangled names (e.g., _ChildClass__private_attr or _ParentClass__private_attr) works.

This example shows how name mangling helps prevent accidental access or modification of private attributes and methods, even in an inheritance hierarchy.
"""

print(f"\n{explanation}")


"""
Extra Information
“Private” instance variables that cannot be accessed except from inside an object, don’t exist in Python. 
However, there is a convention that is followed by most Python code: a name prefixed with an underscore (e.g. _spam) should be treated 
as a non-public part of the API (whether it is a function, a method or a data member). 
It should be considered an implementation detail and subject to change without notice.

Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), 
there is limited support for such a mechanism, called name mangling. Any identifier of the form __spam (at least two leading underscores, 
at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) 
stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.
"""
