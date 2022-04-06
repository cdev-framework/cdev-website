{
    "type": "examples",
    "layout": "type",
    "title": "Integrate HTTP Endpoints",
    "linktitle": "httpendpoints",
    "card_icon": "ti-bolt",
    "card_body": "Learn to create API endpoints with API Gateway",
    "weight": "1"
}

# Build an HTTP API Endpoint
{{<header_divider>}}

HTTP endpoints have become one of the most ubiquitous ways of delivering software to end users. Cdev provides a simple interface for creating HTTP Apis and connecting them to `Serverless Functions`. 

{{<break 1>}}
## Create an Api
{{<codesnippet `/source_code/http_examples/simple_api_example.py`>}}


{{<break 1>}}
## Create routes
{{<codesnippet `/source_code/http_examples/simple_api_example_get.py`>}}


{{<break 1>}}
## Integrate GET route with a Serverless function
{{<codesnippet `/source_code/http_examples/simple_api_example_integration.py`>}}

Get the live url for your endpoint:
```bash
cdev output <component_name>.api.demoApi.endpoint
```

You can test the endpoint with the follow commands from your terminal:
```bash
curl <your_endpoint>/hello_world
```

{{<break 1>}}
## Integrate POST route with data to a Serverless function
{{<codesnippet `/source_code/http_examples/simple_api_example_post.py`>}}

Get the live url for your endpoint:
```bash
cdev output <component_name>.api.demoApi.endpoint
```

You can test the endpoint with the follow commands from your terminal:
```bash
curl -X POST <your_endpoint>/send_data -H 'Content-Type: application/json' -d "{\"login\":\"my_login\"}"
```

Check the logs of your function
```bash
cdev run function.logs <component_name>.send_data_handler
```


{{<break 1>}}

## Return Values from Function
[From the Aws Documentation](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html#http-api-develop-integrations-lambda.response), API Gateway makes the following assumptions if your Lambda function returns valid JSON and doesn't return a statusCode:

- isBase64Encoded is `false`.
- statusCode is `200`.
- content-type is `application/json`. 
- body is the `function's response`.

**Examples:**

Function Response
```python 
return "Hello from Lambda!"
```

Api Gateway Response
```json
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "body": "Hello from Lambda!",
  "headers": {
    "content-type": "application/json"
  }
}
```

{{<break 1>}}

Function Response
```python
return { "message": "Hello from Lambda!" }
```

Api Gateway Response
```json
{
  "isBase64Encoded": false,
  "statusCode": 200,
  "body": "{ \"message\": \"Hello from Lambda!\" }",
  "headers": {
    "content-type": "application/json"
  }
}
```
{{<break 1>}}
If you want to customize your return value completely, it should have the form:
```python
return {
    "cookies" : ["cookie1", "cookie2"],
    "isBase64Encoded": True|False,
    "statusCode": httpStatusCode,
    "headers": { "headername": "headervalue", ... },
    "body": "Hello from Lambda!"
}
```

{{<tool_tip key="tip" summary="Return Custom JSON">}}
If you are going to return a custom value and want the body to be a json value, the value must be a json encoded string. You can use the std lib `json.dumps` method to generate the properly encoded string.

```python
return {
    "cookies" : ["cookie1", "cookie2"],
    "isBase64Encoded": True|False,
    "statusCode": httpStatusCode,
    "headers": { "headername": "headervalue", ... },
    "body": json.dumps({
        "message" :"Hello from Lambda!"
    })
}
```


{{</tool_tip>}}