from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI()

# Basic GET endpoint at the root ("/") route
@app.get("/")
def read_root():
    # Returns a simple JSON response
    return {"message": "Welcome to FastAPI!"}

# GET endpoint with a path parameter
@app.get("/hello/{name}")
def say_hello(name: str):
    # Path parameter "name" is taken from the URL
    return {"message": f"Hello, {name}!"}

# POST endpoint to create an item
@app.post("/items/")
def create_item(item: dict):
    # Accepts a JSON object as the body of the request
    return {"received_item": item}

# PUT endpoint to update an item with query parameters
@app.put("/update-item/")
def update_item(name: str, price: float):
    # Takes "name" and "price" as query parameters for updating an item
    return {"name": name, "price": price}

# DELETE endpoint to delete an item with a path parameter
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    # Path parameter "item_id" specifies which item to delete
    return {"message": f"Item with ID {item_id} deleted."}
