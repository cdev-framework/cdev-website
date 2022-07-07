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


In this tutorial, we will be going through the entire process of creating a full stack application with Cdev. We will be focusing on demonstrating how Cdev can integrate with standard python tools and other development workflows to create a great developer experience. We will explain all the components and steps of this tutorial in depth, but it does help to have some familiarity with some of the technologies and concepts around full stack development.

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

Now we can deploy our project to get a live Webhook

```bash
cdev deploy
```
This step should output the live url of your webhook and look like
```
Base API URL -> <your-endpoint>
```

{{<break>}}

## Create Database Connection
For this project we will be utilizing a relational database and the SqlAlchemy ORM.  An in-depth example of how to set up SqlAlchemy ORM can be found in the examples section of our website as a part of the ["Integrate RelationalDBs"](https://cdevframework.io/docs/examples/relationaldb/#sqlalchemy-orm)chapter. 