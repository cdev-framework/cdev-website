import json

from cdev.aws.lambda_function import ServerlessFunction
from cdev.aws.api import Api, route_verb


myApi = Api("demo")
hello_route = myApi.route("/hello", route_verb.GET)


@ServerlessFunction("hello_function", events=[hello_route.event()])
def hello_world(event, context):
  print(event)
  message = "Hello!"

  return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "body": json.dumps(message),
        "headers": {
          "content-type": "application/json"
        } 
    }

