from pydantic import BaseModel, Field, UUID4, validator
from jarvis.models import Beer, Liquor, Wine
from typing import Union


class CartItem(BaseModel):
    name: str = None
    item_type: Union[Beer, Liquor, Wine] = None
    quantity: str = Field(..., alias="Field_quantity_Value")
    beer_name: str = Field(..., alias="Field_beer_Value")
    wine_name: str = Field(..., alias="Field_wine_Value")
    liquor_name: str = Field(..., alias="Field_liquor_Value")

    @validator("quantity")
    def valid_quantity(cls, v):
        if int(v) < 1:
            raise ValueError("quantity cannot be less than one")
        return v
