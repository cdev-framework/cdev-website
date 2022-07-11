# Generated as part of Quick Start project template 

from cdev.resources.simple.api import Api
from cdev.resources.simple.xlambda import simple_function_annotation

from cdev.resources.simple.relational_db import RelationalDB, db_engine

from cdev import Project as cdev_project

myProject = cdev_project.instance()

DemoApi = Api("demoapi")

hello_route = DemoApi.route("/hello_world", "GET")

@simple_function_annotation("hello_world_function", events=[hello_route.event()])
def hello_world(event, context):
    print('Hello from inside your Function!')


    return {
        "status_code": 200,
        "message": "Hello Outside World!"
    }


db_resource = "demo_db"
username = "username"
password ="pasword"
db_name = "default_table"

myDB = RelationalDB(
  db_resource,
  db_engine.aurora_postgresql,
  username,
  password,
  db_name
)


myProject.display_output("Base API URL", DemoApi.output.endpoint)
myProject.display_output("Routes", DemoApi.output.endpoints)