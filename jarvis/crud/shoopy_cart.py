from asyncpg import Connection
from typing import Union
from jarvis.models import ShoppingCart


async def create_shopping_cart(
    conn: Connection, customer_phone_number: str
) -> Union[ShoppingCart, None]:

    row = await conn.fetchrow(
        f"""
        INSERT INTO shopping_cart(customer_phone_number)
        VALUES($1)
        """,
        customer_phone_number,
    )
    return ShoppingCart(**row)


async def get_cart_by_user_phone_number(
    conn: Connection, customer_phone_number: str
) -> Union[ShoppingCart, None]:

    row = await conn.fetchrow(
        f"""
        SELECT * FROM shopping_cart WHERE customer_phone_number = $1
        """,
        customer_phone_number,
    )
    return ShoppingCart(**row)
