from datetime import datetime
from typing import Union

from pydantic import BaseModel, Field


class Company(BaseModel):
    name: Union[str, None] = Field()
    location: Union[str, None]
    email: Union[str, None] = Field()
    telephone: Union[int, None]
    cellphone: Union[str, None]
    rating: Union[int, None]
    date_create: Union[datetime, None]
    updated: Union[datetime, None]