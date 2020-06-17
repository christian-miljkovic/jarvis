from jarvis.core import config
from jarvis.core import utils
from twilio.rest import Client
import logging

TWILIO_CLIENT = Client(config.TWILIO_ACCOUNT_SID, config.TWILIO_ACCOUNT_AUTH_TOKEN)


class TwilioHelper:
    def __init__(self):
        self.client = TWILIO_CLIENT

    def compose_mesage(self, message, memory=None, item_to_add=None):
        response = {"actions": []}
        self.add_text(response, message)
        if item_to_add and memory:
            self.remember_this_item(response, memory, item_to_add)

        return utils.create_json_response(response)

    def add_text(self, response: dict, message: str):
        response.get("actions").append({"say": message})

    def remember_this_item(self, current_message, current_memory, item):
        new_order = current_memory.get("order", [])
        item_object = {"item": item.get("id"), "quantity": item.get("quantity")}
        new_order.append(item_object)
        return current_message.get("actions").append({"remember": {"order": new_order}})
