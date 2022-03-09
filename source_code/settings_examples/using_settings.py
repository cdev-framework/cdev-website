

from cdev import Project as cdev_project

from src.project_settings import CustomSettings

myProject = cdev_project.instance()

mySettings: CustomSettings =  myProject.settings


print(mySettings.SOME_KEY)
