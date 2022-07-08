{
    "type": "tutorial",
    "layout": "type",
    "title": "Fullstack Application",
    "linktitle": "fullstack", 
    "card_icon": "ti-layout",
    "card_body": "Learn how to create and maintain a fullstack web application",
    "weight": "1"
}


**Coming Soon (August 2022)**

Create a site to create and keep diary entries to learn how Cdev can be used to create and manage full stack web applications.


In this tutorial, we will be going through the entire process of creating a full stack application with Cdev. We will be focusing on demonstrating how Cdev can integrate with standard Python tools and other development workflows. We will explain all the components and steps of this tutorial in depth, but it does help to have some familiarity with some of the technologies and concepts around full stack development.

- How the web works
- Basics of Frontend Development (HTML, CSS, and JS)
- Basics of React
- Basics of Backend Development (requests, etc)
- Relational DB technologies (Sql)
- Monitoring Applications

{{<break 1>}}

### Technologies
- Backend
    - Serverless Functions
- Database 
    - Postgres
    - Sql Alchemy 
    - Alembic
- Frontend
    - React
    - Bootstrap

{{<break 1>}}

## Create Cdev Project
We will be starting this tutorial from the standard `quick-start` template.

```bash
cdev init diary-project --template quick-start
```

Now we can deploy our project to get a live REST Api

```bash
cdev deploy
```
This step should output the live url of your webhook and look like
```
Base API URL -> <your-endpoint>
```

{{<break>}}

