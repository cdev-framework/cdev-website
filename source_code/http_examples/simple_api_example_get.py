from cdev.aws.api import Api

myApi = Api("demoApi")

hello_world_get_route = myApi.route("/hello_world", GET)