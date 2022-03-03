{
    "type": "tutorials",
    "layout": "type",
    "title": "Slack Bot",
    "linktitle": "slackbot", 
    "card_icon": "ti-comments",
    "card_body": "Learn how to create a Slack bot",
    "weight": "3"
}

# New Header

# Building a Slack Bot

{{<blockqoute>}}
What are bots? 
A bot is a type of Slack App designed to interact with users via conversation.

A bot is the same as a regular app: it can access the same range of APIs and do all of the magical things that a Slack App can do.

But when you build a bot for your Slack App, you're giving that app a face, a name, and a personality, and encouraging users to talk to it.

Your bot can send DMs, it can be mentioned by users, it can post messages or upload files, and it can be invited to channels - or kicked out.

{{<break 1>}}
-Slack Documentation
{{</blockqoute>}}



## Creating the App and Bot in Slack
We are going to start by setting up a development App and Bot in Slack and then connect it to a custom backend created with Cdev. Once we have the logic and functionality that we want, we can come back and create a replica of the Bot to be used as the production version. 

Start by going to [https://api.slack.com/apps](https://api.slack.com/apps) and clicking the `Create New App` button. We recommend using the `From an app manifest` starting path. From there, select the workspace you want to add the bot in. Then on the second page, change the name to `Dev {your project}` so that you know this is the development version of your app.


{{<tutorial_image>}}
/images/slack_tutorial/app_manifest.png
{{</tutorial_image>}}
{{<break 1>}}

Now that we have created the App, we are going to give a set of Oauth Permissions to our Bot. This will allow our Bot to make calls to the Slack Api to do things like post messages. Navigate to the `OAuth & Permissions` page via the side bar, then scroll down to the `Scopes` section. For this tutorial, we are going to add the `chat:write` OAuth Permissions.

{{<tutorial_image>}}
/images/slack_tutorial/add_chat_privaleges.png
{{</tutorial_image>}}
{{<break 1>}}

You should be able to now install the App to your Workspace by scrolling back up to the top of the `OAuth & Permissions` page.
{{<tutorial_image>}}
/images/slack_tutorial/install_to_workspace.png
{{</tutorial_image>}}
{{<break 1>}}

Now that the App has been installed, you will see that there is `Bot User OAuth Token`. Take note of this value as we will need it when configuring our backend. 

{{<tutorial_image>}}
/images/slack_tutorial/bot_oauth_token.png
{{</tutorial_image>}}
{{<break 1>}}

We can now set up our Bot to receive events from our Workspace. The general flow of data for a Bot is that Slack sends notifications to our backend about events in the Workspace and then we reply by sending a message to the Slack Api as our Bot. To be able to receive these events, we must provide a webhook for Slack to send the data to, which we will now set up using Cdev.


## Creating the Backend with Cdev
**See getting started if you have not worked with a Cdev project before**

### Create a Cdev Project 

We will be starting from a provided template for this template. You can create the template project by running
```
cdev init my-slack-bot --template slack-bot
```

Our template uses the Slack Python SDK, so you need to install it to your environment via the provided requirements.txt file
```
pip install -r requirements.txt
```

### Add our Settings
We need to change our `Environments` settings module, so that we can provided our `SLACK_SECRET` and `SLACK_BOT_OAUTH_TOKEN` as variables to our `Cdev Environment`. 

```
cdev environment settings_information --key base_class --new-value src.project_settings.SlackBotSettings
```
This command updates your `Cdev Environment` to use the provided `SlackBotSettings` class as the container for your settings. For more information about how to modify `Environment Settings` check out our documentation in the [example section](/docs/examples/settings).


### Set our Settings

Create a file called `cdev_slack_bot_oauth_token` in the `settings/dev_secrets/` folder. Then in the created file, paste the `Bot User OAuth Token` from the previous steps. This should be the only value in the file. 

{{<tutorial_image>}}
/images/slack_tutorial/bot_oauth_token.png
{{</tutorial_image>}}
{{<break 1>}}

Create a file called `cdev_slack_secret` in the `settings/dev_secrets/` folder. Then in the created file, paste the `Signing Secret` from your apps `Basic Information` page. This should be the only value in the file. 


{{<tutorial_image>}}
/images/slack_tutorial/signing_secret.png
{{</tutorial_image>}}
{{<break 1>}}

### Deploying our Bot

Now we can deploy our backend.
```
cdev deploy
```

You should see that the deployment produced an Api url as output.

```
Base API URL -> <your url>
Routes -> FrozenDict({'/webhook POST': 'ca8ts2p'})
```

### Add our generated Webhook

We are going to take this Api and use it to receive events from our Slack Workspace. In the Slack App page, `Enable Events` on the `Events Subscription` page and add your full url (<base_url/webhook>) as the `receive_url`. It will automatically send a test event to your backend to make sure it is configured correctly. 

{{<tutorial_image>}}
/images/slack_tutorial/add_webhook_url.png
{{</tutorial_image>}}
{{<break 1>}}

You can see that the event was received by showing the logs of your function.
```
cdev run function.logs slack_bot.webhook
```

## Modifying the Slack Bot Events

We now must tell Slack what events we want to listen for. This is an important part of understanding the load your backend will receive, and you should choose the smallest amount of events needed to make your application. For this tutorial, we will only be listening to events that directly mention our App or Bot (`message.im` and `app_mention`). You can set your events by scrolling down on the `Events Subscription` page to the `Subscribe to Bot Events` section. Note after saving the changes, you will have to reinstall the app. 

{{<tutorial_image>}}
/images/slack_tutorial/subscribe_to_bot_events.png
{{</tutorial_image>}}
{{<break 1>}}


Now you should be able to directly message your Bot in a Slack Channel and have it reply!
{{<tutorial_image>}}
/images/slack_tutorial/demo_in_slack.png
{{</tutorial_image>}}
{{<break 1>}}

Congratulations you have set up your Slack Bot!! Continue reading to learn how to add more functionality to your Slack Bot!


**Todo add more about using messaging queues to segment messages to downstream consumers**

## Use a messaging queue for more advanced use cases
https://api.slack.com/apis/connections/events-api#the-events-api__responding-to-events
