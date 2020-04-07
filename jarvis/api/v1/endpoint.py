from fastapi import APIRouter, Body
from typing import Dict
from jarvis.core import config
from jarvis.core import utils
from twilio.rest import Client


router = APIRouter()
client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_ACCOUNT_AUTH_TOKEN)


@router.get("/test")
async def twilio_test(payload: Dict = Body(...)):

    message = client.messages.create(
        body="Jarvis test",
        messaging_service_sid=config.TWILIO_ACCOUNT_MESSAGING_SID,
        to=config.TO_PHONE_NUMBER,
    )

    return message.sid


@router.post("/sms")
async def get_twilio_text():
    resp = "Your emy princess forever!"
    return utils.create_text_response(resp)
