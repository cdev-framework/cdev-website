{
    "type": "examples",
    "layout": "type",
    "title": "Integrate RelationalDBs",
    "linktitle": "relationaldb",
    "card_icon": "ti-server",
    "card_body": "Learn to create and integrate a Relational DB",
    "weight": "4",
    "tags":["SQL", "PostgreSQL", "Alembic", "SQL Alchemy", "ORM"]
}


# Serverless Relational Databases
{{<header_divider>}}

Relational Databases have been a flagship part of software development for the past few decades. With [Aws Aurora Databases](https://aws.amazon.com/rds/aurora/), you can integrate a Relational DB with your `Serverless Application`. You can create Postgres or MySql compatible databases that scale with your application

{{<tool_tip key="info" summary="Key Differences">}}
Aurora Databases are designed to integrate with Serverless environments by executing SQL over a HTTP tunnel making it more accessible from a `Serverless Function`. You can use [third party libraries](https://github.com/cloud-utils/aurora-data-api) to access the DB from a `Serverless Function` using both the standard Python DB API and SlqAlchemy.
{{</tool_tip>}}

{{<break 1>}}
## Creating a Relational DB
{{<codesnippet `/source_code/relationaldb_examples/basic_db.py`>}}
{{<tool_tip key="tip" summary="Database Variables Tip">}}
If starting from the quick-start template place the code snippet from above in your `src/hello_world/resources.py` file.
{{</tool_tip>}}

{{<break 2>}}
## Accessing the DB from the CLI
Once you have created a DB, the fastest way to access the DB is through an interactive session on your CLI. You can open a interactive session using the following Cdev Command. This shell is designed to be a simple emulation of [psql](https://www.postgresql.org/docs/13/app-psql.html) and [mysql](https://dev.mysql.com/doc/refman/8.0/en/mysql.html). 
```bash
cdev run relationaldb.shell <component_name>.<resource_name>
```

{{<break 1>}}
### Create a Table
**Mysql**
```sql
CREATE TABLE users(id INT NOT NULL AUTO_INCREMENT,name VARCHAR(100), PRIMARY KEY ( id ));
```
**Postgres**
```sql
CREATE TABLE users( id serial PRIMARY KEY, name VARCHAR ( 50 ) );
```
{{<break 1>}}
### Add Row
```sql
INSERT INTO users(id, name) VALUES (18,'Paul Atreides');
```
{{<break 1>}}
### Query the Table
```sql
select * from users;
```
{{<break 1>}}
### Transactions
**Start Transaction**
```sql
BEGIN
```
**Commit Transaction**
```sql
COMMIT
```
**Rollback Transaction**
```sql
ROLLBACK
```
**Quit Interactive Shell**
```sql
quit
```

{{<break 2>}}
## Connecting to a Relational DB with Python

Although there are some [underlying architectural decisions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/data-api.html) that make these db's optimized for use in a Serverless Computing environment, we can access them in our code using the standard [Python Database Api](https://peps.python.org/pep-0249/) and [SqlAlchemy](https://www.sqlalchemy.org/). To simplify the use of the these standard Api's, we will be using two third party packages: [aurora-data-api](https://github.com/cloud-utils/aurora-data-api) and [sqlalchemy-aurora-data-api](https://github.com/cloud-utils/sqlalchemy-aurora-data-api). These packages handle the hard work of creating the standardized Api's for our created databases and exposing them in packages that are optimized for Serverless Development. 

```bash
pip install aurora-data-api sqlalchemy-aurora-data-api
```

{{<break 1>}}
### Python Database Api
Using `aurora-data-api` to access your DB via the `Python Database Api` is the fastest way to get started. 
{{<codesnippet `/source_code/relationaldb_examples/standard_api_db.py`>}}

**Execute the function**
```bash
cdev run function.execute hello_world_comp.db_handler
```
**Check the logs**
```bash
cdev run function.logs hello_world_comp.db_handler
```

{{<tool_tip key="info" summary="How to use the Python Database API">}}
For more information on how to use the `Python Database Api` checkout this [tutorial](https://philvarner.github.io/pages/novice-python3-db-api.html) 
{{</tool_tip>}}

{{<break 1>}}
### SqlAlchemy Api
The SqlAlchemy Api allows you to execute sql directly or use an Object-Relational Mapper (ORM) to access your DB. 

#### Direct Access
{{<codesnippet `/source_code/relationaldb_examples/sqlalchemy_basic.py`>}}

**Execute the function**
```bash
cdev run function.execute hello_world_comp.db_handler
```
**Check the logs**
```bash
cdev run function.logs hello_world_comp.db_handler
```


{{<break 1>}}
### SqlAlchemy ORM
One of the main benefits of SqlAlchemy is the option to use it's [powerful ORM](https://www.fullstackpython.com/sqlalchemy.html). To get the full use of the ORM, we can pair it with the [alembic](https://alembic.sqlalchemy.org) library to automatically generate the migration files when we update our models.

Starting from the `quick-start` template, add a `relational_db` to your resources.
```bash
cdev init orm-demo --template quick-start
```

Update your `src/hello_world/resources.py` file to 
{{<codesnippet `/source_code/relationaldb_examples/sqlalchemy_orm_resource.py`>}}

Now we can deploy our resources
```bash
cdev deploy
```

{{<break 1>}}
**Next, we are going to create our models.** Install `sqlalchemy_aurora_data_api`.

```bash
pip install sqlalchemy_aurora_data_api
```
Then, create a `src/hello_world/models.py` file and add the following code:

{{<codesnippet `/source_code/relationaldb_examples/sqlalchemy_models.py`>}}

Now we are going to install and configure `alembic`.

```bash
pip install alembic
```
{{<tool_tip key="tip" summary="Alembic Library">}}
`Alembic` is one of the best in class tools for working with SqlAlchemy. You can learn more about the tool from [their official documentation](https://alembic.sqlalchemy.org/en/latest/).
{{</tool_tip>}}

Initialize the needed files for `alembic` using the following command. We will need to edit some of the generated files to connect to our db.
```bash
alembic init src/alembic
```


In the `src/alembic/eny.py` file, import the base declarative model from the `models.py` file, and set that as the `target_metadata` variable on line 21.

```python
from src.hello_world.models import Base
```

```python
target_metadata = Base.metadata
```

Then, change `line 62` to use `connect args` and our database engine.
```python
connectable = create_engine(
        postgres_database_engine,
        echo=True,
        connect_args=dict(aurora_cluster_arn=cluster_arn, secret_arn=secret_arn)
    )
```

Above the `run_migrations_online` function declaration on `line 55`, add the follow lines and uncomment the database engine based on your type of db engine.

```python
import os
from sqlalchemy import create_engine

cluster_arn = os.environ.get("CLUSTER_ARN")
secret_arn = os.environ.get("SECRET_ARN")
database_name = os.environ.get("DB_NAME")

#postgres_database_engine = f'postgresql+auroradataapi://:@/{database_name}'
#mysql_database_engine = f'mysql+auroradataapi://:@/{database_name}'
```

Now to make sure our values are registered in the `env.py` script, we need to set our environments. 

```bash
export SECRET_ARN=$(cdev output --value hello_world_comp.relationaldb.demo_db.secret_arn)
```
```bash
export CLUSTER_ARN=$(cdev output --value hello_world_comp.relationaldb.demo_db.cluster_arn)
```
```bash
export DB_NAME=<db_name>
```
{{<break 1>}}

You should now be able to create automated migrations. 

{{<tool_tip key="warning" summary="Auto Generation limits">}}
You should familiarize yourself with the [limits of alembic auto generation](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect) and **ALWAYS** confirm the changes before applying them.
{{</tool_tip>}}

```bash
alembic revision --autogenerate -m "Added users table"
```
Apply the migration with the `upgrade` command. This will create our `Users` Table.
```bash
alembic upgrade head
```

{{<break 1>}}
Lets now connect to our DB and add an User.
```bash
cdev run relationaldb.shell hello_world_comp.demo_db
```
```sql
BEGIN
```
```sql
INSERT INTO users(id, name) VALUES (1,'Paul Atreides');
```
```sql
COMMIT
```
```bash
quit
```


{{<break 1>}}
Now we can update our `src/hello_world/resources.py` to have our `Serverless Function` use the SqlAlchemy ORM to access our Database. Replace your `src/hello_world/resources.py` with the following code.

{{<codesnippet `/source_code/relationaldb_examples/sqlalchemy_orm_resources_updated.py`>}}

Then deploy the changes to the function
```bash
cdev deploy
```

run the deployed function
```bash
cdev run function.execute hello_world_comp.hello_world_function
```

Check the logs from the function
```bash
cdev run function.logs hello_world_comp.hello_world_function
```

{{<break 2>}}
