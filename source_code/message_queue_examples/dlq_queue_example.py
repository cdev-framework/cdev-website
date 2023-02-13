from cdev.aws.sqs import Queue

myQueue = Queue('demo', dlq_arn="<aws_queue_arn>", max_receive_count=10)