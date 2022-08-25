{
    "type": "examples",
    "layout": "type",
    "title": "Integrate User Authentication",
    "linktitle": "userauthentication",
    "card_icon": "ti-id-badge",
    "card_body": "Learn how to add User Authentication with Auth0",
    "weight": "2"
}


# Add User Authentication to Your Application
{{<header_divider>}}

User Authentication and Management is one of the most important aspects in application development.

With the `Cdev API` resource, we can add granular [User Authorization](https://auth0.com/intro-to-iam/what-is-authorization/) and [Role-Based Access Control (RBAC)](https://auth0.com/docs/manage-users/access-control/rbac) to any backend. The `Cdev API` resource supports
user authentication through [JSON Web Tokens(JWT)](https://jwt.io/introduction).

{{<tool_tip key="info" summary="JWT Authentication">}}
You can learn more about JWT authentication [here](https://auth0.com/docs/secure/tokens/json-web-tokens).
{{</tool_tip>}}

For these examples, we will be using [Auth0](https://auth0.com/) as our User Authorization platform and integrating their service into our API's. Auth0 provides great tutorials and we based the following examples off their [official documentation](https://auth0.com/blog/securing-aws-http-apis-with-jwt-authorizers/) and a [helpful blog by Sandrino Di Mattia](https://sandrino.dev/blog/aws-api-gateway-jwt-auth0).

{{<break 1>}}

## Set Up
We will be starting this tutorial from the `user-auth` template. 

```bash 
cdev init user-auth-demo --template user-auth
```

{{<break 1>}}
## Create a Basic API

You should have a `src/resources.py` file that looks like:

{{<codesnippet `/source_code/userauth_examples/basic_api.py`>}}

To create the `API` and `Serverless Function` run
```bash
cdev deploy
```

{{<tool_tip key="output" summary="Deploy Output">}}
This step should output the live url of your webhook and look like
```
Base API URL -> https://<your-endpoint>/live
Routes -> FrozenDict({'/demo GET': 'ayhuxeb'})
```
{{</tool_tip>}}


You can check that this `API` is working correctly by using the `Curl` command
```bash
curl https://<your_endpoint>/live/demo
```

Or, by going to the url `https://<your_endpoint>/live/demo` in your browser.

{{<break 1>}}
## Setting up Auth0
[Auth0](https://auth0.com/docs/get-started/auth0-overview) is a cloud-based identity management service that uses `APIs` and data syncing to provide authentication and authorization services for applications. 
You can create a [trial Auth0 account](https://auth0.com/signup) that has a free tier of 7,000 active users and unlimited logins with no required credit card. 


From the Auth0 Dashboard, Create a new API on the `Application > API` page. 


{{<tutorial_image>}}
/images/autho_examples/create_api.png
{{</tutorial_image>}}
{{<break 2>}}

{{<tool_tip key="info" summary="Setting the values">}}
Note that you can set the `name` to whatever makes sense for your project. The value that you provide for the `identifier` field will need to be saved as it will be used as the `audience` property in the next step.
{{</tool_tip>}}

{{<break 1>}}
{{<tutorial_image>}}
/images/autho_examples/api_settings.png
{{</tutorial_image>}}
{{<break 2>}}

We need one more value from Auth0: **the `issuer_url` for your Auth0 account**. 

In the `Application` tab, there should be an auto generated `Application` for your API. When you open the auto generate app, you will see the `Domain` for your account. This `Domain` value will be the `issuer_url`.

{{<tutorial_image>}}
/images/autho_examples/issuer_location.jpg
{{</tutorial_image>}}
{{<break 2>}}

### Creating our Authorizer
We can now create an `Authorizer` for our Cdev API. The `Authorizer` provides the information needed to configure a JWT authorizer that adds access control to your API endpoint.

Update your `/src/resources.py` file to the follow, replacing the values on lines `13` and `14`. 

{{<tool_tip key="info" summary="Setting the issuer_url">}}
Note that you need to add 'https://' and a trailing '/' to the `issuer_url`.
{{</tool_tip>}}

{{<codesnippet `/source_code/userauth_examples/default_authorizer.py`>}}

Deploy the changes to the `src/resources.py` file.
```bash
cdev deploy
```
{{<break 1>}}
### Testing our Authorizer
By setting the `default_authorizer` property on the `API`, all created routes will by default use that `Authorizer`. Now, when we `curl` the following generated url, we will receive a `401 Authentication Error`.

```bash
curl -i https://<your_endpoint>/live/demo
```

Now, we must have the correct authorization to be able to access this endpoint. In the `Test` tab on the `API` page, `Auth0` provides a testing token that can be used to test that the authorization is working correctly.
{{<tool_tip key="info" summary="Test Your Authenticated API">}}
You can use your preferred `API Development and Testing Tool` to test your `API` or, download and use one of the following:

**[Insomnia](https://insomnia.rest/)**
{{<break 1>}}
**[Postman](https://www.postman.com/)**
{{<break 1>}}
**[Swagger](https://swagger.io/)**

You can find more information about `API Development and Testing Tools`, in a **[collection of resources for building and maintaining RESTful APIs](https://github.com/yosriady/api-development-tools)** maintained by [Yos Raidy](https://github.com/yosriady).
{{</tool_tip>}}

{{<tutorial_image>}}
/images/autho_examples/api_test_command.jpg
{{</tutorial_image>}}

{{<break 3>}}
## Adding a Frontend to Your Application
We are now going to add a simple HTML page that demonstrates the general concepts of how to create a User Sign-up and Sign-in flow for your application. 

### Add Static Site Resource
Update lines `7`, `37`, and `41` to add a `Static Site` resource to our demo frontend content.

{{<codesnippet `/source_code/userauth_examples/add_frontend_resource.py`>}}

```bash
cdev deploy
```
{{<tool_tip key="warning" summary="Resource Creation Time">}}
To create a frontend that works with Auth0, our website must be secured with `HTTPS`. Therefore, the `Static Site` resources creates your frontend on `AWS Cloudfront`, which is a globally distributed `Content Delivery Network (CDN)`. Using `AWS Cloudfront` provides many benefits, but it also means that it takes a few minutes to initially create the resource. Once created, **updates to the website are instant.** As the resource deploys, you can continue with creating the next section on `Auth0` or grab a cup of coffee. 
{{</tool_tip>}}

{{<break 1>}}
### Create an Application and Database in Auth0
Although we have created and secured our `API`, we need to add a few more resources to `Auth0` to create a user login and authentication work flow.

In the `Auth0` console, navigate to the `authentication > databases` tab. Create a new database that will be used to store the credentials of our development users. 

{{<tutorial_image>}}
/images/autho_examples/create_user_db.png
{{</tutorial_image>}}
{{<break 1>}}

Set the database name to dev-users or any name you prefer.
{{<tutorial_image>}}
/images/autho_examples/user_db_name.png
{{</tutorial_image>}}

{{<break 1>}}
On the `Applications > Applications` page, create a Single Page Application (SPA). 

{{<tutorial_image>}}
/images/autho_examples/create_spa_app.png
{{</tutorial_image>}}
{{<break 1>}}

Once created, navigate to the `connections` tab for your created SPA, and enable the created database for this application. 

{{<tutorial_image>}}
/images/autho_examples/enable_dev_user_db.png
{{</tutorial_image>}}
{{<break 2>}}


### Connecting the Frontend to Auth0
Before deploying our code to the `Static Site` resource, we need to add some information to connect the site to `Auth0`. We need to fill out the values in the `src/content/auth_config.json` file. When you open the file, it should look like:
```json
{
  "domain": "",
  "clientId": "",
  "audience": "",
  "api_endpoint": ""
}
```

We can find the `domain` and `clientId` values on `Auth0` in our Application's `Settings Tab`. 
{{<tutorial_image>}}
/images/autho_examples/domain_client_location.png
{{</tutorial_image>}}

We can find the `audience` value by going to the `Applications > APIs` page.
{{<tutorial_image>}}
/images/autho_examples/audience_location.png
{{</tutorial_image>}}

The `api_endpoint` can be found by running the following `Cdev Command`:
```bash
cdev output user_auth.api.demoapi.endpoint
```

Your final `src/content/auth_config.json` file should be filled out and look similar to:
```json
{
  "domain": "dev-f4xoprya.us.auth0.com",
  "clientId": "YAzlTckppL3gurUOkA53Ay06YvTQY6QW",
  "audience": "urn:tutorial",
  "api_endpoint": "https://5rqurtix69.execute-api.us-east-1.amazonaws.com/live"
}
```

Our final step is to register the `url` of our frontend with `Auth0`. You can get your `url` by running the following command:
```bash
cdev output user_auth.staticsite.demofrontend.site_url
```

In your `Settings` tab on your `Application` page, add your `url` to the following boxes: `Application Login URI`, `Allowed Callback URLs`, `Allowed Logout URLs`, `Allowed Web Origins`, and `Allowed Origins (CORS)`. 
{{<tutorial_image>}}
/images/autho_examples/set_allowed_urls.png
{{</tutorial_image>}}

{{<break 2>}}
### Push The Files to Your Site
Now that we have configured `Auth0`, we can push the demo content to the `Static Site` using the following command:
```bash
cdev run static_site.sync user_auth.demofrontend
```

You can get the `url` of your `Static Site` using the following command.
```bash
cdev output user_auth.staticsite.demofrontend.site_url
```

Now you can visit your site in your web browser!

{{<break 1>}}
### Check Your Site
The provided template site demonstrates the basics of how to login using the [Auth0 Javascript SDK](https://auth0.com/docs/libraries/auth0js) and then use the provided `JWT` to make a call to our `API`. When you login, the page should look like:
{{<tutorial_image>}}
/images/autho_examples/spa_logged_out.png
{{</tutorial_image>}}

When you click `login`, you should be redirected to the `Auth0 Universal Login Page`.
{{<tutorial_image>}}
/images/autho_examples/universal_login.png
{{</tutorial_image>}}

After logging in, you will be redirected and should see the provided `JWT` and user information from `Auth0`. You can then use the `Hit Api` button to make a call to your `API`. 
{{<tutorial_image>}}
/images/autho_examples/spa_logged_in.png
{{</tutorial_image>}}



{{<break 5>}}
