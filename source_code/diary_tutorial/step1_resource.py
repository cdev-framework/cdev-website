# Generated as part of Quick Start project template 
import json
import os

# from sqlalchemy import select, create_engine
# from sqlalchemy.orm import Session

from cdev.aws.api import Api
from cdev.aws.lambda_function import ServerlessFunction
from cdev.aws.relational_db import RelationalDB, db_engine
from cdev import Project

# from .models import Entry





myProject = Project.instance()

## Routes
DemoApi = Api("demoapi")

hello_route = DemoApi.route("/hello_world", "GET")



## DB
myDB = RelationalDB(
  "demo_db",
  db_engine.aurora_postgresql,
  "username",
  "password",
  "default_diaryDB"
)

## Functions

cluster_arn = os.environ.get("CLUSTER_ARN")
secret_arn = os.environ.get("SECRET_ARN")
database_name = os.environ.get("DB_NAME")

# engine = create_engine(f'postgresql+auroradataapi://:@/{database_name}',
#                     connect_args=dict(aurora_cluster_arn=cluster_arn, secret_arn=secret_arn))


@ServerlessFunction("hello_world_function", events=[hello_route.event()], 
environment={"CLUSTER_ARN": myDB.output.cluster_arn, "SECRET_ARN": myDB.output.secret_arn, "DB_NAME": myDB.database_name}, 
permissions=[myDB.available_permissions.DATABASE_ACCESS, myDB.available_permissions.SECRET_ACCESS])
def hello_world(event, context):
    print('Hello from inside your Function!')

    # session = Session(engine)

    # stmt = select(Entry).where(Entry.title == 'test entry')

    # for entry in session.scalars(stmt):
    #     print(entry)

    return {
        "status_code": 200,
        "message": "Hello Outside World!"
    }


## Output
myProject.display_output("Base API URL", DemoApi.output.endpoint)
myProject.display_output("Routes", DemoApi.output.endpoints)

