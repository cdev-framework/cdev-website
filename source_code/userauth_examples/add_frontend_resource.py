# Generated as part of User Auth project template 
import json

from cdev.resources.simple.api import Api, Authorizer
from cdev.resources.simple.xlambda import simple_function_annotation

from cdev.resources.simple.static_site import StaticSite

from cdev import Project as cdev_project

myProject = cdev_project.instance()

demoAuthorizer = Authorizer(
    name="defaultAuth",
    issuer_url="<your-issuer-url>", # ex: https://dev-f4xoprya.us.auth0.com/
    audience="<your-audience-id>" # ex: urn:tutorial
)
 
DemoApi = Api("demoapi", authorizers=[demoAuthorizer], default_authorizer='defaultAuth')
demo_route = DemoApi.route("/demo", "GET")


@simple_function_annotation("demo_handler", events=[demo_route.event()])
def hello_world(event, context):
    print('Hello from inside your Function!')


    return {
        "status_code": 200,
        "body": json.dumps({"message": "Hello World From The Backend!"}),
        "headers": {
            "content-type": "application/json"
        } 
    }


myFrontend = StaticSite("demofrontend", content_folder="src/content")

myProject.display_output("Base API URL", DemoApi.output.endpoint)
myProject.display_output("Routes", DemoApi.output.endpoints)
myProject.display_output("Static Site URl", myFrontend.output.site_url)