from pydantic import BaseModel, UUID4
from typing import List


class ShoppingCart(BaseModel):
    id: UUID4 = None
    customer_number: int
    item_ids: List[int] = []
