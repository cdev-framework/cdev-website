import json

from cdev.resources.simple import api
from cdev.resources.simple.xlambda import simple_lambda_function_annotation

myApi = Api("cdev_api_name", "api_name")

hello_world_get_route = myApi.route("/hello_world", "GET")

@simple_lambda_function_annotation("hello_world_handler", events=[hello_world_get_route])
def hello_world(event, context):
    """
    This is an example function connected to an example api route
    """

    message = {
        "message": "Hello from a lambda"
    }

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps(message),
        "headers": {
          "content-type": "application/json"
        } 
    }