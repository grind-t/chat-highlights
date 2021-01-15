import re
from dataclasses import dataclass


@dataclass
class MessageRecord:
    timestamp: int
    author: str
    text: str


@dataclass
class Highlight:
    keyword: str
    start_timestamp: int
    end_timestamp: int
    messages_count: int
    authors: set[str]


@dataclass
class HighlightConfig:
    keywords: re.Pattern
    timestamps_interval: int
    min_messages: int


def get_chat_highlights(
    records: tuple[MessageRecord, ...], config: HighlightConfig
) -> list[Highlight]:
    active: dict[str, Highlight] = {}
    ended: list[Highlight] = []
    for record in records:
        match = config.keywords.search(record.text)
        if not match:
            continue
        for keyword in match.groups():
            if not keyword:
                continue
            highlight = active.get(keyword)
            if not highlight:
                active[keyword] = Highlight(
                    keyword, record.timestamp, record.timestamp, 1, {record.author}
                )
                continue
            if record.author in highlight.authors:
                continue
            dt = record.timestamp - highlight.end_timestamp
            if dt <= config.timestamps_interval:
                highlight.end_timestamp = record.timestamp
                highlight.messages_count += 1
                highlight.authors.add(record.author)
            elif highlight.messages_count >= config.min_messages:
                ended.append(highlight)
                del active[keyword]
    for highlight in active.values():
        if highlight.messages_count >= config.min_messages:
            ended.append(highlight)
    return ended
