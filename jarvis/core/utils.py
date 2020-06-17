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


async def normalize_cart_item_model(conn, model):
    cart_item_as_dict = model.dict()
    cart_item_with_type = get_item_type_from_model(cart_item_as_dict)
    cart_item_cleaned = get_item_name_from_model(cart_item_with_type)
    user_input_name = cart_item_cleaned.get("name")
    item_type = cart_item_cleaned.get("item_type")
    matched_item = await match_item_by_name_from_user_input(
        conn, user_input_name, item_type
    )
    cart_item_cleaned["name"] = matched_item[0]
    cart_item_cleaned["id"] = matched_item[1]

    return cart_item_cleaned


def get_item_type_from_model(model):
    model_dict = model
    type_fields = {"beer_type", "wine_type", "liquor_type"}

    for key in model_dict.keys():
        value = model_dict.get(key)
        if key in type_fields and value:
            model_dict["item_type"] = value

    return model_dict


def get_item_name_from_model(model):
    model_dict = model
    type_fields = {"beer_name", "wine_name", "liquor_name"}

    for key in model_dict.keys():
        value = model_dict.get(key)
        if key in type_fields and value:
            model_dict["name"] = value

    return model_dict


async def match_item_by_name_from_user_input(conn, user_text, item_type):
    list_of_items = await get_all_item_by_type(conn, item_type)
    list_of_names = [item.name for item in list_of_items]
    name_to_id_dict = {item.name: str(item.id) for item in list_of_items}
    highest_accurate_match = process.extractOne(user_text, list_of_names)

    if not highest_accurate_match:
        raise UserWarning("No accurate match was found based on the input")
    matched_name = highest_accurate_match[0]
    matched_id = name_to_id_dict.get(matched_name, "")
    return [matched_name, matched_id]
