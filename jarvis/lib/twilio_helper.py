from jarvis.core import config
from jarvis.core import utils
from twilio.rest import Client

TWILIO_CLIENT = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_ACCOUNT_AUTH_TOKEN)


class TwilioHelper:
    def __init__(self):
        self.client = TWILIO_CLIENT

    def compose_mesage(self, message):
        response = {"actions": []}
        self.add_text(response, message)
        return utils.create_json_response(response)

    def add_text(self, response: dict, message: str):
        response.get("actions").append({"say": message})

    @staticmethod
    def remember_this_item(current_memory, item, quantity):
        current_order = current_memory.get("order", {"order": []})
        item_object = {"item": item.dict().get("id"), "quantity": quantity}
        current_order.append(item_object)
        return {"actions": [{"remember": current_order}]}
