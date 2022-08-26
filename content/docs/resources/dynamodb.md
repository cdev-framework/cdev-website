{
    "type": "examples",
    "layout": "type",
    "title": "Dynamodb Table",
    "linktitle": "dynamodb",
    "card_icon": "ti-server",
    "card_body": "Learn to connect to a Dynamodb database",
    "weight": "4"
}


# Integrating with DynamoDB 
{{<header_divider>}}

Most applications will need a database for storing persistent data, and DynamoDB is the flagship Aws NoSql database. It is the easiest to get setup and integrated with Serverless Functions. For more information about how to structure and use the database visit the **[Aws documentation](https://docs.aws.amazon.com/dynamodb/index.html)**.

{{<youtube "https://www.youtube.com/embed/8N8kVIEhG1A">}}

{{<break 1>}}
## Create a DynamoDB table for storing emails
The following code snippet shows and example of how you can set the attributes and keys for a DynamoDB table and create the table.
{{<codesnippet `/source_code/dynamodb_examples/simple_dynamo_example.py`>}}


{{<break 1>}}
## Write data from a Serverless Function
Start a new Cdev project and replace the code in the `src/hello_world/resources.py` file with the following code.
{{<codesnippet `/source_code/dynamodb_examples/simple_dynamo_example_put.py`>}}
Deploy the resources.
```bash
cdev deploy
```
Execute the function.
```bash
cdev run function.execute hello_world_comp.email_adder --event-data "{\"body\":{\"first_name\":\"Paul\",\"last_name\":\"Atreides\",\"email\":\"Muaddib@dune.com\"}}"
```
You can run the function above a few times after making changes to the email address (and other fields if you wish, but the email is mandatory as it is the primary key), to add more entries to your database and then execute the scan function with the command below:
```bash
cdev run function.execute hello_world_comp.scan
```
Check the function logs
```bash
cdev run function.logs hello_world_comp.scan
```
You will see a list of items that are in your DynamoDB table in your terminal.
