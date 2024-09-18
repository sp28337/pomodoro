from fastapi import FastAPI

from handlers import routers


app = FastAPI()


for route in routers:
    app.include_router(route)
