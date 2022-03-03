from typing import Optional

from core.constructs.settings import Settings


class CustomSettings(Settings):
    SOME_KEY: str = ""
    ANOTHER_KEY: int = ""
    FINAL_KEY: Optional[str]
