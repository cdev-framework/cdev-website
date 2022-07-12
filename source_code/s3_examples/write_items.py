import os
import boto3

from cdev.resources.simple.object_store import Bucket
from cdev.resources.simple.xlambda import simple_function_annotation


myBucket = Bucket("demo_bucket")


s3_client = boto3.client('s3')

@simple_function_annotation("read_function", environment={"BUCKET_NAME": myBucket.output.bucket_name}, permissions=[myBucket.available_permissions.READ_AND_WRITE_BUCKET])
def read_object(event, context):

  bucket_name = os.environ.get('BUCKET_NAME')

  print(
    s3_client.put_object(Body='Text Test', Bucket=bucket_name, Key="filename.txt")
  )