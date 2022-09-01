import json

from cdev.aws.api import Api
from cdev.aws.lambda_function import ServerlessFunction

from cdev import Project as cdev_project

myProject = cdev_project.instance()

myApi = Api("demoApi")

hello_world_get_route = DemoApi.route("/hello_world", "GET")