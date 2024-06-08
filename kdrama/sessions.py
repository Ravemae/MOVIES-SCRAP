from .db import engine
from sqlmodel import Session, select
from .model import Kdrama


def add_movie(name, date,description, image_link, url):
    with Session(engine) as session:
        kdrama = Kdrama(name=name, date=date , description=description, image_link=image_link , download_link=url)
        session.add(kdrama)
        session.commit()
        return "Movie added to database"

      
def get_all_movies():
    with Session(engine) as session:
        movie = select(Kdrama)
        results = session.exec(movie).all()
        return results

    

    

def update_movie(id,name= None, date= None,description= None, image_link=None, url=None):
    try:
        with Session(engine) as session:
            movie = session.get(Kdrama, id)
            if movie:
                if name is not None:
                    movie.name = name
                elif image_link is not None:
                    movie.image_link = image_link
                elif date is not None:
                    movie.date = date
                elif url is not None:
                    movie.url = url
                elif description is not None:
                    movie.description = description
                else:
                    return "Field not found"
                session.commit()
                return f"Movie with id {id} updated"
            else:
                return f"No movie found with id {id}"
    except Exception as e:
        return f"Error in updating Movie: {e}"   

def delete_movie(id):
    with Session(engine) as session:
        movie = session.get(Kdrama, id)
        session.delete(movie)
        session.commit()
        return f"{movie} deleted"










