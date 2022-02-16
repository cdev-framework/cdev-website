import boto3
import os

from cdev.resources.simple.xlambda import simple_function_annotation
from cdev.resources.simple.object_store import Bucket


myBucket = Bucket("demo_bucket")

s3_client = boto3.client('s3')

@simple_function_annotation("hello_function", permissions=[myBucket.available_permissions.READ_AND_WRITE_BUCKET], environment={"BUCKET_NAME": myBucket.output.bucket_name})
def hello_world(event, context):
  bucket_name = os.environ.get("BUCKET_NAME")
  print(bucket_name)

  print(
    s3_client.list_objects(
      Bucket=bucket_name
    ).get('Contents')
  )

