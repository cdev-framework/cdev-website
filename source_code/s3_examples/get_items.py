import os
import boto3

from cdev.aws.s3 import Bucket
from cdev.aws.lambda_function import ServerlessFunction


myBucket = Bucket("demo_bucket")


s3_client = boto3.client('s3')

@ServerlessFunction("read_function", environment={"BUCKET_NAME": myBucket.output.bucket_name}, permissions=[myBucket.available_permissions.LIST_BUCKET])
def read_object(event, context):

  bucket_name = os.environ.get('BUCKET_NAME')

  print(
    s3_client.list_objects(
      Bucket=bucket_name
    ).get('Contents')
  )