## Create Database Connection
For this project we will be utilizing a relational database and the SqlAlchemy ORM.  An in-depth example of how to set up SqlAlchemy ORM can be found in the examples section of our website as a part of the [Integrate RelationalDBs](https://cdevframework.io/docs/examples/relationaldb/#sqlalchemy-orm) chapter. 

Update your `src/hello_world/resources.py` file to: 
{{<codesnippet `/source_code/diary_tutorial/step1_resource.py`>}}

Now we can deploy our new resources.
```bash
cdev deploy
```

{{<break 1>}}
**Next, we are going to create our database models.** Install `sqlalchemy_aurora_data_api`.
{{<tool_tip key="tip" summary="Database models">}}
`Database models` determine the logical structure of your database.  They determine how data can be stored, organized, and manipulated.
{{</tool_tip>}}
```bash
pip install sqlalchemy_aurora_data_api
```
Then, create a `src/hello_world/models.py` file and add the following code:

{{<codesnippet `/source_code/diary_tutorial/models.py`>}}

Now we are going to install and configure `alembic`.  Alembic is a database migration tool for usage with SQLAlchemy for Python.

```bash
pip install alembic
```
{{<tool_tip key="tip" summary="Alembic Library">}}
`Alembic` is one of the best in class tools for working with SqlAlchemy. You can learn more about the tool from [their official documentation](https://alembic.sqlalchemy.org/en/latest/).
{{</tool_tip>}}

Initialize the needed files for `alembic` using the following command. We will need to edit some of the generated files to connect to our db.
```bash
alembic init src/alembic
```
Replace the code in your `src/alembic/env.py` with the following:
{{<codesnippet `/source_code/diary_tutorial/alembic.py`>}}

Now to make sure our values are registered in the `env.py` script, we need to set our environment variables. 

```bash
export SECRET_ARN=$(cdev output --value hello_world_comp.relationaldb.demo_db.secret_arn)
```
```bash
export CLUSTER_ARN=$(cdev output --value hello_world_comp.relationaldb.demo_db.cluster_arn)
```
```bash
export DB_NAME=<db_name>
```
{{<break 1>}}

You can now create automated migrations. 

{{<tool_tip key="warning" summary="Auto Generation limits">}}
You should familiarize yourself with the [limits of alembic auto generation](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect) and **ALWAYS** confirm the changes before applying them.
{{</tool_tip>}}

```bash
alembic revision --autogenerate -m "Added entries table"
```
Apply the migration with the `upgrade` command. This will create our `Entry` Table.
```bash
alembic upgrade head
```

{{<break 1>}}
Lets now connect to our DB and add an User. The following command will open an interactive session to the database that allows you to execute SQL statments.
```bash
cdev run relationaldb.shell hello_world_comp.demo_db
```
Run the following commands to add a diary entry to your database.
```sql
' (table_name) => ' BEGIN
```
```sql
' (table_name) => 'INSERT INTO entries(title, content) VALUES ('test entry','test our db connection');
```
```sql
' (table_name) => 'COMMIT
```
```bash
' (table_name) => 'quit
```
{{<break 2>}}
## Create Serverless Functions
Now that the database is set up, it is time to add some serverless functions.  We can start by uncommenting lines 5-6, 13, 43-44, and 53-58 of your `src/hello_world/resources.py` file.
{{<break >}}
Then deploy the changes.
```bash
cdev deploy
```

Run the deployed function.
```bash
cdev run function.execute hello_world_comp.hello_world_function
```

Check the logs from the function
```bash
cdev run function.logs hello_world_comp.hello_world_function
```
Next, we will add the routes and functions to create and retrieve our diary entries. First, we will need to add a `src/hello_world/utils.py` file and add the following code to it.

{{<codesnippet `/source_code/diary_tutorial/utils.py`>}}

We will then add the following to our `src/hello_world/resources.py` file on line 14.
```python
from .utils import Response
```

Next, we need to add the following lines below the hello_route on line 24 of `src/hello_world/resources.py` so that our functions will have routes to be associated with.

{{<codesnippet `/source_code/diary_tutorial/routes.py`>}}

We can then add the function for creating entries below the hello function.

{{<codesnippet `/source_code/diary_tutorial/create.py`>}}

We can then add the entry serializer and function for retrieving all the entries below our create function.

{{<codesnippet `/source_code/diary_tutorial/get.py`>}}

Then deploy the changes.
```bash
cdev deploy
```

{{<break 2>}}

## Create and Connect React Frontend
To create a `React` application you will need to install `Node.js`, a `JavaScript Runtime`. 
{{<tool_tip key="info" summary="Node.js Installation Instructions">}}
#### Windows and MacOS
Instructions for Windows and MacOs can be found here: **[Node JS Installers](https://nodejs.org/en/download/)**.

#### Windows Subsystem for Linux(WSL)
WSL instructions can be found here: **[Install Node.js on Windows Subsystem for Linux(WSL)](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl)**.  

{{</tool_tip>}}
The first step is to create a frontend folder in our project to hold our React app. After creating the frontend folder run the following commands.
```bash
cd frontend
```
```bash
npx create-react-app <your-app-name-here>
```
Once the app is initialized run the following commands.

```bash
cd <your-app-name-here>
```
```bash
npm start
```

We can then update our `App.js` file in the `src` folder of our `React` app to the following.

{{<codesnippet `/source_code/diary_tutorial/app.js`>}}

You will need to update the api calls with your API enpoint. At this point you can test your functions on the live server.
 {{<break 1>}}
### Connecting to the Frontend URL
Prepare the `React` application by creating a build folder with the following command:
```bash
npm run build
```
{{<tool_tip key="info" summary="React Build">}}
The command, `npm run build`, minifies files to create a production build of the `React` in order to reduce overall load and render times on the client-side. 
{{</tool_tip>}}

In the root directory, within the `src` folder, create a folder named `content`.

{{<break 1>}}

Use the following command to copy the contents of the `React` app `build` folder to the root `src/content` folder.
```bash
cp -r frontend/<your-app-name-here>/build/* src/content
```
Go to `src/hello_world/resources.py` and add the following code on lines 15-16

```python
from cdev.resources.simple.static_site import StaticSite
myFrontend = StaticSite("demofrontend", content_folder="src/content", index_document='index.html')
```
You also need to add the following line at the bottom of your `src/hello_world/resources.py` file

```python
myProject.display_output("Static Site URl", myFrontend.output.site_url)
```

Now save and deploy the changes.
```bash
cdev plan
```

```bash
cdev deploy
```
{{<break 1>}}

### Push the React Application to Your Site
Sync the front-end, static `React` app, to the `Static Site` with the following command:
```bash
cdev run static_site.sync hello_world_comp.demofrontend  --dir src/content
```

Use the command below to get the url of the `Static Site`. 
```bash
cdev output hello_world_comp.staticsite.demofrontend.site_url
```

Copy and paste it into the browser to view the `Static Site`, and you have successfully created a full-stack web application that you can access from any device with internet.
