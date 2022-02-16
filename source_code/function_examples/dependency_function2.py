import pandas

from cdev.resources.simple.xlambda import simple_function_annotation
from cdev.resources.simple.object_store import Bucket


@simple_function_annotation("hello_function")
def hello_world(event, context):
  print(pandas)

  print("Hey friends")



@simple_function_annotation("hello_function2")
def hello_world2(event, context):
  print(pandas)

  print("Hey friends from a different function")