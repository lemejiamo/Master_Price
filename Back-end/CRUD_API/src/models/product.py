from datetime import datetime
from typing import Union
from pydantic import BaseModel, Field


class Products(BaseModel):
    name: Union[str, None] = Field()
    email: Union[str, None]
    price: Union[int, None]
    measure_unity: Union[str, None]
    category: Union[str, None]
    user_id: Union[str, None]
    store_id: Union[str, None]
    date_create: Union[datetime, None]
    updated: Union[datetime, None]