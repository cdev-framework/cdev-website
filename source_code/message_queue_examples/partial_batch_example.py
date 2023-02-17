from cdev.aws.sqs import Queue
from cdev.aws.lambda_function import ServerlessFunction


myQueue = Queue('demo')

queue_event_trigger = myQueue.create_event_trigger(
    batch_size=5, 
    batch_failure=False
)

@ServerlessFunction("demofunction", events=[queue_event_trigger], permissions=[myQueue.available_permissions.READ_EVENTS])
def hello_world(event,context):
    failed_items = []

    for record in event.get('records'):
        try:
            process_message(record)
        except Exception:
            failed_items.append(record.get('message_id'))


    if failed_items:
        return {"batchItemFailures": [{"itemIdentifier": x} for x in failed_items]}
