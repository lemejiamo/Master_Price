from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel, EmailStr, Field


class Users(BaseModel):
    name: Union[str, None] = Field()
    email: Union[str, None] = Field()
    cel: Union[str, None]
    password: Union[str, None]
    type: Union[int, None] = 1  # 1 standar User 2 Company
    date_load: Union[str, None]
    date_update: Union[str, None]


class UpdatePassword(BaseModel):
    email: Optional[Union[EmailStr, None]]
    password: Optional[Union[str, None]]
    new_password: Optional[Union[str, None]]
    date_update: Optional[Union[datetime, None]]
