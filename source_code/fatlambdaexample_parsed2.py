import boto3


s3_client = boto3.client("s3")


def MyHandler2(event, context):
    # This function gets an object from s3 and returns it to the user

    object = s3_client.get_object(event.get("item_key"))

    # Other Code
    #
    #
    #

    return object

