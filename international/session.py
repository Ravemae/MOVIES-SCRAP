from .db import engine
from .model import International
from sqlmodel import Session, select


async def add_movie(name, image, date, download_link, description):
    try:
        with Session(engine) as session:
            movie = await International(name=name, image=image, date=date, download_link=download_link, description=description)
            session.add(movie)
            session.commit()
            return "Movie added to database"
    except Exception as e:
            return f"Error in adding Movie: {e}"
        
async def get_all_movies():
    with Session(engine) as session:
        movie = await select(International)
        results = session.exec(movie).all()
        return results
        
    
get_all_movies()
    

def update_movie(id, name=None, image=None, date=None, download_link=None, description=None):
    try:
        with Session(engine) as session:
            movie = session.get(International, id)
            if movie:
                if name is not None:
                    movie.name = name
                elif image is not None:
                    movie.image = image
                elif date is not None:
                    movie.date = date
                elif download_link is not None:
                    movie.download_link = download_link
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
        movie = session.get(International, id)
        session.delete(movie)
        session.commit()
        return f"{movie} deleted"