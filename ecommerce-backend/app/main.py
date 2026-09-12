from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.routers.user import router as user_router
from app.routers.category import router as category_router
from app.routers.product import router as product_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




app.include_router(user_router)
app.include_router(category_router)
app.include_router(product_router)

@app.get("/")
def root():
    return {"message":"Hello World"}