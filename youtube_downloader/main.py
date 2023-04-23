import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from youtube_downloader.models import Item

# You can give your API a title and add additional metadata such as a description, version number, etc.
# The description also supports markdown formatting.
app = FastAPI(
    title="Youtube Downloader",
    description="Youtube Downloader API using **yt-dlp** and **ytdl-sub**",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


items = {
    0: Item(id="SUelbSa-OkA"),
    1: Item(id="SORiTsvnU28"),
    2: Item(id="fZUluo9vUNw"),
}


@app.get("/")
def index():
    return "Dummy api index"


@app.get("/items/{item_id}")
def query_item_by_id(item_id: int) -> Item:
    if item_id not in items:
        HTTPException(status_code=404, detail=f"Item with {item_id=} does not exist.")

    return items[item_id]


@app.post("/items")
def add_item(item: Item) -> dict[str, Item]:
    if item.id in items:
        HTTPException(status_code=400, detail=f"Item with {item.id=} already exists.")

    items[item.id] = item
    return {"added": item}


# The 'responses' keyword allows you to specify which responses a user can expect from this endpoint.
@app.put(
    "/items/{item_id}",
    responses={
        404: {"description": "Item not found"},
        400: {"description": "No arguments specified"},
    },
)
def update_item():
    return "Update item"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
