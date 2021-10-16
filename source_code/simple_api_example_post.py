import json

from cdev.resources.simple import api
from cdev.resources.simple.xlambda import simple_lambda_function_annotation

myApi = Api("cdev_api_name", "api_name")

hello_world_get_route = myApi.route("/send_data", "POST")

@simple_lambda_function_annotation("send_data_handler", events=[hello_world_get_route])
def handle_data(event, context):
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