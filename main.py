from fastapi import FastAPI
from intapi import router

app = FastAPI()

app.include_router(router)

