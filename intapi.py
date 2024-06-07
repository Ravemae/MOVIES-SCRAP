from fastapi import APIRouter
from international.session import get_all_movies, add_movie
from international.schema import International
from fastapi import HTTPException

router = APIRouter()

@router.get("/all")
async def all_movies():
    movie = await get_all_movies()
    if not movie:
        return HTTPException(status_code=404, message = "Movies not found")
    return movie

@router.post('/add-movie')
async def add(international: International):
    data = await add_movie(international.name, international.image, international.date, international.download_link, international.description)
    if data:
        return data
    else:
        return HTTPException(status_code=404, message="Movie unable to add")
    