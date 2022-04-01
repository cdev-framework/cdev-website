from aws_lambda_powertools.utilities.data_classes import event_source, APIGatewayProxyEventV2
from aws_lambda_powertools.utilities.data_classes.common import DictWrapper

import base64
from urllib.parse import parse_qs

from typing import Dict, Any

class TwilioWebhookEvent(APIGatewayProxyEventV2):
    def __init__(self, data: Dict[str, Any]):
        body_str = base64.b64decode(data.get('body')).decode("utf-8")
        parsed_data = {k:(v[0] if len(v)==1 else v) for k,v in parse_qs(body_str).items() }
        data['body'] = TwilioWebhookData(parsed_data)
        super().__init__(data)


    @property
    def body(self) -> 'TwilioWebhookData':
        """
        TwilioWebhookData: Wrapper around the data send from a Twilio Webhook. More details can be found on their [official documentation](https://www.twilio.com/docs/messaging/guides/webhook-request).
        """
        return self.get("body")


class TwilioWebhookData(DictWrapper):
    """
    Wrapper around the data send from a Twilio Webhook. More details can be found on their [official documentation](https://www.twilio.com/docs/messaging/guides/webhook-request).
    """

    @property
    def MessageSid(self) -> str:
        "A 34 character unique identifier for the message. May be used to later retrieve this message from the REST API."
        return self.get("MessageSid")


    @property
    def SmsSid(self) -> str:
        "Same value as MessageSid. Deprecated and included for backward compatibility."
        return self.get("SmsSid")


    @property
    def AccountSid(self) -> str:
        "The 34 character id of the [Account](https://www.twilio.com/docs/iam/api/account) this message is associated with."
        return self.get("AccountSid")

    
    @property
    def MessagingServiceSid(self) -> str:
        "The 34 character id of the [Messaging Service](https://www.twilio.com/docs/sms/send-messages#messaging-services) associated with the message."
        return self.get("MessagingServiceSid")

    
    @property
    def From(self) -> str:
        "The phone number or [Channel address](https://www.twilio.com/docs/messaging/channels#channel-addresses) that sent this message."
        return self.get("From")


    @property
    def To(self) -> str:
        "The phone number or [Channel address](https://www.twilio.com/docs/messaging/channels#channel-addresses) address of the recipient."
        return self.get("To")

    
    @property
    def Body(self) -> str:
        "The text body of the message. Up to 1600 characters long."
        return self.get("Body")

    
    @property
    def NumMedia(self) -> str:
        "The number of media items associated with your message"
        return self.get("NumMedia")


    @property
    def ReferralNumMedia(self) -> str:
        "The number of media items associated with a 'Click to WhatsApp' advertisement."
        return self.get("ReferralNumMedia")

