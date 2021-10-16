import boto3


sqs_client = boto3.client("sqs")


def MyHandler3(event, context):
    # This function creates an item in an sqs queue that triggers downstream tasks

    sqs_client.put_item(event.get("sqs_event"))
    return {}