from datetime import datetime
from typing import Union
from pydantic import BaseModel, EmailStr, Field


class Store(BaseModel):
    name: Union[str, None] = Field()
    email: Union[EmailStr, None]
    location: Union[str, None]
    address: Union[str, None]
    user_id: Union[str, None]
    company_id: Union[str, None]
    date_create: Union[datetime, None]
    updated: Union[datetime, None]