import re
from typing import Dict, Pattern, Tuple
from dataclasses import dataclass


@dataclass
class MessageRecord:
    timestamp: int
    author: str
    text: str


@dataclass
class Highlight:
    start: float
    end: float
    messages_count: int
    authors: set[str]


@dataclass
class HighlightConfig:
    keywords: Pattern
    messages_interval: float
    min_messages: int


def get_chat_highlights(
    records: Tuple[MessageRecord, ...], config: HighlightConfig
) -> Dict[str, Highlight]:
    pass
