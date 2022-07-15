import json

from cdev.resources.simple.api import Api
from cdev.resources.simple.xlambda import simple_function_annotation

from cdev import Project as cdev_project

myProject = cdev_project.instance()

myApi = Api("demoApi")

hello_world_get_route = myApi.route("/hello_world", "GET")


@simple_function_annotation("demo_function", events=[hello_world_get_route.event()])
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