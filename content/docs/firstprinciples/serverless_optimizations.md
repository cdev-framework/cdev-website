{
    "type": "firstprinciples",
    "layout": "type",
    "title": "Serverless Function Optimizations",
    "linktitle": "optimizations", 
    "card_icon": "ti-light-bulb",
    "card_body": "Learn about Cdev's Serverless optimizations",
    "weight": "2"
}

Cdev provides optimizations that are designed to make creating and managing Serverless Functions a seamless experience. 


{{<break 1>}}
## Serverless Function Parsing
One of the biggest problems when migrating to a `Serverless Compute` platform is having to think about how the change in the underlying platform creates problems like [cold starts](https://mikhail.io/serverless/coldstarts/define/). 

Cdev introduces a set of parsing tools that attempt to understand the dependencies of a Serverless function, so that it can deploy only the needed dependencies of the function. To understand Cdev's parsing technology, it helps to start with an example and understand all the parts that can add time to a Cold Start. In the example, there are three handler functions that each interact with a different external AWS service, but they are part of the same backend and make sense to be kept in the same file. 

{{<break>}}

{{<codesnippet `/source_code/fatlambdaexample.py`>}}

{{<break>}}

When a python module is loaded, all the code in the top level namespace is executed, which means for our function, it executes all three **boto3.client** calls. These extra global statements adds unnecessary time to each function's Cold Start because each function only uses a single external AWS service, but a connection is made to each of the external AWS services. Connections to these external systems add extra latency because the initial creation of the connection require round trips between the systems before communication can start. 

{{<break>}}

By analyzing the syntax tree representation of the code, Cdev is able to understand what parts of the global namespace are needed for each individual function. With this understanding, we can parse each individual handler function along with the needed global statements into a separate file. These newly created files can be used as the deployment final artifact. 

For the above example, the final deployment artifacts using Cdev would be: 

**myhandler1.py** 
{{<codesnippet `/source_code/fatlambdaexample_parsed1.py`>}}

**myhandler2.py**
{{<codesnippet `/source_code/fatlambdaexample_parsed2.py`>}}

**myhandler3.py**
{{<codesnippet `/source_code/fatlambdaexample_parsed3.py`>}}


{{<break>}}
Using the intermediate files as the deployment artifacts also allows for fine grain tracking of changes to each individual function. Without this optimization, updates to a `global statement` would cause an update to all function handlers within the file.


{{<break>}}

Another benefit of this function parsing is that it removes code that contains `cdev` resource definitions from the final deployed artifact. For example in the follow code from the `quick-start` template, the definition of the `API` is removed from the final deployment artifact.

{{<tool_tip key="warning" summary="Referencing Resources in Functions">}}
Cdev resources should not directly be used in `Serverless Function`. Resources are designed to interact with the `Cdev` framework during the building of a project, but they are designed to be called at runtime. Information about resources should be passed to [functions via environment variables](http://localhost:1313/docs/resources/functions/#environment-variables).
{{</tool_tip>}}

{{<codesnippet `/source_code/quickstart.py`>}}




{{<tool_tip key="warning" summary="Limits of Function Parsing">}}
Using the syntax tree to understand a function's dependencies covers a large majority of situations, but it is technically not able to handle all possible situations. If you have a situation where the syntax tree does not accurately encode a function's dependencies, reach out to daniel@cdevframework.com for a solution. 
{{</tool_tip>}}

{{<break>}}

## Dependency Management

{{<break>}}
### Third Party Packages
One of the biggest challenges of Serverless Development is managing the bundling of third-party packages with your project. Cdev automatically detects and deploys third party packages used by functions.

Due to limitations of the underlying platforms around total package size and to reduce cold starts, it is important that a function only contains the dependencies that are used. Using the parsed functions artifacts, Cdev is able to analyze and compute the dependencies of each individual function and link only the needed dependencies. 

{{<tool_tip key="warning" summary="Platform Limitations">}}
Some Python packages contain platform specific (x86, arm, etc) parts that can differ between your development environment and the Aws Lambda runtime environment. Currently, Cdev chooses the deployment environment of a function based on the development machine being used, but there can be packages that do not work due to platform differences.
{{</tool_tip>}}

{{<break>}}
### Relative Dependencies
Projects often encapsulate and share functionality throughout a project as relative dependencies. Cdev automatically analyzes the relative imports used by a function and packages the needed relative dependencies with the deployment artifact. 

{{<tool_tip key="warning" summary="Limitations">}}
Local dependencies should be reference using the dot notion and be contained within the `src` directory. Cdev only supports referencing dependencies that are either installed via a package manager or referenced as relative dependencies using the dot notation. 
{{</tool_tip>}}


{{<break 2>}}
