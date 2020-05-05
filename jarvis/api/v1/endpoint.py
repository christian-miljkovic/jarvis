from fastapi import APIRouter, Body, Depends, status
from fastapi.responses import JSONResponse
from jarvis.db.database import DataBase, get_database
from jarvis.core import config, utils
from jarvis.lib import TwilioHelper
from typing import Dict
from twilio.rest import Client
import jarvis.crud as crud


router = APIRouter()
twilio_helper = TwilioHelper()
client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_ACCOUNT_AUTH_TOKEN)


@router.post("/add")
async def add_item_to_cart(
    item_id: str, payload: Dict = Body(...), db: DataBase = Depends(get_database)
):
    pass


@router.post("/menu")
async def get_menu(
    item_type: str, payload: Dict = Body(...), db: DataBase = Depends(get_database)
):

    async with db.pool.acquire() as conn:
        try:
            items = crud.get_all_item_by_type(conn, item_type)
            message_list = [utils.item_model_to_message(item) for item in items]
            message = "\n".join(message_list)
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
