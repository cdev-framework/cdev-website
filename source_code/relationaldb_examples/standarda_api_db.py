from cdev.resources.simple.relational_db import RelationalDB, db_engine


myDB = RelationalDB(
  "demo_db",
  db_engine.aurora_postgresql,
  "username",
  "password",
  "default_table"
)

@simple_function_annotation("demo", environment={"CLUSTER_ARN": myDB.output.cluster_arn, "SECRET_ARN":myDB.output.secret_arn}, permissions=[myDB.available_permissions.DATABASE_ACCESS,myDB.available_permissions.SECRET_ACCESS])
def hello_world(event, context):

    cluster_arn = os.environ.get("CLUSTER_ARN")
    secret_arn = os.environ.get("SECRET_ARN")
    
    
    with aurora_data_api.connect(aurora_cluster_arn=cluster_arn, secret_arn=secret_arn, database="default_table") as conn:
        with conn.cursor() as cursor:
            cursor.execute("select * from pg_catalog.pg_tables")
            print(cursor.fetchall())