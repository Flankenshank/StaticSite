import unittest

from formatting import block_to_block_type,BlockType

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

if __name__ == "__main__":
    unittest.main()