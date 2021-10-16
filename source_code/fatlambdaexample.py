import boto3

dynamodb_client = boto3.client("dynamodb")

s3_client = boto3.client("s3")

sqs_client = boto3.client("sqs")


def MyHandler1(event, context):
    # This function connects to a dynamodb table to look
    # up information and return it to the user


    #
    info = dynamodb_client.lookup(event.get("user_id"))

    # Other code 
    #
    #
    #

    return info 

def MyHandler2(event, context):
    # This function gets an object from s3 and returns it to the user

    object = s3_client.get_object(event.get("item_key"))

    # Other Code
    #
    #
    #

    return object

def MyHandler3(event, context):
    # This function creates an item in an sqs queue that triggers downstream tasks

    sqs_client.put_item(event.get("sqs_event"))
    return {}