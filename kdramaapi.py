from fastapi import APIRouter
from kdrama.sessions import get_all_movies, add_movie
from fastapi import HTTPException
from kdrama.schemas import kdrama


route = APIRouter()

@route.get("/all")
def all_movies():
    movies =  get_all_movies()
    if not movies:
        return HTTPException(status_code=404, message= 'No movies')
    return movies

@route.post('/add-movie')
async def addmovie(kdrama : kdrama):
    kdrama = await add_movie(kdrama.name, kdrama.date, kdrama.description, kdrama.image_link, kdrama.url)
    if not kdrama:
        return HTTPException(status_code=404, message="Movie not added successfully") 
    else:
        return kdrama

        
    


