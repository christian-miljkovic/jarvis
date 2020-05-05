from starlette.responses import JSONResponse, Response
from twilio.twiml.messaging_response import MessagingResponse


def create_text_response(response: MessagingResponse) -> Response:
    headers = {"Content-Type": "text/plain"}
    return Response(content=str(response), headers=headers)


def create_json_response(message: dict) -> JSONResponse:
    return JSONResponse(message)


def item_model_to_message(item) -> str:
    price = item.dict().get("price", "")
    return f"{str(item)} - ${price}"
