from typing import Pattern
from dataclasses import dataclass
from re import compile, match


@dataclass
class MessageRecord:
    timestamp: int
    author: str
    text: str


def get_chat_highlights(records: MessageRecord, keywords: Pattern, messages_interval: float, min_messages: float):
    pass
