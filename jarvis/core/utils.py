from starlette.responses import Response
from twilio.twiml.messaging_response import MessagingResponse


def create_text_response(response: MessagingResponse) -> Response:
    headers = {"Content-Type": "text/plain"}
    return Response(content=str(response), headers=headers)
