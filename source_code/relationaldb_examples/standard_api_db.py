import os

import aurora_data_api

from cdev.aws.relational_db import RelationalDB, db_engine
from cdev.aws.lambda_function import ServerlessFunction


myDB = RelationalDB(
  cdev_name="demo_db",
  engine=db_engine.aurora_postgresql,
  username="username",
  password="password",
  database_name="default_table"
)


@ServerlessFunction("db_handler", environment={"CLUSTER_ARN": myDB.output.cluster_arn, "SECRET_ARN":myDB.output.secret_arn, "DB_NAME": db_name}, permissions=[myDB.available_permissions.DATABASE_ACCESS,myDB.available_permissions.SECRET_ACCESS])
def connect_to_db(event, context):

    cluster_arn = os.environ.get("CLUSTER_ARN")
    secret_arn = os.environ.get("SECRET_ARN")
    database_name = os.environ.get("DB_NAME")
    
    with aurora_data_api.connect(aurora_cluster_arn=cluster_arn, secret_arn=secret_arn, database=database_name) as conn:
        with conn.cursor() as cursor:

            # mysql uncomment follow line
            # cursor.execute("SHOW DATABASES;")

            # postgres uncomment follow line
            #cursor.execute("select * from pg_catalog.pg_tables")
            print(cursor.fetchall())