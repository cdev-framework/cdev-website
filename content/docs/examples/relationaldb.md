{
    "type": "examples",
    "layout": "type",
    "title": "Integrate a RelationalDB",
    "linktitle": "relationaldb",
    "card_icon": "ti-server",
    "card_body": "Learn to create and integrate a Relational DB to store data",
    "weight": "1"
}


# Serverless Functions

Relational Databases have been a flagship part of software development for the past few decades. Through Aurora Databases, you can integrate a Relational DB into your Serverless application. You can create Postgres or MySql compatible databases. 


{{<break 2>}}
### Creating a Relational DB
{{<codesnippet `/source_code/relationaldb_examples/basic_db.py`>}}

Aurora Databases are designed to integrate with Serverless environments by executing SQL over a HTTP tunnel making it more accessible from a Serverless Function environment. You can use third party libraries for access the DB from a Serverless Function using both the standard Python DB API.


{{<break 2>}}
### Connecting to a Relational DB with the standard Python DB API
```
pip install aurora-data-api
```

{{<codesnippet `/source_code/relationaldb_examples/basic_db.py`>}}


{{<break 2>}}
### Accessing the DB from the CLI

