{
    "type": "examples",
    "layout": "type",
    "title": "Create Serverless Functions",
    "linktitle": "functions",
    "card_icon": "ti-infinite",
    "card_body": "Learn to create and integrate Serverless functions",
    "weight": "1"
}


# Serverless Functions
{{<header_divider>}}

At the heart of Cdev is the Serverless Function. This is the most powerful resource available through the framework because it is where you have to freedom to create what you want. We have made many optimizations to create the best experience for creating and maintaining Serverless Functions.


For a more in depth discussion about the capabilities and limits of Serverless Functions checkout our [architecture documentation](/docs/firstprinciples)



{{<break 2>}}
{{<tool_tip key="info" summary="Info: some header information" >}}
- Check out [this detailed blog post](/docs/firstprinciples) with a practical example.
{{</tool_tip>}}


{{<tool_tip key="tool_tip" summary="Tip: Looking for a quick read through how the core features are used?" >}}
Check out [this detailed blog post](/docs/firstprinciples) with a practical example.
{{</tool_tip>}}


{{<tool_tip key="warning" summary="Warning: Looking for a quick read through how the core features are used?" >}}
Check out [this detailed blog post](/docs/firstprinciples) with a practical example.
{{</tool_tip>}}


{{<tool_tip key="error" summary="Error: Looking for a quick read through how the core features are used?" >}}
Check out [this detailed blog post](/docs/firstprinciples) with a practical example.
{{</tool_tip>}}


{{<tool_tip key="question" summary="Question: Looking for a quick read through how the core features are used?" >}}
Check out [this detailed blog post](/docs/firstprinciples) with a practical example.
{{</tool_tip>}}


### Basic Function
{{<codesnippet `/source_code/function_examples/basic_function.py`>}}

Once your function is deployed, you can execute it with the `cdev run function.execute` command.
```bash
cdev run function.execute <component_name>.hello_function
```

You can then look at the logs from the deployed function
```bash
cdev run function.logs <component_name>.hello_function
```

As you are working on a `Function`, you can use the `--watch` flag to have live updated feed of your logs
```bash
cdev run function.logs <component_name>.hello_function --watch
```
Note that it may take a second for the logs to show up since they are being pulled from the cloud.


{{<break 1>}}
### Responding to Events
One of the most important aspects of Serverless Functions is that they can triggered by different resources. By passing an `Event` construct into the args of your `Function`, your deployed `Function` will be triggered by the event in the Cloud.
{{<codesnippet `/source_code/function_examples/event_function.py`>}}

You can now get the url of the created http api and execute your function by going to the `/hello` route.
```bash
cdev output <component_name>.api.demo.endpoint
```
You can use the command line tool `curl` to test your live url or
```bash
curl <api_endpoint>/hello
```

You can even go to the url in your favorite web browser! 

After visiting the url you can also checkout the logs of your `Function` to see the information that is passed to your `Function` about the `Event` that triggered it. 

```bash
cdev run function.logs <component_name>.hello_function
```

{{<break 2>}}
### Permissions
By default, created `Functions` have no permissions to access other resources, so you have to provide the permissions to your `Function` for it to be able to access other resources. Other resources will have properties that define the set of `Permissions` available to be granted to `Functions`.

{{<codesnippet `/source_code/function_examples/permission_function.py`>}}


### Environment Variables
Although the above `Function` has permission to access the `Bucket`, it does not by default know the name of the `Bucket`. All functions have a set of Environment Variables that can be set. To access these variables within the `Function` use the `os.environ` variable. 

{{<codesnippet `/source_code/function_examples/environment_function.py`>}}


{{<break 2>}}
### Third Party Packages
Third Party Packages are an important part of modern software development. To use a third party package, simple install it with `pip` (we highly recommend using a virtual python environment) and then use the package in a function.

```bash
pip install pandas
```

{{<codesnippet `/source_code/function_examples/dependency_function.py`>}}

It might take a few seconds to upload a copy of the dependency to the cloud when first used, but when using the package in other functions in the same component, it will simply link to the already deployed version.

{{<codesnippet `/source_code/function_examples/dependency_function2.py`>}}


