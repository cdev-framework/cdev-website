import json

from cdev.aws.lambda_function import ServerlessFunction
from cdev.aws.api import Api, route_verb

myApi = Api("demoApi")

hello_world_get_route = myApi.route("/hello_world", route_verb.GET)

@ServerlessFunction("demo_function", events=[hello_world_get_route.event()])
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
