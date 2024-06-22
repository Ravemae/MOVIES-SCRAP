from pydantic import BaseModel


class General(BaseModel):
    name : str
    m_type : str 
    year : int 
    rating : int 
    download_link : str
    image: str