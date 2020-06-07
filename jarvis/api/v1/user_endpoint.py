from fastapi import APIRouter, Body, Depends, Request, status
from fastapi.responses import JSONResponse
from jarvis.db.database import DataBase, get_database
from jarvis.core import config, utils
from jarvis.lib import TwilioHelper
from typing import Dict
from twilio.rest import Client
import jarvis.crud as crud
import logging

# import jarvis.models as model


router = APIRouter()
twilio_helper = TwilioHelper()
client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_ACCOUNT_AUTH_TOKEN)


@router.post("/add")
async def add_item_to_cart(request: Request, db: DataBase = Depends(get_database)):
    body = await request.form()
    parsed_body = dict(body)
    logging.warning(parsed_body)
    beer = parsed_body.get("Field_beer_Value")
    msg = f"You've succesfully added {beer} to your cart! Reply with `Checkout` if you're done shopping!"
    return twilio_helper.compose_mesage(msg)

    # async with db.pool.acquire() as conn:
    # added_item = model.CartItem(**payload)
    # Make potentially a new helper class that has add item
    # because you have to then convert this to a message after etc
    # shopping_cart = model.ShoppingCart(**payload)

    # return None


@router.get("/menu/{item_type}")
async def get_menu(
    item_type: str, db: DataBase = Depends(get_database),
):
    async with db.pool.acquire() as conn:
        try:
            items = await crud.get_all_item_by_type(conn, item_type)
            message_list = [utils.item_model_to_message(item) for item in items]
            message = "\n".join(message_list)
            return message

            ## get rid of message when sending back to twilio
            twilio_message = twilio_helper.compose_mesage(message)
            return twilio_message

        except UserWarning as warning:
            return JSONResponse(
                status_code=status.HTTP_202_ACCEPTED, content=str(warning)
            )


@router.post("/checkout")
async def checkout_cart(
    payload: Dict = Body(...), db: DataBase = Depends(get_database)
):
    pass


@router.post("/sms")
async def get_twilio_text():
    resp = ":)"
    return utils.create_text_response(resp)


@router.get("/test")
async def twilio_test(payload: Dict = Body(...)):

    message = client.messages.create(
        body="Jarvis test",
        messaging_service_sid=config.TWILIO_ACCOUNT_MESSAGING_SID,
        to=config.TO_PHONE_NUMBER,
    )

    return message.sid
