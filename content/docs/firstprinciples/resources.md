{
    "type": "firstprinciples",
    "layout": "type",
    "title": "Cloud Resource Management",
    "linktitle": "resources", 
    "card_icon": "ti-home",
    "card_body": "Learn how Cdev deploys resources",
    "weight": "1"
}

Although Cdev is currently focused on Serverless development, it is built on a general purpose `cloud` infrastructure framework called `Cdev Core`.

{{<tool_tip key="tip" summary="What is the Cloud?">}}
Within Cdev, a `cloud` is defined as a system that provides on demand computing resources and services via computer to computer communication. 
{{</tool_tip>}}


{{<break 1>}}
## Resources
Within the Cdev framework, a `resource` is a logical representation of a defined computing resource or service provided by a `Cloud`. Although this is an abstract definition, it encapsulates the flexibility of the `resource` model. 

An important aspect to note is that the resource is only a **logical representation** of an actual `Cloud` service. This means that the properties of the resource do not need to map one to one to the actual properties in the `Cloud`. This allows a `resource` to be shaped to meet the needs of different projects. Although the properties of a `resource` can be defined arbitrarily, the definitions must have a logically relationship to the final deployed `cloud` services. 

{{<tool_tip key="info" summary="Default Resources">}}
You can see that the default resources provided with Cdev do not map one to one to the resources they deploy in Aws. For example, the `simple::bucket` resource does not provide all the properties that are available to an `Aws S3 bucket`. 

This definition also allows for higher abstracted resources like the Cdev `Serverless Function` that require tying together multiple services in the `Cloud`.
{{</tool_tip>}}

{{<break 1>}}
A resource must have three values: `name`, `resource_id`, and `hash`. 


### Resource Id
The `resource_id (ruuid)` is used to categorize resource that are of the same type (`cdev::simple::bucket`, etc). The structure of the `ruuid` is `<organization>::<package>::<resource>`. The `organization` is the highest level information about who created and maintains that resource. The `package` allows the `organization` to group and categorize different resources together. The `resource` is a logically appropriate name for the resource. 


### Name
When creating a `resource` it must be given a `name` that will be used to reference the resource throughout the framework.


### Hash
A `resource` can have any number of properties that define how the `resource` should be deployed. The `hash` is the identification of a specific configuration of the properties of a resource. If you change one of the properties of the resource, it should result in a change in the `hash`. This means that the `hash` can be used to track the desired state of the `resource`.

{{<tool_tip key="error" summary="Name as Property">}}
The `name` of a resource should never affect the `hash` of the resource. This differentiation between the `name` and properties is a core principle of how `Cdev Core` tracks changes in resources. 
{{</tool_tip>}}



{{<break 2>}}
## Components
A `component` is a collection of `resources` that share a namespace. The `component` provides a limit on the naming conventions for a set of resources. Within a component, a `resource` must be uniquely identified by both the pairs: <`ruuid`,`name`> and <`ruuid`, `hash`>. The following demonstrates different scenarios with components:
```
Bad (conflicting names in same component)
- Component A 
    - cdev::simple::function demo (hash -> 1)
    - cdev::simple::function demo (hash -> 2)
```
```
Good (conflicting names in different components)
- Component A 
    - cdev::simple::function demo (hash -> 1)
- Component B
    - cdev::simple::function demo (hash -> 2)
```
```
Bad (conflicting hash in same component)
- Component A 
    - cdev::simple::function demo1 (hash -> 1)
    - cdev::simple::function demo2 (hash -> 1)
```
```
Good (conflicting hash in different components)
- Component A 
    - cdev::simple::function demo1 (hash -> 1)
- Component B
    - cdev::simple::function demo2 (hash -> 1)
```

{{<tool_tip key="tip" summary="Nonce Property">}}
Since a resource must not have a conflicting `hash` within the same component, most resources will provide a `nonce` property. This property is used to differentiate resources with the same `hash` as different resources. For example:

```python
bucket1 = Bucket("b1")
bucket2 = Bucket("b2", nonce='1')
```
{{</tool_tip>}}

On top of providing defined namespaces for resources, `components` also define the bounds by which resources can provide output information to each other. When a `resource` is deployed onto the `cloud`, the `cloud` provides back information about what was created. This information can then be passed to other `resources`. For example, a `database name` can be passed to a `serverless function` to define what `database` the `serverless function` should connect to.

`Resources` defined within the same component are able to freely pass their outputs between themselves, but `resources` in different components can **not** share output. To share information between `components`, you can create a `reference` to a `resource` or store the needed data in an outside system. 

{{<tool_tip key="warning" summary="References are in early Beta">}}
Currently, the implementations of these systems do not provide all the features that the architecture is designed to enable. One of the core reasons for the `component` system is to integrate with an IAM layer that determines who can create resources/references and manage components. With a full IAM layer, this architecture will allow teams to explicitly define the ownership and management of different resources. Since these features are not fully integrated, it is best practice to use a single component to define your resources. 
{{</tool_tip>}}


`Components` are designed to be a flexible namespace to adapt to the needs of different projects. There are not many hard rules about how and when resources should be separated into different `components` because they are designed to allow each individual team to decided how to best use them. 

{{<break 2>}}
## The Resource Graph
The connections between the set of all `resources` create a `resource graph`. This data structure is created by understanding how resources share the output generated by the `cloud`. The deployment of resources into the cloud is driven by the workflow of generating a `resource graph` and comparing it to the previously deployed `resource graph`. 

{{<tool_tip key="tip" summary="Cdev Deploy Command">}}
The `cdev deploy` command is responsible for executing this workflow. It generates a new `resource graph` based on the current state of your project then generates the differences from the previously deployed graph. Once you have approved the changes, it deploys them into the `cloud`.
{{</tool_tip>}}


{{<break 2>}}
## Mappers
Updates to `resources` in the `resource graph` can be expressed as three types of actions: `create`, `update`, and `delete`. These three actions must be mapped to changes in the `cloud` to reflect the desired change to the `resource`. Cdev provides a defined layer of abstraction between the actions on the `resource graph` and updating of the `cloud` via the `Mapper` Api. 

A `Mapper` is a class that is designated to handle updating the `cloud` to reflect a desired change for a `resource`. `Mappers` are registered with the framework to handle deploying all resources from an `organization`, and for returning information about the deployed services on the `cloud`.


{{<break 2>}}
## The Backend 
As a project is developed, the current state of the `resource graph` must stored so that it can be referenced in the future to understand updates. Along with the `resource graph` the `backend` also stores all the output information generated by the `cloud`. Within the entire Cdev framework, the `backend` should be the only place that information should be persisted. You can learn more about the backend by visiting its [api definition](/docs/api/core/constructs/backend.html). 






{{<break 2>}}
