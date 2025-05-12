import unittest

from delimiter import split_nodes_delimiter, split_nodes_image, split_nodes_link
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

class TestSplitters(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and another [second link](https://blog.boot.dev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second link", TextType.LINK, "https://blog.boot.dev"),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("This is text with no images", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual([node], new_nodes)

    def test_split_images_no_links(self):
        node = TextNode("This is text with no links", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual([node], new_nodes)


    def test_split_images_non_text_node(self):
    # Create a node that's not TextType.TEXT
        node = TextNode("alt text", TextType.IMAGE, "https://example.com/image.png")
        new_nodes = split_nodes_image([node])
    # Expect the node to be returned unchanged
        self.assertListEqual([node], new_nodes)
    
    def test_split_links_non_text_node(self):
    # Create a node that's not TextType.TEXT
        node = TextNode("link text", TextType.LINK, "https://example.com")
        new_nodes = split_nodes_link([node])
    # Expect the node to be returned unchanged
        self.assertListEqual([node], new_nodes)

if __name__ == "__main__":
    unittest.main()