from fastapi import FastAPI
from intapi import router
from kdramaapi import route

app = FastAPI()

app.include_router(router)




