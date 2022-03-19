from cdev.resources.simple.xlambda import simple_function_annotation

@simple_function_annotation("hello_function")
def hello_world(event, context):
  print('Hello World')
