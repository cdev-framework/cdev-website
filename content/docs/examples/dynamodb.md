{
    "type": "examples",
    "layout": "type",
    "title": "Integrate NoSql DBs",
    "linktitle": "dynamodb",
    "card_icon": "ti-server",
    "card_body": "Learn to connect to a Dynamodb database to read and write data",
    "weight": "3"
}


# Integrating with Dynamodb 

Most applications will need a database for storing persistent data, and Dynamodb is the flagship Aws nosql database. It is the easiest to get setup and integrated with Serverless Functions. For more information about how use the database effectively visit the **[aws documentation](https://docs.aws.amazon.com/dynamodb/index.html)**.

{{<break 2>}}
### Create a Dynamodb table for storing emails
{{<codesnippet `/source_code/dynamodb_examples/simple_dynamo_example.py`>}}

### Write data from a Serverless Function
{{<codesnippet `/source_code/dynamodb_examples/simple_dynamo_example_put.py`>}}


```
cdev run function.execute hello_world_comp.email_adder --event-data "{\"body\":{\"first_name\":\"Paul\",\"last_name\":\"Atreides\",\"email\":\"Muaddib@dune.com\"}}"
```

