from cdev.aws.sqs import Queue
from cdev.aws.lambda_function import ServerlessFunction


myQueue = Queue('demo')
queue_event_trigger = myQueue.create_event_trigger()

@ServerlessFunction("demofunction", events=[queue_event_trigger], permissions=[myQueue.available_permissions.READ_EVENTS])
def hello_world(event,context):
  print(event)