{
    "type": "gettingstarted",
    "layout": "type",
    "title": "Install Python",
    "linktitle": "python", 
    "card_icon": "ti-server",
    "card_body": "Install a compatible version of Python and some additional tools",
    "weight": "1"
}

# Setting up Python
{{<header_divider>}}


The Cdev Sdk is a Python Library and CLI that helps developers with Serverless Development, which means that you will need to have Python installed on your computer and access to a CLI environment.


{{<break 1>}}
## Installing Python
There are many ways of installing Python depending on what Operating System you are using, but the [real python website has a fairly comprehensive guide](https://realpython.com/installing-python/) for installing Python.


{{<break 1>}}
## Check Python version

```bash
python --version
```

Your version should be 3.7, 3.8, or 3.9.


{{<break 1>}}
## Check For Pip
Pip is the third party package management tool for Python. It will be how you install the Cdev Sdk and any other external libraries you need. It should come by default when you install Python.
```
pip -h
```

{{<break 1>}}

## Install Python Virtualenv
It is helpful to use [virtual environments](https://realpython.com/python-virtual-environments-a-primer/) to keep dependencies for different project isolated. You can install the [virtualenv tool](https://virtualenv.pypa.io/en/latest/) from pip to help manage your virtual environments. 

```bash
pip install virtualenv
```

{{<tool_tip key="tip" summary="Using Virtual Environments">}}
For each `Project` you will create and activate your virtual environment.
```
python -m virtualenv .venv

# or 
python3 -m virtualenv .venv
```
```
. ./.venv/bin/activate
```
{{</tool_tip>}}

{{<break 2>}}