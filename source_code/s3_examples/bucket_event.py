import os
import boto3

from cdev.resources.simple.object_store import Bucket, Bucket_Event_Type
from cdev.resources.simple.xlambda import simple_function_annotation


myBucket = Bucket("demo_bucket")
myBucket_event = myBucket.create_event_trigger(Bucket_Event_Type.Object_Created)


s3_client = boto3.client('s3')


@simple_function_annotation("read_function", events=[myBucket_event], environment={"BUCKET_NAME": myBucket.output.bucket_name}, permissions=[myBucket.available_permissions.LIST_BUCKET])
def read_object(event, context):

  bucket_name = os.environ.get('BUCKET_NAME')

  result = s3_client.list_objects(Bucket=bucket_name).get('Contents')

  print(result)

  return {"message": str(result)}