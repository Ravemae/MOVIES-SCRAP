from pydantic import BaseModel


class kdrama(BaseModel):
    name : str
    date : str
    description : str
    image_link: str
    url: str