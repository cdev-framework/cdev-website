import re
from typing import List, Tuple

starts_with_url_regex_str = r"^(?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’])"
starts_with_url_regex = re.compile(starts_with_url_regex_str)

hash_tag_regex_str = "(#[\S]*)"
hash_tag_regex = re.compile(hash_tag_regex_str)

class ParsingError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'Parsing Error -> {self.message}'


def parse_message(message: str) -> Tuple[str, str, List[str]]:
    """Service to parse a text message into structured data about a link.

    Args:
        message (str): the message
        from_id (str): id of the sender of the message

    Returns:
        str: The Url
        str: Description for the Url
        List[str]: Tags for the Url

    Raises:
        ParsingError: An error occurred parsing the message.
    """

    matched_url = starts_with_url_regex.search(message)
    
    if matched_url:
        _, url_end  = matched_url.span()

        url = message[:url_end]
        description_tags = message[url_end+1:]

        if description_tags:
            description, tags = _parse_description_tags(description_tags)
        else:
            description = ""
            tags = []

        return url, description, tags

    raise ParsingError(f"Could not match url in {message}")


def _parse_description_tags(body: str) -> Tuple[str, List[str]]:
    """From a string of the form: <description> [#<tag>] parse the description and list of tags.

    Args:
        body (str): String contains the description and tags

    Returns:
        str: Description
        List[str]]: Tags

    Example:
        input: 'intersting article #blog #python #learning'
        output: ('intersting article', ['blog', 'python', 'learning'])
    """

    parts = body.split("#", 1)
    description = parts[0].strip()

    if len(parts) == 1:
        return description, []

    raw_hashtags = "#" + parts[1]
    try:
        hash_tag_list = hash_tag_regex.findall(raw_hashtags)
        hash_tags = [x[1:] for x in hash_tag_list]
    except Exception as e:
        hash_tags = []

    return description, hash_tags