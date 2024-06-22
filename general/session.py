from db import engine
from model import General
from sqlmodel import Session, select

def add_movie(name, m_type, year, rating, image, download_link):
    try:
        with Session(engine) as session:
            movie = General(name=name, m_type=m_type, year=year, rating=rating, image=image, download_link=download_link)
            session.add(movie)
            session.commit()
            print(f"Movie added to database: {name}")
            return "Movie added to database"
    except Exception as e:
            print(f"Error in adding Movie: {e}")
            return f"Error in adding Movie: {e}"

def get_all_movies():
    with Session(engine) as session:
        movie = select(General)
        results = session.exec(movie).all()
        return results

def update_movie(id, name=None, m_type=None, year=None, rating=None, image=None, download_link=None):
    try:
        with Session(engine) as session:
            movie = session.get(General, id)
            if movie:
                if name is not None:
                    movie.name = name
                if m_type is not None:
                    movie.m_type = m_type
                if year is not None:
                    movie.year = year
                if rating is not None:
                    movie.rating = rating
                if image is not None:
                    movie.image = image
                if download_link is not None:
                    movie.download_link = download_link
                session.commit()
                print(f"Movie with id {id} updated")
                return f"Movie with id {id} updated"
            else:
                return f"No movie found with id {id}"
    except Exception as e:
        print(f"Error in updating Movie: {e}")
        return f"Error in updating Movie: {e}"

def delete_movie(id):
    with Session(engine) as session:
        movie = session.get(General, id)
        if movie:
            session.delete(movie)
            session.commit()
            print(f"{movie} deleted")
            return f"{movie} deleted"
        else:
            return f"No movie found with id {id}"
