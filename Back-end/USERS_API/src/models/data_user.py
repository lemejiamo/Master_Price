from datetime import datetime
from typing import Union
from pydantic import BaseModel, EmailStr, Field


class TokenCreateModel(BaseModel):
    email: Union[EmailStr, None]
    user_id: Union[str, None]
    name: Union[str, None]


class TokenCheckModel(BaseModel):
    login_token: Union[str, None]


class LoginModel(BaseModel):
    email: Union[EmailStr, None]
    password: Union[str, None]


class ChangePasswordModel(LoginModel):
    new_password: Union[str, None]


class UserModel(BaseModel):
    name: Union[str, None] = Field()
    email: Union[EmailStr, None] = Field()
    cel: Union[str, None]
    password: Union[str, None]
    date_create: Union[str, None]
    updated: Union[str, None]
    category: Union[str, None] = 'user'