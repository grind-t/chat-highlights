import re
from unittest import TestCase, main
from chat_highlights import (
    Highlight,
    HighlightConfig,
    MessageRecord,
    get_chat_highlights,
)


class TestChatHighlights(TestCase):
    def setUp(self):
        regex = re.compile(r"(ha)?(roflan)?")
        microsecs = 4 * 1000000
        min_messages = 2
        self.config = HighlightConfig(regex, microsecs, min_messages)

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
        expected = [
            Highlight("ha", 1000000, 5000000, 2, {"author1", "author2"}),
            Highlight("roflan", 2000000, 5500000, 2, {"author1", "author2"}),
        ]
        self.assertListEqual(actual, expected)


if __name__ == "__main__":
    main()