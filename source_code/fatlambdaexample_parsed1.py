import boto3

dynamodb_client = boto3.client("dynamodb")


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
