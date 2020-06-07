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
        INSERT INTO {item_type}(name, price, quantity, image_url, image_width, image_height)
        VALUES($1, $2, $3, $4, $5, $6)
        RETURNING *
        """,
        item.name,
        item.price,
        item.quantity,
        item.image_url,
        item.image_width,
        item.image_height,
    )
    if row and model:
        return model(**row)
    else:
        raise UserWarning(
            f"Either {item_type} items or model was empty while adding to the database."
        )


async def update_item(
    conn: Connection, item: Union[Beer, Liquor, Wine]
) -> Union[Beer, Liquor, Wine, None]:

    item_type = str(item)
    model_mapping = {"beer": Beer, "wine": Wine, "liquor": Liquor}
    model = model_mapping.get(item_type, None)
    row = await conn.fetchrow(
        f"""
        UPDATE {item_type}
        SET name = $1, price = $2, quantity = $3, image_url = $4, image_width = $5, image_height = $6
        RETURNING *
        """,
        item.name,
        item.price,
        item.quantity,
        item.image_url,
        item.image_width,
        item.image_height,
    )
    if row and model:
        return model(**row)
    else:
        raise UserWarning(
            f"Either {item_type} items or model was empty when trying to make an update."
        )


async def delete_item(
    conn: Connection, item: Union[Beer, Liquor, Wine]
) -> Union[Beer, Liquor, Wine, None]:

    item_type = str(item)
    model_mapping = {"beer": Beer, "wine": Wine, "liquor": Liquor}
    model = model_mapping.get(item_type, None)
    row = await conn.fetchrow(
        f"""
        DELETE FROM {item_type}
        WHERE id = $1
        RETURNING *
        """,
        item.id,
    )
    if row and model:
        return model(**row)
    else:
        raise UserWarning(
            f"Either {item_type} items or model was empty when trying to delete the item."
        )


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
        raise UserWarning(
            f"Either there are no {item_type} items or the model was empty while getting the menu."
        )
