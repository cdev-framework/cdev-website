{
    "type": "examples",
    "layout": "type",
    "title": "Integrate User Authentication",
    "linktitle": "userauthentication",
    "card_icon": "ti-id-badge",
    "card_body": "Learn how add User Authentication with Auth0",
    "weight": "2"
}


# Add User Authentication to Your Application
{{<header_divider>}}

User Authentication and Management is one of the most important aspects aspects in application development.

With the `Cdev Api` resource, we can add granular [User Authorization](https://auth0.com/intro-to-iam/what-is-authorization/) and [Role-Based Access Control (RBAC)](https://auth0.com/docs/manage-users/access-control/rbac) to any backend. The `Cdev Api` resource supports
user authentication through JWT Tokens (need more details on the specifics).

For these examples, we will be using [Auth0](https://auth0.com/) as our User Authorization platform and integrating their service into our Api's. Auth0 provides great tutorials and we based the following examples off their [official documentation](https://auth0.com/blog/securing-aws-http-apis-with-jwt-authorizers/) and a [helpful blog by Sandrino Di Mattia](https://sandrino.dev/blog/aws-api-gateway-jwt-auth0)

{{<break 1>}}
## Create a Basic Api
User the `quick-start` template as a starting place 
```bash
cdev init user-auth-demo --template user-auth
```
You should have a `src/resources.py` file that looks like 

{{<codesnippet `/source_code/userauth_examples/basic_api.py`>}}

To create the `Api` and `Handler` run
```bash
cdev deploy
```

You will get output that looks like 
```
Base API URL -> https://<your-endpoint>/live
Routes -> FrozenDict({'/demo GET': 'ayhuxeb'})
```

You can check that this `Api` is working correctly by using the Curl command
```bash
curl https://<your_endpoint>/live/demo
```

Or by going to the url `https://<your_endpoint>/live/demo` in your browser.

{{<break 1>}}
## Setting up Auth0
You can create a [trail Auth0 account](https://auth0.com/signup) that has a free tier of 7,000 active users and unlimited logins with no required credit card. 


From the Auth0 Dashboard, Create a new Api on the `Application > Api` page. 


{{<tutorial_image>}}
/images/autho_examples/create_api.png
{{</tutorial_image>}}
{{<break 2>}}

**Note that you can set the `name` to whatever makes sense for your project. The value that you provide for the `identifier` field will need to saved as it will be used as the `audience` property in the next step.**

{{<tutorial_image>}}
/images/autho_examples/api_settings.png
{{</tutorial_image>}}
{{<break 2>}}

We need one more value from Auth0: the `issuer_url` for your Auth0 account. In the `Application` tab, there should be an auto generated application for your api.

{{<tutorial_image>}}
/images/autho_examples/issuer_location.jpg
{{</tutorial_image>}}
{{<break 2>}}

### Creating our Authorizer
We can now create an `Authorizer` for our Cdev Api. 

Update your /src/resources.py file to the follow, replacing the values on lines `13` and `14`. **Note that we add 'https://' and a trailing '/' to the issuer_url.**
{{<codesnippet `/source_code/userauth_examples/default_authorizer.py`>}}

```bash
cdev deploy
```
{{<break 1>}}
### Testing our Authorizer
By setting the `default_authorizer` property on the Api, all created routes will by default use that Authorizer. Now when we curl the following generated url we will receive a 401 Authentication Error.

```bash
curl -i https://<your_endpoint>/live/demo
```

Now we must have the correct authorization to be able to access this endpoint. In the `Test` tab on out `Api` page, Auth0 provides a testing token that can be used to test that the authorization is working correctly.

{{<tutorial_image>}}
/images/autho_examples/api_test_command.jpg
{{</tutorial_image>}}

{{<break 3>}}
## Adding a Frontend to Your Application
We are now going to add a simple HTML page that demonstrates the general concepts of how to create a User Sign up and Sign in flow for your application. 

### Add Static Site Resource
Update lines `7`, `37`, and `41` to add a static front end hosting resource

{{<codesnippet `/source_code/userauth_examples/add_frontend_resource.py`>}}

```bash
cdev deploy
```

**This resource takes a while to create, so we will do some more work on the Auth0 site as it goes.**

{{<break 1>}}
### Create an Application and Database in Auth0
Although we have created and secured our Api, we need to add a few more resources to Auth0 to create the user login and authentication experience. Back in your Auth0 console, navigate to the `authentication > databases` tab. We are going to create a new database that will be used to store the credentials of our development users. 

{{<tutorial_image>}}
/images/autho_examples/create_user_db.png
{{</tutorial_image>}}


{{<tutorial_image>}}
/images/autho_examples/user_db_name.png
{{</tutorial_image>}}

{{<break 1>}}
On the `Applications > Applications` page, we can create a Single Page Application (SPA). 

{{<tutorial_image>}}
/images/autho_examples/create_spa_app.png
{{</tutorial_image>}}
{{<break 1>}}

Once created, navigate to the `connections` tab for your created SPA. There you will be able to enable your user database for this application. 

{{<tutorial_image>}}
/images/autho_examples/enable_dev_user_db.png
{{</tutorial_image>}}
{{<break 2>}}


### Connecting the Frontend to Auth0
We can now return to our Cdev application and hopefully the `static site` resource has finished deploying. Before deploying our code to the `static site` resource, we need to add some information to connect the site to Auth0. We are going to fill out the values in the `src/content/auth_config.json` file. When you open the file, it should look like:
```json
{
  "domain": "",
  "clientId": "",
  "audience": "",
  "api_endpoint": ""
}
```

We can find the `domain` and `clientId` values on Auth0 in our Application's `Settings Tab`. 
{{<tutorial_image>}}
/images/autho_examples/domain_client_location.png
{{</tutorial_image>}}

We can find the `audience` value by going to the `Applications > APIs` page.
{{<tutorial_image>}}
/images/autho_examples/audience_location.png
{{</tutorial_image>}}

The `api_endpoint` can be found by running the following `Cdev Command`
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

Our final step is to register the `url` of our frontend with Auth0. You can get your `url` by running the following command:
```bash
cdev output user_auth.staticsite.demofrontend.site_url
```

In your `Settings` tab on your `Application` page, add your url to the following boxes: `Application Login URI`, `Allowed Callback URLs`, `Allowed Logout URLs`, `Allowed Web Origins`, `Allowed Origins (CORS)`. 
{{<tutorial_image>}}
/images/autho_examples/set_allowed_urls.png
{{</tutorial_image>}}

{{<break 2>}}
### Push The Files to Your Site
Now that we have configured Auth0 with our site, we can push the demo content to your site using the following command.
```bash
cdev run static_site.sync user_auth.demofrontend
```

You can find your url in a web browser.
```bash
cdev output user_auth.staticsite.demofrontend.site_url
```

{{<break 1>}}
### Check Your Site
The provided template site demonstrates the basics of how to login using the [Auth0 Javascript SDK](https://auth0.com/docs/libraries/auth0js) and then use the provided `jwt` to make a call to our Api. When you login the page should look like
{{<tutorial_image>}}
/images/autho_examples/spa_logged_out.png
{{</tutorial_image>}}

Then when you click `login`, you should be redirected to `Auth0 Universal Login Page`
{{<tutorial_image>}}
/images/autho_examples/universal_login.png
{{</tutorial_image>}}

After logging in, you will be redirected and should see a representation the provided `jwt` and user information from Auth0. You can then use the `hit api` button to make a call to your Api. 
{{<tutorial_image>}}
/images/autho_examples/spa_logged_in.png
{{</tutorial_image>}}



{{<break 5>}}