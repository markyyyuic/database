from fastapi import FastAPI
from routers.testing import testing

app = FastAPI()


app.include_router(testing)


