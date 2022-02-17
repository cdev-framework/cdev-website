from cdev.resources.simple.queue import Queue
from cdev.resources.simple.xlambda import simple_function_annotation


myQueue = Queue('demo')
queue_event_trigger = myQueue.create_event_trigger()

@simple_function_annotation("demofunction", events=[queue_event_trigger], permissions=[myQueue.available_permissions.READ_EVENTS])
def hello_world(event,context):
  print(event)