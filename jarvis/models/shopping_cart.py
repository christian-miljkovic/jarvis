from pydantic import BaseModel, UUID4
from typing import List
from jarvis.models import CartItem


class ShoppingCart(BaseModel):
    id: UUID4 = None
    customer_phone_number: int = None
    item_ids: List[CartItem] = []
