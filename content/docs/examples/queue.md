{
    "type": "examples",
    "layout": "type",
    "title": "Integrate a Message Queues",
    "linktitle": "queue",
    "card_icon": "ti-direction",
    "card_body": "Learn to create and integrate a Message Queue",
    "weight": "6"
}


# Message Queues

Message Queue that allows for events to be transmitted

{{<break 2>}}
### Basic Queue

{{<codesnippet `/source_code/message_queue_examples/simple_queue_example.py`>}}


{{<break 2>}}
### Integrating with a Serverless Function
You can use a Serverless Function to respond to the events from a Queue

{{<codesnippet `/source_code/message_queue_examples/queue_event_example.py`>}}