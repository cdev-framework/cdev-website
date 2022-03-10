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

The Cdev Sdk is currently distributed as a Python Package with PyPi, so you can install it using a single command with `pip`. **Note that it is always recommended working with a [python virtual environment](/docs/gettingstarted/python)**

```bash
pip install cdev
```

Once you have installed the package, the CLI tool should be available to your environment. You can check that the tool has properly installed by running the following command.
```bash
cdev -h
```

{{<break 1>}}
## Create Your First Project
Now that we have the Cdev Sdk installed, we can use it to create a new `Project`. We can start our `Project` from a template that will help us get started faster.
```bash
cdev init demo-project --template quick-start
```

{{<break 1>}}

## Deploying Resources

Cdev helps developers manage and deploy the changes to their `Project` onto the Cloud. You can use the `plan` command to check the current set of changes that would be deployed in the Cloud based on the changes you have made to the `Project`. Since we have not deployed anything in the Cloud for this `Project`, it will show that we want to create an `Api` and `Serveless Function`.

```bash
cdev plan
```

{{<break 1>}}

When you are ready to deploy your changes, you can use the `deploy` command to deploy the changes. You will be prompted to confirm the set of changes to you are about to deploy. **Note that Cdev will use the currently configured Aws credentials for your environment to deploy the resources**
```bash
cdev deploy
```
{{<break 1>}}

## Testing Serverless Function

Now that we have deployed our `Serverless Function` and `Api`, we can test that they have been created in the Cloud. We can use `Commands` to execute our function in the Cloud and then retrieve the logs of the `Serverless Function`.

```bash
cdev run function.execute hello_world_comp.hello_world_function
```

**You might have to wait a sec for the logs to process in the cloud**
```bash
$ cdev run function.logs hello_world_comp.hello_world_function
```
{{<break 1>}}

## Test Api Endpoint

We can also check that our `Api` has been properly created and configured with our `Serverless Function`. We must use the `Output` command to get the url that the Cloud generated for our `Api`.
```bash
cdev output hello_world_comp.api.demoapi.endpoint
```
outputs
```
<your-url>
```

{{<break 1>}}

We can now use the `curl` cli tool to call our `Api Endpoint` or visit `<your-url>/hello_world` directly in your web browser!
```bash
$ curl <your-url>/hello_world
```


{{<break 1>}}

## Clean Up


We can delete all the created resources using the `destroy` command.
```bash
$ cdev destroy
```

{{<break 1>}}

## Next Steps
Now that you have created you deployed your first `Api` and `Serverless Function`, you can follow [one of our tutorials to learn how to create larger project](/docs/tutorials)