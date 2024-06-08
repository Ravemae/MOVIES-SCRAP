from fastapi import FastAPI
from intapi import router
from kdramaapi import route

app = FastAPI()
def internationals():
    app.include_router(router)
def kdrama():
    app.include_router(route)

kdrama()




