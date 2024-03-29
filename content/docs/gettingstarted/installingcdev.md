{
    "type": "gettingstarted",
    "layout": "type",
    "title": "Installing the Cdev Sdk",
    "linktitle": "gettingstarted", 
    "card_icon": "ti-package",
    "card_body": "Install and configure the Cdev Sdk",
    "weight": "3"
}

# Installing the Cdev Sdk
{{<header_divider>}}

The Cdev Sdk is currently distributed as a Python Package with PyPi, so you can install it using a single command with `pip`. 


{{<tool_tip key="tip" summary="Python Virtual Environments">}}
It is consider a Python development best practice to always work with a [python virtual environment](/docs/gettingstarted/python). The virtual environment will help you avoid dependency conflicts when working with multiple projects. 
{{</tool_tip>}}

{{<break 1>}}

## Installing the SDK

```bash
pip install cdev
```

Once you have installed the package, the CLI tool should be available to your environment. You can check that the tool has properly installed by running the following command.
```bash
cdev -h
```

{{<break 1>}}
## Create Your First Project
{{<tool_tip key="info" summary="Artifacts S3 Bucket">}}
When creating a new project, you will be prompted to link to a `S3 Bucket` for your deployment artifacts. This bucket will be used internally by Cdev to help manage your deployment artifacts. 

If you have `S3 Buckets` in your AWS account, you will be prompted to select which bucket to use. If no bucket is present in the account, you will be prompted to create one. 

The same bucket can be used for managing the deployment artifacts for multiple projects.

{{</tool_tip>}}

{{<break 1>}}

Now that we have the Cdev Sdk installed, we can use it to create a new `Project`.
```bash
cdev init demo-project
```

{{<break 1>}}

{{<tool_tip key="tip" summary="Template Project">}}
By default, Cdev will create your project with some boilerplate files setup to help you get started faster. 
{{</tool_tip>}}


{{<break 1>}}

## Deploying Resources

Cdev helps developers manage and deploy the changes to their `Project` onto the Cloud. You can use the `plan` command to check the current set of changes that would be deployed in the Cloud based on the changes you have made to your `Project`. Since we have not deployed anything in the Cloud for this `Project`, it will show that we want to create the resources defined in the `src/resources.py` file: an `API` and `Serverless Function`.

```bash
cdev plan
```

{{<break 1>}}

When you are ready to deploy your changes, you can use the `deploy` command to deploy the changes. You will be prompted to confirm the set of changes that you are about to deploy. **Note that Cdev will use the currently configured Aws credentials for your environment to deploy the resources**
```bash
cdev deploy
```
{{<break 1>}}

## Testing Serverless Function

Now that we have deployed our `Serverless Function` and `API`, we can test that they have been created in the Cloud. We can execute our function in the Cloud and then retrieve the logs of the `Serverless Function`.

```bash
cdev run function.execute hello_world_comp.hello_world_function
```

**You might have to wait a sec for the logs to process in the cloud**
```bash
cdev run function.logs hello_world_comp.hello_world_function
```
{{<break 1>}}

## Test API Endpoint

We can also check that our `API` has been properly created and configured with our `Serverless Function`. We can use the `Output` command to get the url that the Cloud generated for our `API`.
```bash
cdev output hello_world_comp.api.demoapi.endpoint
```
outputs
```
<your-url>
```

We can now use the `curl` cli tool to call our `API Endpoint` or visit `<your-url>/hello_world` directly in your web browser!
```bash
curl <your-url>/hello_world
```


{{<break 1>}}

## Clean Up


We can delete all the created resources using the `destroy` command.
```bash
cdev destroy
```

{{<break 1>}}

## Next Steps
Now that you have created and deployed your first `API` and `Serverless Function`, you can follow [one of our tutorials to learn how to create a larger project.](/docs/tutorials)

{{<break 2>}}
