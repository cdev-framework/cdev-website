{
    "type": "blogs",
    "layout": "type",
    "title": "Cold Starts",
    "linktitle": "coldstarts",
    "card_icon": "ti-zip",
    "card_body": "Learn how Cdev packages functions to reduce cold starts",
    "weight": "2",
    "Image":"/images/blog_thumbnails/pexels-pixabay-434259.jpg",
    "date": "2022-05-01T16:19:26+06:00",
    "Author": "Daniel Sanchez",
    "AuthorImage":"/images/headshots/daniel_headshot.jpg"
}


{{<blockquote>}}
"A computer seems infinitely fast, until it doesn't!"
{{</blockquote>}}

{{<break>}}


Perhaps the most infamous problem in the serverless compute space is: **The Cold Start**. It is a problem that arises from any horizontal scaling platform, but did not become a problem for developers until the Serverless compute paradigm. Although unavoidable, it is possible to lower Cold Starts to an acceptable level on Serverless compute platforms. 

Cdev has created new parsing technology that is aimed at helping developers manage their Cold Starts while maintaining a familiar development experience. 

{{<break>}}

### Horizontal Scaling
For a lot of people the limits of computers are most noticed when a server hosting an application is overloaded from an increase in traffic that causes the site to crash. As a site grows in popularity, it eventually reaches a point that no single computer is fast enough to handle all the traffic, so the only way to handle all the traffic is to use multiple computers.

Horizontal scaling is when a copy of an application is run on multiple different computers, and another computer runs a load balancing program to split the traffic to the different application computers. As traffic increases, more servers can be added to handle the traffic, and inversely if traffic decreases, unneeded servers can be removed. 


{{<blog_image  img="/diagrams/load_balancer.svg" alt="load balancer image">}}

Before the public cloud providers, developers had to buy and rack these servers themselves, which meant they had to attempt to forecast their future traffic. One of the early big impacts the public cloud providers was offering programmatic autoscaling, so that instead of having to physically rack a new server, developers only needed to click a few buttons on a website. Then cloud providers went a step further and created products that could monitor your application and add new instances based on customized triggers on different metrics such as cpu utilization, memory usage, network bandwidth or a range of other metrics so that scaling happened automatically. 

{{<break>}}

### So what is a Cold Start?
Another time that people most likely notice the speed limitations of computers is when turning one on. We must sit waiting for the computer to power on and return to a usable state. Servers have a similar phenomenon where they must run initialization steps before they are ready to handle traffic. Some of this initialization is from the underlying system and some is code written by the developer. 

**A Cold Start is the time that is takes for an autoscaled computing unit to be initialized and reach the state that it can begin handling requests.** 

For traditional applications, the Cold Start when adding another version of the application was in the range of powering on a computer (> 1 min) as the Cloud Provider was most likely providing a new Virtual Machine for that unit. This meant that the autoscaling trigger had to be set at a point that it was unlikely that the current machines would be overwhelmed before the new machine had finished the Cold Start. As long as the increase in traffic was not too rapid, the end users would not notice the cold start as the already provisioned machines would handle the requests. 

{{<break>}}


### Why is this a problem for Serverless compute?

As mentioned in our **[Why Serverless](/docs/firstprinciples/whyserverless)** post, serverless compute platforms changed the unit of deployment for software projects from applications to single functions in an attempt to have finer grained horizontal scaling abilities. These platforms are set up so that when a request comes in and no available function is available, a new function is provisioned to handle the request, but now that request must wait for the function's Cold Start to finish before being handled. These platforms have exposed a previously hidden latency to end users. Developers want their applications to feel fast and not have unneeded latency, and since Cold Starts are partially dependent on the developers own initialization code, developers must now optimize their code to reduce Cold Starts.

{{<break>}}

### What are the current ways to mitigate Cold Starts? 

The current state of mitigating Cold Starts is best understood by looking at the three types of serverless functions people are creating described in ***[this post by Matt Coulter](https://dev.to/cdkpatterns/learn-the-3-aws-lambda-states-today-the-single-purpose-function-the-fat-lambda-and-the-lambda-lith-361j)*** . 

Reading this article, I could not help but feel like Goldilocks trying to find the right bed to sleep in: 
- The single purpose function requiring to much of a change in how I think about software development. Being a mere mortal who is not a ninja at navigating my IDE, having to constantly switch and create different files causes friction that interrupts the flow state of coding. 
- The lambda-lith seemed to not take enough advantage of these new platforms, and the Cold Starts are killer. 
- The Fat lambda seemed the most reasonable compromise, but if not constantly monitored it could spiral to having killer Cold Starts too. 

Can we have the benefits of serverless compute platforms while not having to constantly worry about Cold Starts?

{{<break>}}

