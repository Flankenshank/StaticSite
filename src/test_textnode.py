import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

# Test for inequality with different text
    def test_different_text(self):
        node = TextNode("First text", TextType.BOLD)
        node2 = TextNode("Different text", TextType.BOLD)
        self.assertNotEqual(node, node2)

# Test for inequality with different text_type
    def test_different_type(self):
        node = TextNode("Same text", TextType.BOLD)
        node2 = TextNode("Same text", TextType.ITALIC)
        self.assertNotEqual(node, node2)

# Test for equality with url=None (default)
    def test_url_none(self):
        node = TextNode("Text with no URL", TextType.LINK)
        node2 = TextNode("Text with no URL", TextType.LINK)
        self.assertEqual(node, node2)

# Test for inequality with different urls
    def test_different_url(self):
        node = TextNode("Link text", TextType.LINK, "https://example.com")
        node2 = TextNode("Link text", TextType.LINK, "https://different.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()