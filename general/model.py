from sqlmodel import Field, SQLModel
from db import create_db_and_tables

class General(SQLModel, table=True):
    id : int | None = Field(default=None, primary_key=True)
    name : str | None = Field(max_length=300)
    m_type : str | None = Field(max_length=300)
    year : int | None = Field(default=None)
    rating : int | None = Field(default=None)
    image : str 
    download_link : str
    
create_db_and_tables()