from enum import Enum
import re

def markdown_to_blocks(markdown):
    blocks = []
    for block in markdown.split('\n\n'):
        block = block.strip()
        if len(block):
            blocks.append(block)
    return blocks

class BlockType(Enum):
    paragraph = 1
    heading = 2
    code = 3
    quote = 4
    unordered_list = 5
    ordered_list = 6

def block_to_block_type(markdown):
    if re.match(r"^#{1,6} ", markdown):
        return BlockType.heading
    
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.code
    
    lines = markdown.split('\n')
    if all(line.startswith(">") for line in lines):
        return BlockType.quote
    
    if all(line.startswith("- ") for line in lines):
        return BlockType.unordered_list
    
    if all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
        return BlockType.ordered_list
    
    return BlockType.paragraph