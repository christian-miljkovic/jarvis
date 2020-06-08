from pydantic import BaseModel, Field, validator


class CartItem(BaseModel):
    name: str = None
    item_type: str = None
    quantity: str = Field(None, alias="Field_quantity_Value")
    beer_name: str = Field(None, alias="Field_beer_Value")
    beer_type: str = Field(None, alias="Field_beer_Type")
    wine_name: str = Field(None, alias="Field_wine_Value")
    wine_type: str = Field(None, alias="Field_wine_Type")
    liquor_name: str = Field(None, alias="Field_liquor_Value")
    liquor_type: str = Field(None, alias="Field_liquor_Type")

    @validator("quantity")
    def valid_quantity(cls, v):
        if int(v) < 1:
            raise ValueError("quantity cannot be less than one")
        return v
