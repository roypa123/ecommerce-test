from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers.user import router as user_router
from app.routers.category import router as category_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(user_router)
app.include_router(category_router)

@app.get("/")
def root():
    return {"message":"Hello World"}