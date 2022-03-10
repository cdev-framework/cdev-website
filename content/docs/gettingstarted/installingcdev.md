{
    "type": "gettingstarted",
    "layout": "type",
    "title": "Installing the Cdev Sdk",
    "linktitle": "gettingstarted", 
    "card_icon": "ti-package",
    "card_body": "Install and configure the Cdev Sdk",
    "weight": "3"
}

## Install the Cdev Sdk

```bash
pip install cdev
```


## Create Your First Project
```bash
cdev init demo-project --template quick-start
```


Deploy the Template Project
```bash
cdev deploy
```

Invoke the deployed function directly from the cli
```bash
cdev run function.execute hello_world_comp.hello_world_function
```

You might have to wait a sec for the logs to process in the cloud
```bash
$ cdev run function.logs hello_world_comp.hello_world_function
```

Invoke the deployed function via the created HTTP Api
```bash
cdev output hello_world_comp.api.demoapi.endpoint
```
outputs
```
<your-url>
```

Call your Api Endpoint
```bash
$ curl <url>/hello_world
```

You can also visit `<url>/hello_world` in your favorite web browser!

Delete the Resources in the Environment
```
$ cdev destroy
```
