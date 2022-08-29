import os
import boto3

from cdev.aws.s3 import Bucket
from cdev.aws.lambda_function import ServerlessFunction


myBucket = Bucket("demo_bucket")


s3_client = boto3.client('s3')

@ServerlessFunction("write_function", environment={"BUCKET_NAME": myBucket.output.bucket_name}, permissions=[myBucket.available_permissions.READ_AND_WRITE_BUCKET])
def write_object(event, context):

  bucket_name = os.environ.get('BUCKET_NAME')

  print(
    s3_client.put_object(Body='Text Test', Bucket=bucket_name, Key="filename.txt")
  )