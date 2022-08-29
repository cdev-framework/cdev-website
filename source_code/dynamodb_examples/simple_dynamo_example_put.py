import json
import os
import time

import boto3

from cdev.aws.dynamodb import Table, AttributeDefinition, KeyDefinition, key_type, attribute_type
from cdev.aws.lambda_function import ServerlessFunction


myAttributes = [
  AttributeDefinition("email", attribute_type.S),
  AttributeDefinition("date_created", attribute_type.S)
]

myKeys = [
  KeyDefinition("email", key_type.HASH),
  KeyDefinition("date_created", key_type.RANGE)
]


EmailTable = Table("EmailRegistryTable", myAttributes, myKeys)


client = boto3.resource('dynamodb')
table_name = os.environ.get("TABLENAME")


@ServerlessFunction("email_adder", environment={"TABLENAME": EmailTable.output.table_name}, permissions=[EmailTable.available_permissions.READ_AND_WRITE_TABLE])
def add_email_handler(event, context):
    print(event)

    # Load the body of the request into a data obj    
    data = event.get("body")

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    now = int( time.time() )

    print(f"ADDING: {first_name}; {last_name}; {email}")
    table = client.Table(table_name)
  
    table.put_item(
        Item={
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'date_created': str(now)
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Email Added",
            "success": True
        }),
        "headers":{
            "Access-Control-Allow-Origin": "*",
            "mode": "no-cors"
        }
    }
@ServerlessFunction("scan", environment={"TABLENAME": EmailTable.output.table_name}, permissions=[EmailTable.available_permissions.READ_AND_WRITE_TABLE])
def scan(event, context):
    table = client.Table(table_name)
    response=table.scan()
    response['Items']
    print(response)