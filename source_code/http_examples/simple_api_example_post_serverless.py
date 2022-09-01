import json

from cdev.aws.api import Api
from cdev.aws.lambda_function import ServerlessFunction

from cdev import Project as cdev_project

myProject = cdev_project.instance()

myApi = Api("demoApi")

send_data_route = myApi.route("/send_data", "POST")


@ServerlessFunction("send_data_handler", events=[send_data_route.event()])
def hello_world(event, context):
    
    """
    This is an example function connected to an example POST API route that can receive data
    """

    print(event)

    data = json.loads(event.get("body"))

    print(data)
    message = {
        "message": "Handled Data"
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