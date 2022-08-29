from cdev.aws.lambda_function import ServerlessFunction

@ServerlessFunction("hello_function")
def hello_world(event, context):
  print('Hello World')
