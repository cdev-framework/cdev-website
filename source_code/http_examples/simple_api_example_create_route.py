import json

from cdev.resources.simple.api import Api
from cdev.resources.simple.xlambda import simple_function_annotation

from cdev import Project as cdev_project

myProject = cdev_project.instance()

myApi = Api("demoApi")

hello_world_get_route = DemoApi.route("/hello_world", "GET")