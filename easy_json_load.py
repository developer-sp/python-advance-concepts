"""
Python's SimpleNamespace is a utility for creating simple object types. 
It's part of the types module in the Python Standard Library and provides a way to quickly and simply create a "dot notation" namespace for a collection of attributes.
"""

import json
from pydantic import BaseModel
from types import SimpleNamespace


eg_json = """{
    "point_one": {
        "x":6,
        "y":7
    },
    "point_two": {
        "x":20,
        "y":3,
        "z":51.0
    }
}"""

# -------------------------------------------------- Method 1 - JSON Load -------------------------------------------------------

data = json.loads(eg_json)  # converts to dictionary
print("x:", data["point_one"]["x"])

# we see that we have to use the dictionary method to get the values from the data json
# this will be problamatic when the json contains many nested objects and we have to fetch the inner values
# one good solution for this will be the (.) dot notation

# ------------------------------------------------- Method 2 - Pydantic -----------------------------------------------------


class Point_X(BaseModel):
    x: int
    y: int


class Point_Y(BaseModel):
    x: int
    y: int
    z: float


class Points(BaseModel):
    point_one: Point_X  # expects a dictionary with name point_one
    point_two: Point_Y


# print(Point_One.model_validate_json("""{"x":5, "y":10}"""))
# print(Point_Two.model_validate_json("""{"x":5, "y":10, "z":10}"""))
# print(
#     Points.model_validate_json(
#         """{"point_x":{"x":5, "y":10}, "point_y":{"x":5, "y":10, "z":10}}"""
#     ).point_x
# )

data = Points.model_validate_json(eg_json)
print("x:", data.point_one.x)

# this is a good approach where we can access the inner values with dot (.) notation
# but we have to setup 3 classes and this is an overhead

# -------------------------------------------------- Method 3 - SampleNamespace --------------------------------------------------

# Sample namespace converts a dictionary into am object with quick access to the attributes with dot notation

sample_dict = {
    "circle": 5,
    "rectangle": 10,
}

data = SimpleNamespace(**sample_dict)
print("Length:", data.rectangle)

# data.length = 17 can alter the values


sample_dict = {
    "circle": {"radius": 5, "circumference": 10},
    "rectangle": {"length": 11, "bread": 20},
}

data = SimpleNamespace(**sample_dict)
# print("Length:", data.rectangle.length) doesnt work, it doesnt nest
print("Length:", data.rectangle["length"])

# what if the key has (.)s or spaces

sample_dict = {
    "circle radius": 5,
    "rectangle.length": 10,
}

data = SimpleNamespace(**sample_dict)
# print("Length:", data.rectangle.length) throws error
print(
    "Length:", getattr(data, "rectangle.length")
)  # it works because SimpleNamespaces creates an obj and obj have setattr getattr
print("Radius:", getattr(data, "circle radius"))

# we can alter the values
setattr(data, "rectangle.length", 12)
print("Length:", getattr(data, "rectangle.length"))

# now trying on the json
# the object_hook will recursivly call each object in the json and each of that object is converted to SimpleNamespace Object
data = json.loads(eg_json, object_hook=lambda x: SimpleNamespace(**x))
print("z:", data.point_two.z)

# this also works if the json keys have dots(.) or spaces in it, we can use getattr and setattr
