import json

from cdev.resources.simple.xlambda import simple_function_annotation
from cdev.resources.simple.api import Api, route_verb

myApi = Api("demoApi")

send_data_route = myApi.route("/send_data", route_verb.POST)

@simple_function_annotation("send_data_handler", events=[send_data_route.event()])
def hello_world(event, context):
    """
    This is an example function connected to an example POST api route that can receive data
    """

    print(event)

    # Load the body of the request into a data obj
    data = json.loads(event.get("body"))

    print(data)
    

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps({"message": "handled data"}),
        "headers": {
          "content-type": "application/json"
        } 
    }
