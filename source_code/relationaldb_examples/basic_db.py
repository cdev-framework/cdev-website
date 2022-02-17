from cdev.resources.simple.relational_db import RelationalDB, db_engine


myDB = RelationalDB(
  "demo_db",
  db_engine.aurora_postgresql,
  "username",
  "password",
  "default_table"
)
