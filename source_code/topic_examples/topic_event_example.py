from cdev.aws.topic import Topic
from cdev.aws.lambda_function import ServerlessFunction

myTopic = Topic("demo")
topic_event = myTopic.create_event_trigger()

@ServerlessFunction("demofunction", events=[topic_event], permissions=[myTopic.available_permissions.SUBSCRIBE])
def demo(event, context):
    print(event)

