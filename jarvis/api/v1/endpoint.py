from fastapi import Body
from typing import Dict
from starlette.requests import Request
from jarvis.core.config as config

router = APIRouter()


@router.get("/test")
async def twilio_test(payload: Dict = Body(...)):
    auth_token = 'your_auth_token'
    client = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_ACCOUNT_AUTH_TOKEN)

    message = client.messages.create(body="Join Earth's mightiest heroes. Like Kevin Bacon.", messaging_service_sid='MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',to='+15558675310')

    print(message.sid)
