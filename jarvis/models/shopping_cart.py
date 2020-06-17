from pydantic import BaseModel, UUID4
from typing import List
from jarvis.models import CartItem


class ShoppingCart(BaseModel):
    customer_phone_number: int = None
