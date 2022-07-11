# Generated as part of Quick Start project template 
import os

from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session

from cdev.resources.simple.api import Api
from cdev.resources.simple.xlambda import simple_function_annotation
from cdev.resources.simple.relational_db import RelationalDB, db_engine
from cdev import Project as cdev_project

from .models import User

myProject = cdev_project.instance()

## Routes
DemoApi = Api("demoapi")

hello_route = DemoApi.route("/hello_world", "GET")

## DB
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


## Functions

cluster_arn = os.environ.get("CLUSTER_ARN")
secret_arn = os.environ.get("SECRET_ARN")
database_name = os.environ.get("DB_NAME")

engine = create_engine(f'postgresql+auroradataapi://:@/{database_name}',
                    connect_args=dict(aurora_cluster_arn=cluster_arn, secret_arn=secret_arn))


@simple_function_annotation("hello_world_function", events=[hello_route.event()], 
environment={"CLUSTER_ARN": myDB.output.cluster_arn, "SECRET_ARN": myDB.output.secret_arn, "DB_NAME": myDB.database_name}, 
permissions=[myDB.available_permissions.DATABASE_ACCESS, myDB.available_permissions.SECRET_ACCESS])
def hello_world(event, context):
    print('Hello from inside your Function!')

    session = Session(engine)

    stmt = select(User).where(User.name == 'Paul Atreides')

    for user in session.scalars(stmt):
        print(user)

    return {
        "status_code": 200,
        "message": "Hello Outside World!"
    }


## Output
myProject.display_output("Base API URL", DemoApi.output.endpoint)
myProject.display_output("Routes", DemoApi.output.endpoints)