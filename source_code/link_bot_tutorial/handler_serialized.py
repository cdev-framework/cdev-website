from twilio.twiml.messaging_response import MessagingResponse

from cdev.aws.lambda_function import ServerlessFunction

from .api import twilio_webhook_route
from .serializer import TwilioWebhookEvent

@ServerlessFunction("twilio_handler", events=[twilio_webhook_route.event("application/xml")])
def twilio_handler(event, context):
    twilio_event = TwilioWebhookEvent(event)
    print(f"Received message -> {twilio_event.body.Body}; from -> {twilio_event.body.From}")

    response = MessagingResponse()
    response.message("Hi from your backend!")

    return response.to_xml()