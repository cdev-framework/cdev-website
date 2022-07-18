{
    "type": "examples",
    "layout": "type",
    "title": "Project Settings",
    "linktitle": "settings",
    "card_icon": "ti-settings",
    "card_body": "Learn to create and modify your Project Settings",
    "weight": "3"
}


# Create and Update Project Settings
{{<header_divider>}}

Cdev provides a mechanism to manage settings per `Environment`. These settings can be used to provide different values to the framework for different `Environments`.

We built our settings starting from the [Pydantic Settings module](https://pydantic-docs.helpmanual.io/usage/settings/) to provide a type safe mechanism for working with settings, and then we added an additional workflow inspired by the [Django Settings module](https://docs.djangoproject.com/en/4.0/topics/settings/) to provide flexibility when working with complex types (List, Dict, etc). 


{{<break 1>}}
## Creating and Setting a Custom Settings Class
In your `src` folder, create a new file called `project_settings.py`. Then copy the following code into the file.
{{<codesnippet `/source_code/settings_examples/basic_settings.py`>}}

Set this as the `Settings` for the current `Environment` using the following command. 
```bash
cdev environment settings_information --key base_class --new-value src.project_settings.CustomSettings
```

This command sets the `CustomSettings` class found in the `src.project_settings` module as the default class to use for your `Environment` Settings. 

{{<tool_tip key="info" summary="Structure of Values">}}
Note that the structure of the `--new-value` parameter is `<python_module>.<class_name>`, where the `python_module` must be available on the [python search path](https://docs.python.org/3/tutorial/modules.html#the-module-search-path) and contain the class `class_name` that is a descendant of `core.constructs.settings.Settings`.
{{</tool_tip>}}


{{<break 1>}}
## Using your Setting
You can access the Settings via the `Global Project` object.

{{<codesnippet `/source_code/settings_examples/using_settings.py`>}}

{{<tool_tip key="info" summary="Type Hints">}}
You can directly reference a property (`myProject.settings.SOME_KEY`) without storing the settings in the `mySettings` variable, but this step allows us to add a typing hint to help clarify the values we are using.
{{</tool_tip>}}

{{<break 1>}}
## Modifying a Custom Setting Class
All the custom setting classes will derive from the Core Constructs `Settings` class, which itself derives from the Pydantic `BaseSettings` Model. Therefore, we can add additional settings by adding properties to the class with the defining type conditions. You must derive from the `Settings` class to make sure that the needed settings for the framework to work are available. 


{{<codesnippet `/source_code/settings_examples/basic_settings_properties.py`>}}

{{<tool_tip key="info" summary="Property Names">}}
All properties should be all uppercase with '_' to separate words
{{</tool_tip>}}


{{<break 1>}}
## Setting the Values 

The ordering of the precedent for settings values is (from lowest to highest):
1. The default field values for the Settings model.
2. Variables loaded from the secrets directory.
3. Environment variables.
4. Variables from the Dynamic Settings Modules.


{{<break 1>}}
### Defaults from the Settings Model
When creating a property, it is recommended to either provide a value as the default value or denote the property as `Optional`.  
{{<codesnippet `/source_code/settings_examples/basic_settings_properties.py`>}}

{{<break 1>}}
### Secret Values
When a Cdev `Environment` is created, a directory (settings/secrets/<your_environment>_secrets) is added to store the secret values for that `Environment`. This directory is used when loading your settings module as the [Secrets Directory for the Pydantic Base Settings](https://pydantic-docs.helpmanual.io/usage/settings/#secret-support). Following the Pydantic Documentation to set a secret, create a file name `cdev_<property>` and add the value as the only thing in the file.  

{{<tool_tip key="warning" summary="Storing Secrets">}}
You should make sure these files are not stored in a public repository. You can add a .gitignore to block these files by using the [example .gitignore](/docs/examples/git/#gitignore)
{{</tool_tip>}}

Create:
```
settings/secrets/<your_environment>_secrets/cdev_some_key
```
{{<tool_tip key="info" summary="File Name">}}
The file needs to have the `cdev_` prefix and the property written in lower case.
{{</tool_tip>}}

Then add to the file:
```
somesecretvalue
```

{{<break 1>}}
### Environment variables
You can use standard Environment Variables to set your settings values via [Pydantic Base Settings support for Environment Variables](https://pydantic-docs.helpmanual.io/usage/settings/#parsing-environment-variable-values). 

```bash
export CDEV_SOME_KEY=somevalue
```

{{<tool_tip key="info" summary="Variable Names">}}
The variables needs be have the `CDEV_` prefix.
{{</tool_tip>}}


{{<break 1>}}
### Variable from the Dynamic Settings Modules
For more complex values, it can be helpful to write the values directly in Python. We felt that the Django framework handled this in an elegant way, so we modeled our system after theirs. Each Cdev `Environment` comes with a python module that can be used to load complex values. You can set properties by setting them as variables in the module.

{{<tool_tip key="info" summary="Variable Names">}}
Note we do NOT need to use the `cdev` prefix when setting the properties
{{</tool_tip>}}

{{<codesnippet `/source_code/settings_examples/dynamic_settings.py`>}}


As mentioned in the [Django Settings documentation](https://docs.djangoproject.com/en/4.0/topics/settings/#the-basics), the file is a valid python module therefor:
1. It doesn’t allow for Python syntax errors.

2. It can assign settings using normal Python syntax. For example:
```python
ANOTHER_KEY = "somevalue".capitalize()
```

3. It can import values from other settings files.

Each Cdev `Environment` has it's own dedicated dynamic module in the `settings/` folder, but there is also a `base_settings.py` module that is applied for all environments. This should be used to set values that are the same for all `Environments`.


{{<tool_tip key="warning" summary="Settings Lifecycle">}}
Note that the life cycle of a `Setting` class is that it is initialized as a child of the Pydantic `Base Settings` then the Dynamic Setting Modules are applied. This means if you have a required property that is only set via a Dynamic Setting Module, it will fail to initially create the class because of a `Pydantic` validation error. This can be avoided by either providing a default value when creating the `Custom Setting Class` or making the property as `Optional`.

{{</tool_tip>}}
{{<break 1>}}

## Working In Teams
When working on a project with a team of developers it is wise for each developer to have their own environment during development.  Creating a new environment is as simple as running the following command:
```bash
cdev environment create <name of your environment>
```
After you create your environment you can switch to it by running the following command:
```bash
cdev environment set <name of your environment>
```
Whenever you change environments you need to update your settings by running the following command:
```bash
cdev environment settings_information --key base_class --new-value src.project_settings.CustomSettings
```

{{<tool_tip key="tip" summary="Selecting Environments">}}
At any point you can check what environments are available by running the following command:
```bash
cdev environment ls
```
There will be an arrow pointing to which environment is currently being used if one is set.
{{</tool_tip>}}








