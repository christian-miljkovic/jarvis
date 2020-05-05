from asyncpg import Connection
from typing import List, Union
from jarvis.models import Beer, Wine, Liquor


async def create_item(
    conn: Connection, item: Union[Beer, Liquor, Wine]
) -> Union[Beer, Liquor, Wine, None]:

    item_type = str(item)
    model_mapping = {"beer": Beer, "wine": Wine, "liquor": Liquor}
    model = model_mapping.get(item_type, None)
    row = await conn.fetchrow(
        f"""
        INSERT INTO {item_type}(name, price, image_url, image_width, image_height)
        VALUES($1, $2, $3, $4, $5)
        RETURNING *
        """,
        item.name,
        item.price,
        item.image_url,
        item.image_width,
        item.image_height,
    )
    if row and model:
        return model(**row)
    else:
        raise UserWarning(f"Erroed while trying to create a {item_type} item.")


async def get_all_item_by_type(
    conn: Connection, item_type: str
) -> List[Union[Beer, Liquor, Wine, None]]:

    model_mapping = {"beer": Beer, "wine": Wine, "liquor": Liquor}
    model = model_mapping.get(item_type, None)
    rows = await conn.fetch(
        f"""
        SELECT * FROM {item_type} WHERE quantity > 0
        """
    )
    if rows and model:
        return [model(**row) for row in rows]
    else:
        raise UserWarning(f"Erroed while trying to get all {item_type} items.")
