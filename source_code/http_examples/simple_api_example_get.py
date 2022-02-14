from cdev.resources.simple.api import Api, route_verb

myApi = Api("demoApi")

hello_world_get_route = myApi.route("/hello_world", route_verb.GET)