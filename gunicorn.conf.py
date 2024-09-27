import os

from dotenv import load_dotenv
from uvicorn_worker import UvicornWorker


bind = "0.0.0.0:8000"
workers = 4
worker_class = UvicornWorker


environment = os.getenv("ENVIRONMENT")
print(environment)
env = os.path.join(os.getcwd(), f"{environment}.env")
if os.path.exists(env):
    print(env)
    load_dotenv(env)

print(os.getenv("YANDEX_CLIENT_ID"))
