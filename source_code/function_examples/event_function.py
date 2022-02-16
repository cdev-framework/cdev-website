import json

from cdev.resources.simple.xlambda import simple_function_annotation
from cdev.resources.simple.api import Api, route_verb


myApi = Api("demo")
hello_route = myApi.route("/hello", route_verb.GET)


@simple_function_annotation("hello_function", events=[hello_route.event()])
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

