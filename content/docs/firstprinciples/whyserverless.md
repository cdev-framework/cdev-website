{
    "type": "firstprinciples",
    "layout": "type",
    "title": "Why use Serverless?",
    "linktitle": "whyserverless", 
    "card_icon": "ti-thought",
    "card_body": "Learn the benefits and drawbacks of serverless compute platforms",
    "weight": "1"
}

# What is Serverless?

{{<blockqoute>}}
“But there are still servers involved!” - Some person every time there is a discussion about serverless
{{</blockqoute>}}

Overtime the meaning of Serverless has become muddied. Some would say that it has always been muddy because there are in fact servers still involved with any kind of serverless offering, and it is just about who manages the servers. Typically Serverless refers to services that offer abstracted versions of applications such that developers do not need to worry about creating, managing, or scaling the underlying infrastructure that the application runs on. These applications can range from databases, object/file storage, compute, and as time passes, almost any tool developers use.

Although there are cool serverless services in almost any developer tool vertical, Cdev's main focus is on improving the developer experience for serverless compute platforms like AWS Lambda, Azure Functions, GCP Functions, etc. We believe that serverless compute platforms have the potential to expand the range of viable software projects and pool of people that can develop these projects. To understand how Cdev improves the developer experience, it is important to understand the technology that came before Serverless compute platforms. 

### Before The Cloud 
In the historic days, if you wanted to start a new company on the internet you would need to acquire the physical servers that you application was going to run on. This was a process that required a lot of upfront cost both in time and money. If your application was successful, it would eventually reach a point that no single machine could handle all traffic on its own, so the only way to handle all the traffic is to use multiple computers.

Horizontal scaling is when a copy of an application is run on multiple different computers, and another computer runs a load balancing program to split the traffic to the different application computers. As traffic increases, more servers can be added to handle the traffic, and inversely if traffic decreases, unneeded servers can be removed. 

![load balancer image](/diagrams/load_balancer.svg)

### The Cloud
When AWS released EC2 in 20XX, they changed the calculous around horizontal scaling. Instead of a company needing to forecast their traffic far enough ahead that they have time to order and rack new servers, a company could now spin up new servers with the click of a button. 

### The Serverless Value Proposition

In 2015, AWS announced **[Lambda](https://www.youtube.com/watch?v=9eHoyUVo-yg&ab_channel=AmazonWebServices)**: the first serverless compute platform. This was the logical conclusion of the arc of horizontal scaling. This platform would provide the finest granularity for horizontal scaling by working at the level of individual functions. This new paradigm was supposed to completely abstract all aspects of horizontal scaling allowing developers to get all the benefits while focusing on their own projects. Also by abstracting these details, serverless compute platforms are supposed to by an easier on ramp for new developers to deploy their projects because they need not understand networking and server but instead need only know how to write a function. 

With this value proposition, it seemed the serverless compute platforms would lead to another dramatic shift in delivering software solutions, but the adoption of the technology has not gone as expected. 

### Why Create Cdev?

Switching the unit of horizontal scaling from a bundled application to individual functions is a change that creates friction with traditional developer tools and frameworks. These frictions grow as a project scales and have slowed the rate of adoption because the current methods for combating them add manual work to the developer experience. Although any new technology will have growing pains, it has been particularly difficult for serverless development to break free because the opportunity cost of using the traditional cloud deployment model is so strong. With the initial cloud offering the opportunity cost was lower because the only other way to run these applications were on premise, but serverless compute platforms must compete against the cloud providers other offerings that are have more stable tooling. 


At Cdev, we believe that new tools and frameworks must be created to unlock the full value proposition of serverless compute platforms. The tools must solve the problems of serverless development while not creating more manual work than the tools from traditional development backgrounds. 