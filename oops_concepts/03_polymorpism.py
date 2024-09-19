'''
Polymorphism in programming is defined as an object’s ability to take many forms.

Thus, the essence of Polymorphism is to define methods in a way that they 
can provide a common interface for objects of different class types or data types.

Why Poly?

Polymorphism came as a response to improving the flexibility, extensibility, 
and reusability of code.

Overall, Polymorphism promises to offer flexible and reusable code, as 
different types of objects can be passed and used interchangeably, 
without worrying about the underlying implementation – simplifying the 
design of complex systems.
'''

# Example is a len()

# it works for string
print(len("hello"))

# it works for lists
print(len([1,2,3]))

# This is the essence of polymorphism. Able to reuse code without any reimplementation
# and do not worry about how it handles data of different types, this
# no need to write specific implementation for each type of object

# --------------------- Poly Morphism in OOPs -------------------

# 1. Method Overloading
# Its the ability of a single func to accept different num / types of args

# But Python Does not Support Method Overloading. Example

def add(a: int, b: int) -> int:
    print("int add")
    return a + b

def add(a: str, b: str) -> str:
    print("str add")
    return a + b

# Both of them print "str add"  This is because the Python interpreter considers 
# only the latest definition of a method, even if you overload.
add(1,2)

add('1','2')

# But in C++ we can do like void add(int a, int b) and void add(double a, double b)
# to create two functions, which can take two different types

# But we can do other method overloading, like passing extra parameters

def add(a, b, c=0):
    return a + b + c

# so we can use the above function for both just two i/ps or3 i/ps
print(add(1, 2))
print(add(1,2,3))

# we can apply this same concept to class when defining methods


# 2. Method OVerriding
# We have seen this in inhertience, where the derived class overrides
# the method defined parent class
# Method overriding allows for more specialized behaviour for subclasses
# and is acrucial aspect of polymorphism

class Animal:
    def sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("The dog barks")

class Cat(Animal):
    def sound(self):
        print("The cat meows")
