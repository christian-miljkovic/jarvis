from fastapi import APIRouter, Depends
from jarvis.db.database import DataBase, get_database
from jarvis.core.models import Item
from jarvis.models import Beer, Liquor, Wine
import jarvis.crud as crud

router = APIRouter()


@router.post("/add/{drink_type}")
async def add_item_to_db(
    drink_type: str, item: Item, db: DataBase = Depends(get_database)
):
    type_mapping = {"beer": Beer, "liquor": Liquor, "wine": Wine}
    async with db.pool.acquire() as conn:
        type_converted_item = type_mapping.get(drink_type)(**item.dict())
        added_item = await crud.create_item(conn, type_converted_item)
        return added_item
