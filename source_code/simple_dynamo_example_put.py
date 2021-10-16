import json
import os
import time

import boto3

from cdev.resources.simple.table import Table, key_type, attribute_type, simple_table_output
from cdev.resources.simple.xlambda import simple_lambda_function_annotation as simple_lambda_function

MyAttributes = [
    {"AttributeName": "email", "AttributeType": attribute_type.S},
    {"AttributeName": "date_created", "AttributeType": attribute_type.S},
]

MyKeys = [
    {"AttributeName": "email", "KeyType": key_type.HASH},
    {"AttributeName": "date_created", "KeyType": key_type.RANGE},
]


EmailTable = Table("EmailRegistryTable", "new_email_registry", MyAttributes, MyKeys)


client = boto3.resource('dynamodb')
table_name = os.environ.get("TABLENAME")


@simple_lambda_function("email_adder", Environment={"TABLENAME": EmailTable.from_output(simple_table_output.table_name)}, permissions=[EmailTable.permissions.READ_AND_WRITE_TABLE])
def add_email_handler(event, context):
    print(event)

    # Load the body of the request into a data obj    
    data = json.loads(event.get("body"))

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
