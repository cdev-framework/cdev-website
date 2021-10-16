from cdev.resources.simple.api import Api

myApi = Api("cdev_api_name", "api_name")

hello_world_get_route = myApi.route("/hello_world", "GET")