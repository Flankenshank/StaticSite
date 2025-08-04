import unittest

from formatting import block_to_block_type,BlockType,markdown_to_blocks,markdown_to_html_node,extract_title

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        heading = "### Hello"     
        heading_result = block_to_block_type(heading)
        self.assertEqual(heading_result, BlockType.heading)

    def test_not_heading(self):
        not_heading = "###Hello"     
        not_heading_result = block_to_block_type(not_heading)
        self.assertEqual(not_heading_result, BlockType.paragraph)

    def test_code(self):
        code = "``` this is some code ```"
        code_result = block_to_block_type(code)
        self.assertEqual(code_result, BlockType.code)

    def test_quote(self):
        quote = "> Quote line 1\n> Quote line 2"
        quote_result = block_to_block_type(quote)
        self.assertEqual(quote_result, BlockType.quote)

    def test_unordered(self):
        unordered = "- Unordered list line 1\n- Unordered list line 2\n- Unordered list line 3"
        unordered_result = block_to_block_type(unordered)
        self.assertEqual(unordered_result, BlockType.unordered_list)     

    def test_ordered(self):
        ordered = "1. Ordered list line 1\n2. Ordered list line 2\n3. Ordered list line 3"
        ordered_result = block_to_block_type(ordered)
        self.assertEqual(ordered_result, BlockType.ordered_list)  



    def test_paragraphs(self):
        md = """
        This is **bolded** paragraph
        text in a p
        tag here

        This is another paragraph with _italic_ text and `code` here

        """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
            ```
            This is text that _should_ remain
            the **same** even with inline stuff
            ```
            """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_h1_header(self):
        md = "# This is an h1 header\n## This is not an h1 header\nThis is a paragraph"
        self.assertEqual(extract_title(md),"This is an h1 header")

    def test_no_h1_header(self):
        md = "## This is not an h1 header\nThis is a paragraph"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_h1_header_line_2(self):
        md = "## This is not an h1 header\n# The h1 header is not on the first line\nThis is a paragraph"
        self.assertEqual(extract_title(md),"The h1 header is not on the first line")

    def test_h1_header_spaces(self):
        md = "#      This is an h1 header with more spaces\n## This is not an h1 header\nThis is a paragraph"
        self.assertEqual(extract_title(md),"This is an h1 header with more spaces")

if __name__ == "__main__":
    unittest.main()