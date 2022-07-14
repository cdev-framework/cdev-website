import os

import sqlalchemy_aurora_data_api
from sqlalchemy import create_engine

from cdev.resources.simple.relational_db import RelationalDB, db_engine
from cdev.resources.simple.xlambda import simple_function_annotation


myDB = RelationalDB(
  cdev_name="demo_db",
  engine=db_engine.aurora_postgresql,
  username="username",
  password="password",
  database_name="default_table"
)


cluster_arn = os.environ.get("CLUSTER_ARN")
secret_arn = os.environ.get("SECRET_ARN")
database_name = os.environ.get("DB_NAME")

sqlalchemy_aurora_data_api.register_dialects()
    
engine = create_engine(f'postgresql+auroradataapi://:@/{db_name}',
                    echo=True,
                    connect_args=dict(aurora_cluster_arn=cluster_arn, secret_arn=secret_arn))
    

@simple_function_annotation("db_handler", environment={"CLUSTER_ARN": myDB.output.cluster_arn, "SECRET_ARN":myDB.output.secret_arn, "DB_NAME": db_name}, permissions=[myDB.available_permissions.DATABASE_ACCESS, myDB.available_permissions.SECRET_ACCESS])
def connect_to_db(event, context):
    print(sqlalchemy_aurora_data_api)

    #sql_stmt = "SHOW DATABASES;"

    #sql_stmt = "select * from pg_catalog.pg_tables"

    with engine.connect() as conn:
        for result in conn.execute(sql_stmt):
            print(result)