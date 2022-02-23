{
    "type": "examples",
    "layout": "type",
    "title": "Integrate User Authentication",
    "linktitle": "userauthentication",
    "card_icon": "ti-user",
    "card_body": "Learn how add User Authentication with Auth0",
    "weight": "2"
}


# Add User Authentication to Your Application

User Authentication and Management is one of the most important aspects aspects in application development.

Through the Cdev `Api` resource, we can granular User Authorization to any backend that we create. Cdev `Api` supports
user authentication through JWT Tokens (need more details on the specifics).


We will be using Auth0 as our User Authorization platform and integrating their service into our Api's. AUth0 provides great tutorials and we based this example off their [official documentation](https://auth0.com/blog/securing-aws-http-apis-with-jwt-authorizers/) and a [helpful blog by Sandrino Di Mattia](https://sandrino.dev/blog/aws-api-gateway-jwt-auth0)

{{<break 1>}}
## Create a Basic Api
User the `quick-start` template as a starting place 
```
cdev init user-auth-demo --template quick-start
```
You should have a `src/resources.py` file that looks like 

{{<codesnippet `/source_code/userauth_examples/basic_api.py`>}}

To create the Api and Handler run
```
cdev deploy
```

You will get output that looks like 
```
Base API URL -> https://<your_endpoint>/live
Routes -> FrozenDict({'/hello_world GET': 'muupctg'})
```

You can check that this Api is working correctly by using the Curl command
```
curl https://<your_endpoint>/live/hello_world
```

Or by going to the url `https://<your_endpoint>/live/hello_world` in your browser.

{{<break 1>}}
## Setting up Auth0
You can create a [trail Auth0 account](https://auth0.com/signup) that has a free tier of 7,000 active users and unlimited logins with no required credit card. 


From the Auth0 Dashboard, Create a new Api. Note that you can set the name value to whatever makes sense for your project. The value that you provide for the `identifier` field will need to saved as it will be used as the `audience` property in the next step.
**picture**

If you forget the `identifier` field for your created api in Auth0, you can find it here.
**picture**


We need one more value from Auth0: the `issuer_url` for your Auth0 account.
**picture**


We can now create an `Authorizer` for our Cdev Api. **Note that we add 'https://' and a trailing '/' to the issuer_url and the `name` property on the Cdev Authorizer does not need to match the name of the created Api in Auth0**
{{<codesnippet `/source_code/userauth_examples/default_authorizer.py`>}}

```
cdev deploy
```

By setting the `default_authorizer` property on the Api, all created routes will by default use that Authorizer. Now when we curl the following generated url we will receive a 401 Authentication Error.

```
curl -i https://<your_endpoint>/live/hello_world
```

Now we must have the correct authorization to be able to access this endpoint. Auth0 provides a testing token that can be used to test that the authorization is working correctly.

**pictures**



{{<break 1>}}
## Creating a Frontend
Now that we have the endpoint secured, we are going to create a simple frontend that allows the user to login and then access the restricted endpoint. 

