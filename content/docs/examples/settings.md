{
    "type": "examples",
    "layout": "type",
    "title": "Project Settings",
    "linktitle": "settings",
    "card_icon": "ti-settings",
    "card_body": "Learn to create and modify your Project Settings",
    "weight": "2"
}


# Create and Update Project Settings

Cdev provides a mechanism to manage settings per `Environment` that affect how your resources are generated. These settings can be used to provide different values to the framework for different `Environments`. 

We built our settings starting from the [Pydantic Settings module](https://pydantic-docs.helpmanual.io/usage/settings/) to provide a relatively type safe mechanism for working with settings, and then we added an additional workflow inspired by the [Django Settings module](https://docs.djangoproject.com/en/4.0/topics/settings/). 


{{<break 1>}}
## Creating and Setting a Custom Settings Class
In your `src` folder, create a new file called `project_settings.py`. Then copy the following code into the file.
{{<codesnippet `/source_code/settings_examples/basic_settings.py`>}}

Then to set this as the `Settings` for the current `Environment`, run the following command. 
```
cdev environment settings_information --key base_class --new-value src.project_settings.CustomSettings
```

This command sets the `CustomSettings` class found in the `src.project_settings` module as the default class to use for your `Environment` Settings. Note that the structure of the `--new-value` parameter is `<python_module>.<class_name>`, where the `python_module` must be available on the [python search path](https://docs.python.org/3/tutorial/modules.html#the-module-search-path) and contain the class `class_name` that is a descendant of `core.constructs.settings.Settings`.


{{<break 1>}}
## Using your Setting
You can access the Settings via the `Global Project` object.

{{<codesnippet `/source_code/settings_examples/using_settings.py`>}}

**Note you can directly reference a property (`myProject.settings.SOME_KEY`) without storing the settings in the `mySettings` variable, but this step allows us to add a typing hint to help clarify the values we are using.**


{{<break 1>}}
## Modifying a Custom Setting Class
All the custom Settings will derive from the Core Constructs `Settings` class, which itself derives from the Pydantic `BaseSettings` Model. Therefore, we can add additional settings by adding properties to the class with the defining type conditions. You must derive from the `Settings` class to make sure that the needed settings for the framework to work are available. **Note that all properties should be all uppercase with '_' to separate words**

{{<codesnippet `/source_code/settings_examples/basic_settings_properties.py`>}}


## Setting the Values 

The ordering of the precedent for settings values is (from lowest to highest):
1. The default field values for the Settings model.
2. Variables loaded from the secrets directory.
3. Environment variables.
4. Variable from the Dynamic Settings Modules.


{{<break 1>}}
### Defaults from the Settings Model
When creating a property, it is recommended to either provide a value as the default value or denote the property as `Optional`.  
{{<codesnippet `/source_code/settings_examples/basic_settings_properties.py`>}}


### Secret Values
When a Cdev `Environment` is created, a directory (settings/secrets/<your_environment>_secrets) is added to store the secret values for that `Environment`. This directory is used when loading your settings module as the [Secrets Directory for the Pydantic Base Settings](https://pydantic-docs.helpmanual.io/usage/settings/#secret-support). Following the Pydantic Documentation to set a secret, create a file name `cdev_<property>` and add the value as the only thing in the file.  **Note that you should make sure these files are not stored in a public repository. You can add a .gitignore to block these files by following the [getting start guide](/docs/gettingstarted#ignorefile)**

{{<break 1>}}
Create:
```
settings/secrets/<your_environment>_secrets/cdev_some_key
```
**Note the file needs be have the `cdev_` prefix and also the property is written in lower case.**
{{<break 2>}}
Then add to the file:
```
somesecretvalue
```

{{<break 1>}}
### Environment variables
You can use standard Environment Variables to set your settings values via [Pydantic Base Settings support for Environment Variables](https://pydantic-docs.helpmanual.io/usage/settings/#parsing-environment-variable-values). 

```
export CDEV_SOME_KEY=somevalue
```
**Note the variables needs be have the `CDEV_` prefix**

{{<break 1>}}
### Variable from the Dynamic Settings Modules
For more complex values, it can be helpful to write the values directly in Python. We felt that the Django framework handled this in an elegant way, so we modeled our system after theirs. Each Cdev `Environment` comes with a python module that can be used to load complex values. You can set properties by setting them as variables in the module. **Note we do NOT need to use the `cdev` prefix when setting the properties**

{{<codesnippet `/source_code/settings_examples/dynamic_settings.py`>}}


As mentioned in the [Django Settings documentation](https://docs.djangoproject.com/en/4.0/topics/settings/#the-basics), the file is a valid python module therefor:
1. It doesn’t allow for Python syntax errors.

2. It can assign settings dynamically using normal Python syntax. For example:
```
ANOTHER_KEY = "somevalue".capitalize()
```

3. It can import values from other settings files.

Each Cdev `Environment` has it's own dedicated dynamic module in the `settings/` folder, but there is also a `base_settings.py` module that is applied for all environments. This should be used to set values that are the same for all `Environments`.

{{<break 1>}}
### Extra Notes
Note that the life cycle of a `Setting` class is that it is initialized as a child of the Pydantic `Base Settings` then the Dynamic Setting Modules are applied. This means if you have a required property that is only set via a Dynamic Setting Module, it will fail to initially create the class because of a `Pydantic` validation error. This can be avoided be either providing a default value when creating the `Custom Setting Class` or making the property as `Optional`.














