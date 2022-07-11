from cdev.resources.simple.relational_db import RelationalDB, db_engine

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
