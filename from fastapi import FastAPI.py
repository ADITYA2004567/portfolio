from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI app
app = FastAPI()

# A class to define how our item data looks
class Item(BaseModel):
    name: str
    description: str = None

# In-memory "database"
items = []

# Home route
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Get all items
@app.get("/items")
def get_items():
    return items

# Add a new item
@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return {"message": "Item added successfully", "item": item}
