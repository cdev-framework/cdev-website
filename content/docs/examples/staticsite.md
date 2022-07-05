{
    "type": "examples",
    "layout": "type",
    "title": "Integrate React JS",
    "linktitle": "static sites",
    "card_icon": "ti-infinite",
    "card_body": "Learn how to connect React to the Static Site Resource",
    "weight": "1"
}

# Connect React JS to the Static Site Resource
{{<header_divider>}}

Many websites are built using a front-end library or framework. `React(React.js or ReactJS)` is one of the most popular front-end libraries. `React` can easily integrate with `Cdev` to be a static site resource and complement the backend. For more information about how to use `React`, visit the **[official documentation](https:/reactjs.org/)**.

{{<break 1>}}

## Requirements
To create a `React` application you will need to install `Node.js`, a JavaScript runtime, on your `Windows Subsystem for Linux`. The instructions can be found here: **[Install Node.js on Windows Subsystem for Linux(WSL)](https://docs.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-wsl)** . 
{{<break 1>}}

The initial file structure should resemble the image below. If this is not your starting point for this example, consult the `Getting Started` section to initialize a `Cdev project` before continuing.

{{<tutorial_image>}}
/images/react_example/init_img.png
{{</tutorial_image>}}
{{<break 2>}}

## Create a React Application
In the root of your project folder, create a `React` app with the following command:
```bash
npx create-react-app <your-app-name-here>
# example
npx create-react-app my-react-app
```
Once the `React` app is created, the file structure will look like this:
{{<tutorial_image>}}
/images/react_example/react_file_structure.png
{{</tutorial_image>}}
{{<break 1>}}

Using the terminal, enter the folder that contains the `React` app and start the local server to confirm that the `React` app was created correctly.
```bash
cd <your-app-name-here>
npm start

#example 
cd my-react-app
npm start
```
This should be the output of `http://localhost:3000`:
{{<tutorial_image>}}
/images/react_example/react_local_host.png
{{</tutorial_image>}}
{{<break 2>}}

## Connect the React App to the Static Site Resource
Prepare the `React` application by creating a build folder with the following command:
```bash
npm run build
```
{{<tool_tip key="info" summary="React Build">}}
The command, `npm run build`, minifies files to create a production build of the `React` in order to reduce overall load and render times on the client-side. 
{{</tool_tip>}}

In the root directory, within the `src` folder, create a folder named `content`.
{{<tutorial_image>}}
/images/react_example/root_src.png
{{</tutorial_image>}}
{{<break 1>}}

Use the following command to copy the contents of the `React` app `build` folder to the root `src/content` folder.
```bash
cp -r <your-app-name-here>/build/* src/content

#example
cp -r my-react-app/build/* src/content
```
The file structure should look like this:
{{<tutorial_image>}}
/images/react_example/src_with_build_contents.png
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
Now save and deploy the changes.
```bash
cdev plan
cdev deploy
```
{{<break 1>}}

### Push the React Application to Your Site
Sync the front-end, static `React` app, to the static site with the following command:
```bash
cdev run static_site.sync hello_world_comp.demofrontend  --dir src/content
```

Use the command below to get the url of the static site. 
```bash
cdev output hello_world_comp.staticsite.demofrontend.site_url
```

Copy and paste it into the browser to view the `Static Site`, `React` app.
{{<tutorial_image>}}
/images/react_example/react_site.png
{{</tutorial_image>}}
{{<break 2>}}

{{<break 1>}}


