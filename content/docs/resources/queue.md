{
    "type": "examples",
    "layout": "type",
    "title": "SQS Queue",
    "linktitle": "queue",
    "card_icon": "ti-direction",
    "card_body": "Learn to create and integrate a Message Queue",
    "weight": "5"
}


# Message Queues
{{<header_divider>}}

Message queue that allows for events to be transmitted between different software components. 

{{<break 1>}}
### Basic Queue

{{<codesnippet `/source_code/message_queue_examples/simple_queue_example.py`>}}

{{<break 2>}}
### Integrating with a Serverless Function
You can use a Serverless Function to respond to the events from a queue.

{{<codesnippet `/source_code/message_queue_examples/queue_event_example.py`>}}

{{<break>}}
### Message Ordering
By default, message order is not guaranteed, but you can designate a queue as First in First Out (fifo). This feature impacts performance and functionality of the queue, therefor [you should be aware of the trade-offs](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html).

{{<codesnippet `/source_code/message_queue_examples/fifo_queue_example.py`>}}

{{<break>}}
### Handling Errors
Sometimes there can be erroneous messages passed into the Queue that are not able to be properly handled. The message retry policy for a queue can be configured with the `max_receive_count` parameter, which determines the number of time a message should be retried. You can also provide a Dead Letter Queue (dql), which is a seperate queue to move messages into once they have exceeded the `max_receive_count`. 

{{<codesnippet `/source_code/message_queue_examples/dlq_queue_example.py`>}}

{{<break>}}

By default, SQS sends batches of events to the handling function, and if the function throws an exception during the handling of a batch, the queue will mark the entire batch as failed. You can configure your queue to handle individual message failures by setting the `batch_failure` parameter on the event and [return a structured response from your function when a message fails](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-batchfailurereporting).


{{<codesnippet `/source_code/message_queue_examples/partial_batch_example.py`>}}
