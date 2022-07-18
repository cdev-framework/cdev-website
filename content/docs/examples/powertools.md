{
    "type": "examples",
    "layout": "type",
    "title": "Powertools",
    "linktitle": "powertools",
    "card_icon": "ti-hummer",
    "card_body": "Integrate Aws Lambda Powertools",
    "weight": "4"
}

# AWS Lambda Powertools
[An open source set of utilities](https://awslabs.github.io/aws-lambda-powertools-python/latest/) managed by AWS that provide out of the box functionality for tracing, logging, custom metrics, middleware, etc., for `Serverless Functions`. These tools help teams implement best practices around Serverless development with little overhead. You can install the tools using `pip`.
```bash
pip install aws-lambda-powertools
```
All of the following examples are available in the `power-tools` template project. 
```bash
cdev init demo --template power-tools
```

```bash
cdev deploy
```

{{<tool_tip key="tip" summary="More Information">}}
To learn more about the tool you can read this [blog](https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-lambda-powertools/) from AWS. The [power tools library](https://awslabs.github.io/aws-lambda-powertools-python/latest) contains more constructs than listed here, and we are working hard on making the Cdev framework work with them.
{{</tool_tip>}}


{{<break 1>}}
## Tracing
The tracing library provides a wrapper over `AWS X-Ray` that allows you to quickly get started by using the `@tracer` annotation. To send traces to `AWS X-Ray`, you will need to give your function the correct permissions, which you can grant with the AWS Managed role `AWSXRayDaemonWriteAccess`. 

{{<tool_tip key="tip" summary="Using AWS Managed Roles">}}
You can use any AWS Managed IAM Role by wrapping it in a `PermissionArn` Object.
```python
from cdev.resources.simple.iam import PermissionArn

tracer_permission = PermissionArn("arn:aws:iam::aws:policy/AWSXRayDaemonWriteAccess")
```
{{</tool_tip>}}


{{<codesnippet `/source_code/power_tools_examples/tracer_example.py`>}}

```bash
cdev run function.execute power_tools.tracer_example --event-data "{\"charge_id\":\"123\"}"
```

```bash
cdev run function.logs power_tools.tracer_example
```


{{<break 1>}}
## Logging
The logger libraries provides a standardized interface for logging information. By default, it outputs the logs as structured JSON.
{{<codesnippet `/source_code/power_tools_examples/logging_example.py`>}}

```bash
cdev run function.execute power_tools.logger_example --event-data "{\"charge_id\":\"123\"}"
```

```bash
cdev run function.logs power_tools.logger_example
```


{{<break 1>}}
## Metrics
Create custom metrics are asynchronously captured by AWS Cloudwatch. 

{{<codesnippet `/source_code/power_tools_examples/metrics_example.py`>}}

```bash
cdev run function.execute power_tools.metrics_example
```

```bash
cdev run function.logs power_tools.metrics_example
```

{{<tool_tip key="warning" summary="Using Multiple Libraries">}}
You can mix and match all the available libraries, but when using multiple annotations on the same handler, you should have `metrics.log_metrics` as the top annotation. 
{{</tool_tip>}}


{{<break 1>}}
## Middleware
The Middleware library provides the ability to execute functionality before and after your defined handler. This is a powerful way of encapsulating functionality that is shared across many handlers. For example, it can be used to validate the given data in an external database before triggering the actual functionality. 

{{<codesnippet `/source_code/power_tools_examples/middleware_example.py`>}}

```bash
cdev run function.execute power_tools.middleware_example
```

```bash
cdev run function.logs power_tools.middleware_example
```

{{<break 1>}}
## Data Classes
Although all AWS `Serverless Functions` by default should [conform to the same signature ](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html), it can be helpful to have `typing` information about the event that is triggering the function. This information can help you understand the structure of the data inside the function. The `powertools` library provides a set of classes that wrap the triggering `Event` to provide this additional information. A list of all the available events can be found on the [official documentation pages](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html).

{{<codesnippet `/source_code/power_tools_examples/dataclass_example.py`>}}

```bash
cdev output power_tools.api.demoapi.endpoint
```

```bash
curl <your_url>/helloworld
```

```bash
cdev run function.logs power_tools.dataclass_example
```

{{<tool_tip key="error" summary="Data Classes Limitations">}}
The implementation of `Data Classes` do not provide any guarantees of data validation. If an event does not conform to the expected form of a certain `Data Class`, it will not throw an error until a non-existent property is accessed. For example, triggering the above function directly will lead to an error.

```bash
cdev run function.execute power_tools.dataclass_example
```
For strong data validation, considering using the [Parser library](https://awslabs.github.io/aws-lambda-powertools-python/latest/utilities/parser/) in `powertools`.

{{</tool_tip>}}


{{<break 2>}}
