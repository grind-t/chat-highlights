from unittest import TestCase
import re
from chat_highlights import (
    Highlight,
    HighlightConfig,
    MessageRecord,
    get_chat_highlights,
)

class TestChatHighlights(TestCase):
    def setUp(self):
        self.config = HighlightConfig(re.compile(r"(ha)?(roflan)?"), 4, 2)

    def test_get_chat_highlights(self):
        records = (
            MessageRecord(1000000, "author1", "haha"),
            MessageRecord(2000000, "author1", "roflanZdarova"),
            MessageRecord(5000000, "author2", "haha"),
            MessageRecord(5500000, "author2", "roflanZdarova"),
            MessageRecord(6000000, "author2", "roflanPominki"),
            MessageRecord(10000000, "author3", "haha"),
        )
        actual = get_chat_highlights(records, self.config)
        expected = {
            "haha": Highlight(1000000, 5000000, 2, set("author1", "author2")),
            "roflan": Highlight(2000000, 5500000, 2, set("author1", "author2")),
        }
        self.assertDictEqual(actual, expected)
