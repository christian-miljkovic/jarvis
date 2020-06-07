from starlette.responses import JSONResponse, Response
from twilio.twiml.messaging_response import MessagingResponse
from fuzzywuzzy import process
from jarvis.crud.items import get_all_item_by_type


def create_text_response(response: MessagingResponse) -> Response:
    headers = {"Content-Type": "text/plain"}
    return Response(content=str(response), headers=headers)


def create_json_response(message: dict) -> JSONResponse:
    return JSONResponse(message)


def item_model_to_message(item) -> str:
    price = item.dict().get("price", "")
    name = item.dict().get("name", "")
    quantity = item.dict().get("quantity", "")
    return f"{name} - ${price} quantity: {quantity}"


def match_item_name_from_user_input(conn, item_type, user_text):
    list_of_items = get_all_item_by_type(conn, item_type)
    list_of_names = [item.name for item in list_of_items]
    highest_accurate_match = process.extractOne(user_text, list_of_names)
    return highest_accurate_match
