{
    "type": "examples",
    "layout": "type",
    "title": "Integrate Pub/Sub Topics",
    "linktitle": "topic",
    "card_icon": "ti-signal",
    "card_body": "Learn to create and integrate a Pub/Sub Topic",
    "weight": "5"
}


# Pub/Sub Topic
{{<header_divider>}}

A Pub/Sub Topic that allows for events to be transmitted in a Fan Out fashion.

{{<break 1>}}
### Basic Topic

{{<codesnippet `/source_code/topic_examples/simple_topic_example.py`>}}


{{<break 2>}}
### Integrating with a Serverless Function
You can use a Serverless Function to respond to the events from a Queue

{{<codesnippet `/source_code/topic_examples/topic_event_example.py`>}}
