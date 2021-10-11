from fastapi import FastAPI
from config.database import engine
from config.database import Base
from auth import authrouter
from users import usersrouter
from location import locationrouter
from product import productrouter
from productmovement import productmovrouter

Base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get("/")
def hello():
    return "Hello"


app.include_router(authrouter.router)
app.include_router(usersrouter.router)
app.include_router(locationrouter.router)
app.include_router(productrouter.router)
app.include_router(productmovrouter.router)
