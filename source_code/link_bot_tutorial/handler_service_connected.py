from twilio.twiml.messaging_response import MessagingResponse

from cdev.resources.simple.xlambda import simple_function_annotation

from .api import twilio_webhook_route
from .serializer import TwilioWebhookEvent
from .link_service import parse_message, ParsingError

@simple_function_annotation("twilio_handler", events=[twilio_webhook_route.event("application/xml")])
def twilio_handler(event, context):
    twilio_event = TwilioWebhookEvent(event)
    print(f"Received message -> {twilio_event.body.Body}; from -> {twilio_event.body.From}")

    response = MessagingResponse()

    try: 
        url, description, tags = parse_message(twilio_event.body.Body)

        print(f"{twilio_event.body.Body} -> ({url}, {description}, {tags})")

        response.message("Parsed Message!")
    except ParsingError as e:
        response.message(e.message)

    
    return response.to_xml()

