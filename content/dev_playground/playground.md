{
    "type": "dev_playground",
    "layout": "type",
    "title": "Different Code Snippets",
    "linktitle": "functions",
    "card_icon": "ti-infinite",
    "card_body": "Playground for code snippets",
    "weight": "1"
}


# Code Snippets
{{<header_divider>}}


## Header 2

### Header 3

#### Header 4


**bold text**
{{<break 1>}}
*italic text*
{{<break 1>}}
[A link to google](https://google.com)
{{<break 3>}}

## Emphasis 
`emphasized text`

{{<break 1>}}

## Single Commands 
Single commands can be written inside a code block with the language set to bash

```bash
cdev run function.execute <component_name>.hello_function
```

{{<break 1>}}
## Code Snippets
Render a python file with line numbers, syntax highlighting, and a  copy button
{{<codesnippet `/source_code/function_examples/basic_function.py`>}}


{{<break 1>}}
## Tooltips
Tools tips provide a way for surfacing information to the user that is collapsible and categorized by a color and icon to help communicate the message.  


{{<tool_tip key="info" summary="Some Title">}}
Info tool tips provide additional information about documentation. 
{{</tool_tip>}}

{{<tool_tip key="tip" summary="Some Title">}}
Tips provide helpful tips about documentation. Also any `tool_tip` can itself contain rendered markdown content.

```bash
some command
```

{{</tool_tip>}}

{{<tool_tip key="warning" summary="Some Title">}}
Tips provide helpful warnings about documentation
{{</tool_tip>}}


{{<tool_tip key="error" summary="Some Title">}}
Tips provide helpful errors about documentation
{{</tool_tip>}}


{{<tool_tip key="question" summary="Some Title">}}
What is the meaning of life? 42
{{</tool_tip>}}


{{<tool_tip key="python" summary="Test">}}
Something about python
{{</tool_tip>}}


## Images
{{<tutorial_image>}}
/images/link_bot_tutorial/notion_share_db_with_integration.png
{{</tutorial_image>}}


## Block Quote 

{{<blockquote>}}
What are bots? 
{{<break 2>}}
A bot is a type of Slack App designed to interact with users via conversation.
{{<break 2>}}
A bot is the same as a regular app: it can access the same range of APIs and do all of the magical things that a Slack App can do.
{{<break 1>}}
But when you build a bot for your Slack App, you're giving that app a face, a name, and a personality, and encouraging users to talk to it.
{{<break 2>}}
Your bot can send DMs, it can be mentioned by users, it can post messages or upload files, and it can be invited to channels - or kicked out.

{{<break 2>}}
-Slack Documentation
{{</blockquote>}}
