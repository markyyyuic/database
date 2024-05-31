from fastapi import FastAPI, APIRouter


testing = APIRouter(tags=["testing"])


@testing.get("/items/")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
