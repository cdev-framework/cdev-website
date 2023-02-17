
from cdev.aws.frontend import Site
from cdev import Project as cdev_project

myProject = cdev_project.instance()


certificate_arn = "<certificate_arn>"
site_url = "demo-site.io"

myFrontend = Site("demo-site", index_document='index.html', ssl_certificate_arn=certificate_arn, domain_name=site_url)

myProject.display_output("Static Site URl", myFrontend.output.site_url)