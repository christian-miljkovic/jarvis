from pydantic import BaseModel, UUID4
from typing import Optional


class Item(BaseModel):
    id: UUID4 = None
    name: str = ""
    price: float = 0.0
    quantity: int = 0
    image_url: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
