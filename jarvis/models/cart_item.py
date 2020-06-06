from pydantic import BaseModel


class CartItem(BaseModel):
    name: str = ""
    item_type: int
