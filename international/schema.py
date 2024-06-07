from pydantic import BaseModel


class International(BaseModel):
    name : str
    date : str
    download_link : str
    image: str
    description: str
