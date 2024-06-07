from sqlmodel import Field, SQLModel
from db import create_db_and_tables

class International(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    name : str | None = Field(max_length=300)
    image : str 
    date : int | None = Field(default=None)
    download_link : str
    description: str 
    
create_db_and_tables()