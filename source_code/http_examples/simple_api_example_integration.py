import json

from cdev.resources.simple.xlambda import simple_function_annotation
from cdev.resources.simple.api import Api, route_verb

myApi = Api("demoApi")

hello_world_get_route = myApi.route("/hello_world", route_verb.GET)

@simple_function_annotation("demo_function", events=[hello_world_get_route.event()])
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