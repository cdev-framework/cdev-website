{
    "type": "tutorial",
    "layout": "type",
    "title": "Create a Link Aggregator",
    "linktitle": "linkaggregator", 
    "card_icon": "ti-link",
    "card_body": "Learn how to create a virtual assistant to collect links",
    "weight": "2"
}

Learn how to store links by texting them to a Twilio number and then save them in a Notion Database. 

Twilio provides Api's to help developers integrate SMS into their applications. You can easily send automated text messages with Twilio, and also use webhooks to receive text messages. In this tutorial, we will be creating a `bot` with a SMS interface that allows us to text links to the bot and have those links saved in a Notion Database.

{{<youtube "https://www.youtube.com/embed/uYMn5cWK8tE">}}

{{<tool_tip key="tip" summary="Other Data Stores">}}
In this tutorial, we are using Notion to store our links, but the way the tutorial is structured, you will only need to change the last step to send the links to a different service.
{{</tool_tip>}}

{{<break 1>}}
## Create Twilio Account
You can sign up for a trial [Twilio account](https://www.twilio.com/try-twilio) that can be used for this tutorial. The trial account will come with a credit balance that is more than sufficient for this project. The account will also have access to all [features needed for this tutorial](https://support.twilio.com/hc/en-us/articles/223136107-How-does-Twilio-s-Free-Trial-work-). At the end of the tutorial, you can delete your account or upgrade it to a full Twilio account without losing your work.


When creating your account, you will have to verify both an email and phone number. When you are asked to add some information about how you will be using Twilio, you can use the following settings
{{<tutorial_image>}}
/images/link_bot_tutorial/twilio_signup.png
{{</tutorial_image>}}

Now that your trial account is set up, you can transition to creating your Cdev project. Once we have set up the template project, we will go back to the Twilio Console to create our phone number and webhook. 


{{<break 1>}}
## Create Cdev Project
We will be starting this tutorial from the `quick-start-twilio` project. This is similar the standard `quick-start` template but with a few changes to help integrate with Twilio.

```bash
cdev init link-bot --template quick-start-twilio
```

```bash
pip install -r requirements.txt
```

Now we can deploy our project to get a live Webhook

```bash
cdev deploy
```
This step should output the live url of your webhook and look like
```
Base API URL -> <your-endpoint>
```

We can check that the webhook is live and working by running
```bash
curl -X POST https://<your-endpoint>/twilio_handler
```
You should receive output like 
```
<?xml version="1.0" encoding="UTF-8"?><Response><Message>Hi from your backend!</Message></Response>
```
{{<break 1>}}
## Connect a Twilio Number to the Webhook
We can now go back to the Twilio Console to create our phone number and attach our webhook. In the console, create your first phone number.
{{<tutorial_image>}}
/images/link_bot_tutorial/get_a_number.jpg
{{</tutorial_image>}}

{{<break 1>}}
Now that we have a `Twilio Phone Number`, create a `Messaging Service`.
{{<tutorial_image>}}
/images/link_bot_tutorial/create_messaging_service.png
{{</tutorial_image>}}

{{<tutorial_image>}}
/images/link_bot_tutorial/service_options.jpg
{{</tutorial_image>}}

{{<break 1>}}
Then add a sender. By default, it will add your created number.
{{<tutorial_image>}}
/images/link_bot_tutorial/add_sender.png
{{</tutorial_image>}}

{{<tutorial_image>}}
/images/link_bot_tutorial/added_number.png
{{</tutorial_image>}}

{{<break 1>}}
Now add the webhook information. You will need to add the generated url for your webhook from your `Project`.
{{<tool_tip key="tip" summary="Retrieving your url">}}
If you do not remember your `url` that was outputted by the deployment, you can run the following command to retrieve your url
```bash
cdev output link_bot.api.demoapi.endpoint
```

```
endpoint -> <your-endpoint>
```

Make sure to add the `/twilio_handler` path when adding it to the Twilio Console.

{{</tool_tip>}}

{{<tutorial_image>}}
/images/link_bot_tutorial/add_webhook.png
{{</tutorial_image>}}


{{<break 1>}}
Finally, you can leave the `Business Registration` information empty and complete your `Service`

{{<tutorial_image>}}
/images/link_bot_tutorial/business_registration.png
{{</tutorial_image>}}

{{<tool_tip key="info" summary="Business Registration">}}
If you decided to upgrade your trial account into a full Twilio account, you will need to add some information about how you use the service. This helps Twilio detect spammers and stay in compliance with their carriers.
{{</tool_tip>}}


You can now send a test text message from your number to yourself. 
{{<tutorial_image>}}
/images/link_bot_tutorial/send_demo_message.png
{{</tutorial_image>}}

{{<tutorial_image>}}
/images/link_bot_tutorial/send_test_message.png
{{</tutorial_image>}}

{{<break 1>}}
You should receive your demo text message from your Twilio Number! You can then reply to the number, which will trigger your webhook and reply back with `"Hi from your backend!"`. 


Congratulations {{<emoji>}}:tada:{{</emoji>}} You have created a live bot! We will now be adding more logic to our backend to have the bot save links that we send!

{{<tool_tip key="tip" summary="Create a Contact">}}
Although not necessary, it is fun to save your number in your contacts and give it a photo to make the bot feel more alive!
{{</tool_tip>}}

{{<break 1>}}
## Structure Incoming Messages

Looking at the logs of the current handler, we can see that the first step to parsing our message is structuring the data that is passed to our web hook. Twilio passed the data about the incoming message as a `query string` that is Base64 encoded. We need to decode this data and turn into a structure that we can work with.

{{<tool_tip key="tip" summary="See the logs">}}
You can check the logs with the following command.

```bash
cdev run function.logs link_bot.twilio_handler
```
In the logs, you should see a message like
```
event body -> VG9Db3VudHJ5PVVTJlRvU3RhdGU9TUkmU21zTWVzc2FnZVNpZD1TTTIyMmUxNTNkNTYwZTc4Njg2YTBlMjRmMDkwMmY1YTM4Jk51bU1lZGlhPTAmVG9DaXR5PUdSQU5EK0JMQU5DJkZyb21aaXA9MjgwMjcmU21zU2lkPVNNMjIyZTE1M2Q1NjBlNzg2ODZhMGUyNGYwOTAyZjVhMzgmRnJvbVN0YXRlPU5DJlNtc1N0YXR1cz1yZWNlaXZlZCZGcm9tQ2l0eT1DT05DT1JEJkJvZHk9SGVsbG8rbXkrbmV3K0JvdCtGcmllbmQlMjErJkZyb21Db3VudHJ5PVVTJlRvPSUyQjE4MTA0NDI0NzIyJk1lc3NhZ2luZ1NlcnZpY2VTaWQ9TUc2ZjM2ZDdiMjkzNzhiM2YyMzAyMjMyYzNhNGVhNGU5MyZUb1ppcD00ODQzOSZOdW1TZWdtZW50cz0xJlJlZmVycmFsTnVtTWVkaWE9MCZNZXNzYWdlU2lkPVNNMjIyZTE1M2Q1NjBlNzg2ODZhMGUyNGYwOTAyZjVhMzgmQWNjb3VudFNpZD1BQzcxMDc1MTQ4OGVkZWRlMGRkOWMwYTNkOTkyODBkNmQ2JkZyb209JTJCMTcwNDQ5MDY0NjImQXBpVmVyc2lvbj0yMDEwLTA0LTAx
```
{{</tool_tip>}}

Create a `src/link_bot/serializer.py` file and add the following code to the file. The work for deserializing the data from Twilio is done in the `TwilioWebhookEvent` class initializer (lines 11-13). 

{{<codesnippet `/source_code/link_bot_tutorial/serializer.py`>}}

{{<tool_tip key="info" summary="Powertools Dataclasses">}}
The `TwilioWebhookEvent` is derived from a data class from the Lambda Powertools library. This library provides a light weight mechanism to provide additional information about the `triggering` event for a handler. This allows developers to be given type hints when using the `object` in the handler. 
{{</tool_tip>}}

We can now update our webhook to use our created class to have easier access to the data from Twilio. Update your `handlers.py` to the following code. The newly created `twilio_event` object will provided access to all the available data from the Twilio event.

{{<codesnippet `/source_code/link_bot_tutorial/handler_serialized.py`>}}



{{<break 1>}}
## Link Parsing Service
Now that we are able to understand the data provided to our webhook by Twilio, we need to define the structure of the message that we will support. Our bot will receive a link to store, a description of the link, and set of tags. 


{{<codesnippet `/source_code/link_bot_tutorial/basic_link_service.py`>}}


### Advanced Part

{{<triple_iphone_image `/images/link_bot_tutorial/send_message_hn.jpg` `/images/link_bot_tutorial/basic_message_hn.png` `/images/link_bot_tutorial/error_basic_parsing.png`>}}


{{<break 1>}}
## Test Project


## Save Information Into Notion


### Create a Notion DB Integration


### Save with the Notion Api

{{<break>}}