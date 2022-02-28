# Generated as part of Quick Start project template 

from cdev.resources.simple.api import Api, Authorizer
from cdev.resources.simple.xlambda import simple_function_annotation

from cdev import Project as cdev_project

myProject = cdev_project.instance()

demoAuthorizer = Authorizer(
    name="defaultAuth",
    issuer_url="https://dev-f4xoprya.us.auth0.com/",
    audience="urn:tutorial"
)

DemoApi = Api("demoapi", authorizers=[demoAuthorizer], default_authorizer='defaultAuth')

hello_route = DemoApi.route("/hello_world", "GET")

@simple_function_annotation("hello_world_function", events=[hello_route.event()])
def hello_world(event, context):
    print('Hello from inside your Function!')


    return {
        "status_code": 200,
        "message": "Hello Outside World!"
    }



myProject.display_output("Base API URL", DemoApi.output.endpoint)
myProject.display_output("Routes", DemoApi.output.endpoints)