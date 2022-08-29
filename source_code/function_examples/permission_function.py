import boto3

from cdev.aws.lambda_function import ServerlessFunction
from cdev.aws.s3 import Bucket


myBucket = Bucket("demo_bucket")

s3_client = boto3.client('s3')

@ServerlessFunction("hello_function", permissions=[myBucket.available_permissions.READ_AND_WRITE_BUCKET])
def hello_world(event, context):
  bucket_name = "BUCKET_NAME"

  print(
    s3_client.list_objects(
      Bucket=bucket_name
    ).get('Contents')
  )

