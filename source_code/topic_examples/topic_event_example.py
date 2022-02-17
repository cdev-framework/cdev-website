from cdev.resources.simple.topic import Topic
from cdev.resources.simple.xlambda import simple_function_annotation

myTopic = Topic("demo")
topic_event = myTopic.create_event_trigger()

@simple_function_annotation("demofunction", events=[topic_event], permissions=[myTopic.available_permissions.SUBSCRIBE])
def demo(event, context):
    print(event)

