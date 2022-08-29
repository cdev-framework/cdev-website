import pandas

from cdev.aws.lambda_function import ServerlessFunction
from cdev.aws.s3 import Bucket


@ServerlessFunction("hello_function")
def hello_world(event, context):
  print(pandas)

  print("Hey friends") 