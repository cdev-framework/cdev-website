# Generated as part of Quick Start project template 

from cdev.aws.api import Api
from cdev.aws.lambda_function import ServerlessFunction

from cdev.aws.relational_db import RelationalDB, db_engine

from cdev import Project as cdev_project

myProject = cdev_project.instance()

DemoApi = Api("demoapi")

hello_route = DemoApi.route("/hello_world", "GET")

@ServerlessFunction("hello_world_function", events=[hello_route.event()])
def hello_world(event, context):
    print('Hello from inside your Function!')


    return {
        "status_code": 200,
        "message": "Hello Outside World!"
    }


myDB = RelationalDB(
  cdev_name="demo_db",
  engine=db_engine.aurora_postgresql,
  username="username",
  password="password",
  database_name="default_table"
)


myProject.display_output("Base API URL", DemoApi.output.endpoint)
myProject.display_output("Routes", DemoApi.output.endpoints)