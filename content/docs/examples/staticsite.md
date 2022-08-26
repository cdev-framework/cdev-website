{
    "type": "examples",
    "layout": "type",
    "title": "Host a React Frontend",
    "linktitle": "static sites",
    "card_icon": "ti-desktop",
    "card_body": "Learn how to host a static frontend with the Static Site Resource",
    "weight": "1"
}


# Host a React Frontend with the Static Site Resource
{{<header_divider>}}

Many websites are built using front-end libraries, frameworks and static site generators to improve performance, user experience, and reduce cost. Cdev can easily integrate these technologies with the `Static Site` resource to host your static front-end content.

{{<break 1>}}
## Host React JS with the Static Site Resource

`React(React.js or ReactJS)` is one of the most popular front-end libraries. This example will show how `Cdev` can easily integrate `React` with the `Static Site` resource. 

{{<tool_tip key="info" summary="React Documentation">}}
For more information about how to use `React`, visit the **[official documentation](https:/reactjs.org/)**. 
{{</tool_tip>}}

{{<break 1>}}

### Requirements
To create a `React` application you will need to install `Node.js`, a `JavaScript Runtime`. 
{{<tool_tip key="info" summary="Node.js Installation Instructions">}}

#### Windows and MacOS
Instructions for Windows and MacOs can be found here: **[Node JS Installers](https://nodejs.org/en/download/)**.

#### Windows Subsystem for Linux(WSL)
WSL instructions can be found here: **[Install Node.js on Windows Subsystem for Linux(WSL)](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl)**.  

{{</tool_tip>}}
{{<break 1>}}

Use the following command to start a new project. 
```bash
cdev init react-project
```

{{<break 1>}}

### Create a React Application
In the root of your project folder, create a `React` app with the following command:
```bash
npx create-react-app <your-app-name-here>
```
For example:
```bash
npx create-react-app my-react-app
```
Once the `React` app is created, the file structure will look like this:
{{<tutorial_image>}}
/images/staticsite_examples/react_example/react_structure.png
{{</tutorial_image>}}
{{<break 1>}}

Using the terminal, enter the folder that contains the `React` app and start the local server to confirm that the `React` app was created correctly.
```bash
cd <your-app-name-here>
npm start
```
For example:
```bash
cd my-react-app
npm start
```
This should be the output of `http://localhost:3000`:
{{<tutorial_image>}}
/images/staticsite_examples/react_example/react_local_host.png
{{</tutorial_image>}}
{{<break 2>}}

### Connect the React App to the Static Site Resource
Prepare the `React` application by creating a build folder with the following command:
```bash
npm run build
```
{{<tool_tip key="info" summary="React Build">}}
The command, `npm run build`, minifies files to create a production build of the `React` app in order to reduce overall load and render times on the client-side. 
{{</tool_tip>}}

In the root directory, within the `src` folder, create a folder named `content`.
{{<tutorial_image>}}
/images/staticsite_examples/react_example/react_src_structure.png
{{</tutorial_image>}}
{{<break 1>}}

Use the following command to copy the contents of the `React` app `build` folder to the root `src/content` folder.
```bash
cp -r <your-app-name-here>/build/* src/content
```
For example:
```bash
cp -r my-react-app/build/* src/content
```
The file structure should look like this:
{{<tutorial_image>}}
/images/staticsite_examples/react_example/react_src_structure.png
{{</tutorial_image>}}
{{<break 2>}}

### Add Static Site Resource
Go to `hello_world/resources.py` and add the code at `lines 6, 26 and 30`.
```bash
# Generated as part of Quick Start project template 

from cdev.resources.simple.api import Api
from cdev.resources.simple.xlambda import simple_function_annotation

from cdev.resources.simple.static_site import StaticSite

from cdev import Project as cdev_project

myProject = cdev_project.instance()

DemoApi = Api("demoapi")

hello_route = DemoApi.route("/hello_world", "GET")

@simple_function_annotation("hello_world_function", events=[hello_route.event()])
def hello_world(event, context):
    print('Hello from inside your Function!')


    return {
        "status_code": 200,
        "message": "Hello Outside World!"
    }

myFrontend = StaticSite("demofrontend", content_folder="src/content", index_document='index.html')

myProject.display_output("Base API URL", DemoApi.output.endpoint)
myProject.display_output("Routes", DemoApi.output.endpoints)
myProject.display_output("Static Site URl", myFrontend.output.site_url)
```
Save and deploy the changes.
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

Copy and paste the url into the browser to view the `Static Site`, `React` app.
{{<tutorial_image>}}
/images/staticsite_examples/react_example/react_site.png
{{</tutorial_image>}}
{{<break 2>}}

{{<break 1>}}

