from fastapi import FastAPI

from app import routers


app = FastAPI()


for route in routers:
    app.include_router(route)
