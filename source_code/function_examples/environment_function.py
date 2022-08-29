import boto3
import os

from cdev.aws.lambda_function import ServerlessFunction
from cdev.aws.s3 import Bucket


myBucket = Bucket("demo_bucket")

s3_client = boto3.client('s3')

@ServerlessFunction("hello_function", permissions=[myBucket.available_permissions.READ_AND_WRITE_BUCKET], environment={"BUCKET_NAME": myBucket.output.bucket_name})
def hello_world(event, context):
  bucket_name = os.environ.get("BUCKET_NAME")
  print(bucket_name)

  print(
    s3_client.list_objects(
      Bucket=bucket_name
    ).get('Contents')
  )

