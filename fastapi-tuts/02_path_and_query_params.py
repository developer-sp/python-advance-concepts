from fastapi import FastAPI, Query, Path
from typing import Union

# Initialize FastAPI app
app = FastAPI()

# GET endpoint demonstrating both path and query parameters
@app.get("/items/{item_id}")
def get_item(
    item_id: int = Path(..., description="The ID of the item to retrieve"),  # Path parameter with validation
    q: Union[str, None] = Query(None, max_length=50, description="Search query string")  # Optional query parameter
):
    # Returns the item ID and optional query string "q" if provided
    return {"item_id": item_id, "query": q}

# GET endpoint with multiple query parameters for pagination
@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, page: int = 1, page_size: int = 10):
    # "user_id" is a path parameter, while "page" and "page_size" are query parameters
    return {"user_id": user_id, "page": page, "page_size": page_size}
