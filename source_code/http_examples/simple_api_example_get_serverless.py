import json

from cdev.aws.api import Api
from cdev.aws.lambda_function import ServerlessFunction

from cdev import Project as cdev_project

myProject = cdev_project.instance()

myApi = Api("demoApi")

hello_world_get_route = myApi.route("/hello_world", "GET")


@ServerlessFunction("demo_function", events=[hello_world_get_route.event()])
def hello_world(event, context):
    """
    This is an example function connected to an example API route
    """
    message = {
        "message": "Hello World from Lambda!"
    }

    return {
        "isBase64Encoded": False,
        "status_code": 200, 
        "body": json.dumps(message),
        "headers": {
            "Content-Type": "application/json"
        }
    }


myProject.display_output("Base API URL", myApi.output.endpoint)
myProject.display_output("Routes", myApi.output.endpoints)