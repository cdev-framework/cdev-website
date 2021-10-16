{
    "type": "examples",
    "layout": "type",
    "title": "HTTP API endpoints",
    "linktitle": "httpendpoints",
    "card_icon": "ti-bolt",
    "card_body": "Learn how create different API endpoints with API Gateway",
    "weight": "1"
}

# Build an HTTP API Endpoint

HTTP endpoints have become one of the most ubiquitous ways of delivering software to end users. Cdev provides a simple
interface for creating HTTP Apis on the cloud and connecting them to serverless functions. 

{{<break 2>}}
### Create an Api
{{<codesnippet `/source_code/simple_api_example.py`>}}


### Create a GET route
{{<codesnippet `/source_code/simple_api_example_get.py`>}}


### Integrate GET route with serverless function
{{<codesnippet `/source_code/simple_api_example_integration.py`>}}

You can test the endpoint with the follow commands from your terminal:
{{<cli linux="curl https://google.com" windows="wget https://google.com">}}


### Integrate POST route with data to a serverless function
{{<codesnippet `/source_code/simple_api_example_post.py`>}}
{{<cli linux="curl https://google.com -d {data}" windows="wget https://google.com -d {data}">}}
