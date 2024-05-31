from fastapi import FastAPI, APIRouter


testing3 = APIRouter(tags=["testing3"])


@testing3.get("/sad/")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
