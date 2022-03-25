{
    "type": "firstprinciples",
    "layout": "type",
    "title": "Managing a Project",
    "linktitle": "resources", 
    "card_icon": "ti-home",
    "card_body": "Learn how to manage a Cdev Project",
    "weight": "2"
}

Cdev provides abstractions to manage `resource graphs` as `projects`. 

{{<break 1>}}
## Projects
A `project` is a representation that provides a more natural way of conceptualizing a `resource graph`. The `Cdev Sdk` provides a [singleton object](/docs/api/cdev/constructs/project.html) representing the information available for a `project` such as the settings, components, and resource output. You can create a new project using the `cdev init` command. 

{{<tool_tip key="tip" summary="Accessing the Project Object">}}
You can access the `Project` object using the singleton. 
```python
from cdev import Project as cdev_project

myProject = cdev_project.instance()
```
{{</tool_tip>}}


{{<break 1>}}
### Environments
An `environment` is an isolated version of the `project` deployed in the `cloud`. You can create as many `environments` as needed for a project, which enables using individual environments for `feature developement`. By using resources that are pay per use, creating an isolated environment for each `feature` is no longer prohibitevly expensive. 

{{<tool_tip key="tip" summary="Working with Environments">}}
You can create and interact with the different environments of a `project` using the `cdev environment` command.
{{</tool_tip>}}


{{<break 2>}}