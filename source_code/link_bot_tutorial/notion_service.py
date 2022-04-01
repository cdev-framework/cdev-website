import os
from notion_client import Client
from typing import Dict, List


NOTION_TOKEN = "NOTION_TOKEN"
NOTION_DB_ID = "NOTION_DB_ID"

notion_token = os.environ.get(NOTION_TOKEN)
notion_db_id = os.environ.get(NOTION_DB_ID)

notion_client = Client(auth=notion_token)

def save_info_notion(url: str, description: str, tags: List[str]) -> str:
    print(f"url {url}; description {description}; tags {tags}")
    notion_client.pages.create(**{
        "parent": { "database_id": notion_db_id },
        "properties": create_properties(description, url, tags)
        }  
    )
    print(f"Added info to database {notion_db_id}")

    return u"Saved to Notion \u2705"


def create_properties(description: str, url: str, tags: List[str]) -> Dict:
    tag_list = [{"name": x} for x in tags]

    return {
        "Description": {
            "title": [
                {
                    "text": {
                        "content": description
                    }
                }
            ],
        },
        "link": {
            "url": url,
        },
        "Tags": {
            "multi_select": tag_list
        },
        "Status": {
            "multi_select": [
                {"name":"Unread"}
            ]
        },
    }
