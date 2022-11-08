from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, EmailStr, Field


class Users(BaseModel):
    name: Union[str, None] = Field()
    email: Union[str, None] = Field()
    cel: Union[str, None]
    password: Union[str, None]
    date_create: Union[str, None]
    updated: Union[str, None]
    category: Union[str, None] = 'user'


class UpdatePassword(BaseModel):
    email: Optional[Union[EmailStr, None]]
    password: Optional[Union[str, None]]
    new_password: Optional[Union[str, None]]
    date_update: Optional[Union[datetime, None]]
