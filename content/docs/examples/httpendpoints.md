{
    "type": "examples",
    "layout": "type",
    "title": "Integrate HTTP Endpoints",
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
{{<codesnippet `/source_code/http_examples/simple_api_example.py`>}}


### Create routes
{{<codesnippet `/source_code/http_examples/simple_api_example_get.py`>}}


### Integrate GET route with a Serverless function
{{<codesnippet `/source_code/http_examples/simple_api_example_integration.py`>}}

Get the live url for your endpoint:
```
cdev output <component_name>.api.demoApi.endpoint
```

You can test the endpoint with the follow commands from your terminal:
```
curl <your_endpoint>/hello_world
```

{{<break 2>}}
### Integrate POST route with data to a Serverless function
{{<codesnippet `/source_code/http_examples/simple_api_example_post.py`>}}

Get the live url for your endpoint:
```
cdev output <component_name>.api.demoApi.endpoint
```

You can test the endpoint with the follow commands from your terminal:
```
curl -X POST <your_endpoint>/send_data -H 'Content-Type: application/json' -d "{\"login\":\"my_login\"}"
```

Check the logs of your function
```
cdev run function.logs <component_name>.send_data_handler
```
