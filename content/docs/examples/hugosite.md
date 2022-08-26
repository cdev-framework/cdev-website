{
    "type": "examples",
    "layout": "type",
    "title": "Host a Hugo Frontend",
    "linktitle": "static sites",
    "card_icon": "ti-desktop",
    "card_body": "Learn how to host a static frontend with the Static Site Resource",
    "weight": "2"
}


# Host a Hugo Frontend with the Static Site Resource
{{<header_divider>}}

Many websites are built using front-end libraries, frameworks and static site generators to improve performance, user experience, and reduce cost. Cdev can easily integrate these technologies with the `Static Site` resource to host your static front-end content.

{{<break 1>}}

## Sync a Hugo Site to the Static Site Resource
`Hugo` is a static website generator that converts content files, written in markdown, to static HTML and CSS pages. This example shows how Cdev hosts a Hugo site with the `Static Site` Resource.

{{<tool_tip key="info" summary="Hugo Documentation">}}
For more information about how to use `Hugo`, visit the **[official documentation](https:/https://gohugo.io/)**. 
{{</tool_tip>}}

{{<break 1>}}
### Requirements
To generate a static site, you will need to have `Git` and `Hugo` installed. 
{{<tool_tip key="info" summary="Hugo Installation Instructions">}}

#### Git
Instructions for installing `Git` can be found **[here](https://git-scm.com/downloads)**

#### Hugo

You can find the instructions for installing `Hugo` on your system **[here](https://gohugo.io/getting-started/installing/)**.
{{</tool_tip>}}

{{<break 1>}}

Use the following command to start a new project. 
```bash
cdev init hugo-project
```

{{<break 1>}}
### Generate a Hugo Site
We will use the **[Hugo quickstart](https://gohugo.io/getting-started/quick-start/)** guide to generate a site. 

In the root of the project folder, initialize a new `Hugo` site with the following command:
```bash
hugo new site quickstart
```

The file structure will now look like this:
{{<tutorial_image>}}
/images/staticsite_examples/hugo_example/hugo_structure.png
{{</tutorial_image>}}

{{<break 2>}}
### Add a Theme
Using the terminal, navigate into the `quickstart` folder and run the following commands:
{{<tool_tip key="warning" summary="Initializing a Repository">}}
Ensure that a git repository(git init) is initialized from within the `quickstart` folder prior to adding the theme submodule.

{{</tool_tip>}}

```bash
git init
```
```bash
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
```
{{<tool_tip key="info" summary="Hugo Themes">}}

Hugo themes can be downloaded from **[the official documentation](https://themes.gohugo.io/)**. It is accepted practice to add a theme as a `git submodule`. 
{{</tool_tip>}}

Next, use the command below to add the theme to the `quickstart/config.toml` file. 
```bash
echo theme = \"ananke\" >> config.toml
```
The file structure will now look like this:
{{<tutorial_image>}}
/images/staticsite_examples/hugo_example/hugo_config_theme.png
{{</tutorial_image>}}

{{<break 1>}}
Use the following command to add a sample blog post to the site.
```bash
hugo new posts/my-first-post.md
```
Start the `hugo server`.
```bash
hugo server -D
```
{{<tool_tip key="info" summary="Hugo Server">}}

You can find out more about `Hugo` server's options and limitations in the  **[the official documentation](https://gohugo.io/commands/hugo_server/)**. 
{{</tool_tip>}}

View your site, locally, at `http://localhost:1313/`.
{{<tutorial_image>}}
/images/staticsite_examples/hugo_example/hugo_local.png
{{</tutorial_image>}}

{{<break 2>}}
### Build Hugo Site
{{<tool_tip key="warning" summary="Hugo Build">}}
The build command must be executed from within the `quickstart` folder.

{{</tool_tip>}}
Use the command below to create a build folder of the `Hugo` site.
```bash
hugo -D
```
{{<tool_tip key="info" summary="Hugo Build">}}
The command `hugo`, builds the `Hugo` site. For the purposes of this example, the `-D` flag is utilized to include content marked as drafts in the build. To see where content is marked as a draft in this example, view the `quickstart/content/posts/my-first-post.md` file.

{{</tool_tip>}}

{{<break 1>}}

In the root directory, within the `src` folder, create a folder named `content` and use the following command to copy the contents of the `Hugo` site's `public` folder to the root `src/content` folder.
```bash
cp -r quickstart/public/* src/content
```
{{<tool_tip key="info" summary="Public Folder">}}
The `public folder` is created by the build command, `hugo`, and contains the files that can be uploaded to a web server for your `Hugo` site.

{{</tool_tip>}}
The file structure should look like this:
{{<tutorial_image>}}
/images/staticsite_examples/hugo_example/hugo_src_structure.png
{{</tutorial_image>}}

{{<break 1>}}
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
### Push the Hugo Generated Site to Your Static Site 
Use the commands below to sync the new `Hugo` site, to the `Static Site` and get the url.
```bash
cdev run static_site.sync hello_world_comp.demofrontend  --dir src/content
```
```bash
cdev output hello_world_comp.staticsite.demofrontend.site_url
```

Use the url to view the `Hugo` `Static Site`.
{{<tutorial_image>}}
/images/staticsite_examples/hugo_example/hugo_site.png
{{</tutorial_image>}}





{{<break 1>}}
