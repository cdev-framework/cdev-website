import boto3

from cdev.resources.simple.xlambda import simple_function_annotation
from cdev.resources.simple.object_store import Bucket


myBucket = Bucket("demo_bucket")

s3_client = boto3.client('s3')

@simple_function_annotation("hello_function", permissions=[myBucket.available_permissions.READ_AND_WRITE_BUCKET])
def hello_world(event, context):
  bucket_name = "BUCKET_NAME"

  print(
    s3_client.list_objects(
      Bucket=bucket_name
    ).get('Contents')
  )

