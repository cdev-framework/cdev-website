{
    "type": "firstprinciples",
    "layout": "type",
    "title": "Serverless Optimizations",
    "linktitle": "optimizations", 
    "card_icon": "ti-light-bulb",
    "card_body": "Learn about Cdev's Serverless optimizations",
    "weight": "3"
}

Although Cdev provides a general purpose cloud deployment framework, we are also focused on improving the `serverless development` experience. Although `Serverless` can refer to a wide range of different services, this section is focused on our optimizations around `Serverless Compute` platforms like Aws Lambda.

{{<break 1>}}
## Serverless Function Parsing
One of the biggest problems when migrating to a `Serverless Compute` platform is having to think about how the change in the underlying platform creates problems like [cold starts](/blogs/coldstarts/). 

Cdev introduces a set of parsing tools that attempt to understand the dependencies of a Serverless function, so that it can deploy only the needed dependencies of the function. To understand Cdev's parsing technology it helps to start with an example and understand all the parts that can add time to Cold Start. In the example, there are three handler functions that each interact with a different external AWS service, but they are part of the same backend and make sense to be kept in the same file. 

{{<break>}}

{{<codesnippet `/source_code/fatlambdaexample.py`>}}

{{<break>}}

When a python module is loaded, all the code in the top level namespace is executed, which means for our function, it executes all three **boto3.client** calls. These extra global statements adds unnecessary time to each function's Cold Start because each function only uses a single external AWS service, but a connection is made to each of the external AWS services. Connections to external systems add extra latency because the initial creation of the connection require rounds trips between the systems before communication can start. 

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
Using the intermediate files as the deployment artifacts also allows for fine grain tracking of changes to each individual function. Without this optomization, updates to a `global statement` would cause an update to all function handlers within the file.

{{<tool_tip key="warning" summary="Limits of Function Parsing">}}
Using the syntax tree to understand a function's dependencies covers a large majority of situations, but it is technically not able to handle all possible situations. To understand how Cdev provides tools to fill these gaps check out the **[API documentation for Lambda function annotations]()**
{{</tool_tip>}}


{{<break 1>}}
## Package Management
**Coming soon April 2022**

{{<break 2>}}
