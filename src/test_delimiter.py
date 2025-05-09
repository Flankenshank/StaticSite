import unittest

from delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestDelimiter(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [TextNode("This is a text node", TextType.TEXT)])

    def test_delimiter_code(self):
        node = TextNode("A line with `inline code` inside.", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("A line with ", TextType.TEXT),
            TextNode("inline code", TextType.CODE),
            TextNode(" inside.", TextType.TEXT)
              ]
        self.assertEqual([n.text for n in result], [n.text for n in expected])
        self.assertEqual([n.text_type for n in result], [n.text_type for n in expected])

if __name__ == "__main__":
    unittest.main()