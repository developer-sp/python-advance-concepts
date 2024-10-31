from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

# Initialize FastAPI app
app = FastAPI()

# Pydantic model to define the structure and validation of an Item
class Item(BaseModel):
    name: str
    price: float

# In-memory database (dictionary) to store items
items_db: Dict[int, Item] = {}

# POST endpoint to create an item
@app.post("/items/{item_id}", status_code=201)
def create_item(item_id: int, item: Item):
    if item_id in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[item_id] = item  # Store item in the in-memory database
    return {"item_id": item_id, "item": item}

# GET endpoint to read an item
@app.get("/items/{item_id}")
def read_item(item_id: int):
    item = items_db.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# PUT endpoint to update an item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    items_db[item_id] = item  # Update item in the database
    return item

# DELETE endpoint to delete an item
@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_id]  # Remove item from the database
    return {"message": "Item deleted"}
