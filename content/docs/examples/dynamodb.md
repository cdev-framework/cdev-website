{
    "type": "examples",
    "layout": "type",
    "title": "Integrate with Dynamodb",
    "linktitle": "dynamodb",
    "card_icon": "ti-server",
    "card_body": "Learn to connect to a Dynamodb database to read and write data",
    "weight": "2"
}


# Integrating with Dynamodb 

Most applications will need a database for storing persistent data, and Dynamodb is the flagship aws nosql database. It is the easiest to get setup and integrated with serverless functions. For more information about how use the database effectively visit the **[aws documentation](https://docs.aws.amazon.com/dynamodb/index.html)**.

{{<break 2>}}
### Create a Dynamodb table for storing emails
{{<codesnippet `/source_code/simple_dynamo_example.py`>}}

### Lambda function that writes a new email 
{{<codesnippet `/source_code/simple_dynamo_example_put.py`>}}


