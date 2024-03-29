from twilio.twiml.messaging_response import MessagingResponse

from cdev.aws.lambda_function import ServerlessFunction
from cdev import Project as cdev_project

from .api import twilio_webhook_route
from .serializer import TwilioWebhookEvent
from .link_service import parse_message, ParsingError
from .notion_service import save_info_notion
from .notion_service import NOTION_DB_ID, NOTION_TOKEN

from ..link_bot_settings import LinkBotSettings

myProject = cdev_project.instance()
mySettings: LinkBotSettings = myProject.settings

notion_env_vars = {
    NOTION_DB_ID: mySettings.NOTION_DB_ID,
    NOTION_TOKEN: mySettings.NOTION_SECRET
}


twilio_webhook_permissions = []
twilio_webhook_env_vars = {**notion_env_vars}

@ServerlessFunction("twilio_handler", 
    events=[twilio_webhook_route.event("application/xml")], 
    environment=twilio_webhook_env_vars, 
    permissions=twilio_webhook_permissions
)
def twilio_handler(event, context):
    twilio_event = TwilioWebhookEvent(event)
    print(f"Received message -> {twilio_event.body.Body}; from -> {twilio_event.body.From}")

    response = MessagingResponse()

    try: 
        url, description, tags = parse_message(twilio_event.body.Body)

        print(f"{twilio_event.body.Body} -> ({url}, {description}, {tags})")

        try:
            return_message = save_info_notion(url, description, tags)
            response.message(return_message)

        except Exception as e:
            response.message("Could not save to Notion")

        
    except ParsingError as e:
        response.message(e.message)

    
    return response.to_xml()

