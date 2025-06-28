from enum import Enum
import re
from htmlnode import HTMLNode
from delimiter import text_to_textnodes
from textnode import text_node_to_html_node,TextNode,TextType

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

def markdown_to_html_node(markdown):
    block_nodes = []
    for block in markdown_to_blocks(markdown):
        blocktype = block_to_block_type(block)
        if blocktype == BlockType.heading:
            match = re.match(r"^(#{1,6}) ", block)
            if match:
                num_hashes = len(match.group(1))
                heading_text = block[match.end():]
                block_nodes.append(HTMLNode(tag=f"h{num_hashes}", value=None, children=text_to_children(heading_text), props=None))
        
        if blocktype == BlockType.quote:
            lines = block.split('\n')
            cleaned_lines = []
            for line in lines:
                cleaned_lines.append(line.lstrip("> "))
            final_text = "\n".join(cleaned_lines)
            block_nodes.append(HTMLNode(tag="blockquote", value=None, children=text_to_children(final_text), props=None))

        if blocktype == BlockType.unordered_list:
            lines = block.split('\n')
            li_objects = []
            for line in lines:
                cleaned_line = line.lstrip("- ")
                li_objects.append(HTMLNode(tag="li", value=None, children=text_to_children(cleaned_line), props=None))
            block_nodes.append(HTMLNode(tag="ul", value=None, children=li_objects, props=None))

        if blocktype == BlockType.ordered_list:
            lines = block.split('\n')
            li_objects = []
            for line in lines:
                cleaned_line = re.sub(r'^\d+\. ', '', line)
                li_objects.append(HTMLNode(tag="li", value=None, children=text_to_children(cleaned_line), props=None))
            block_nodes.append(HTMLNode(tag="ol", value=None, children=li_objects, props=None))

        if blocktype == BlockType.paragraph:
            cleaned_block = re.sub(r'\s+', ' ', block.strip())
            block_nodes.append(HTMLNode(tag="p", value=None, children=text_to_children(cleaned_block), props=None))

        if blocktype == BlockType.code:
            lines = block.split('\n')
            code_lines = lines[1:-1]
            stripped_lines = [line.lstrip() for line in code_lines]
            code_content = '\n'.join(stripped_lines)
            if code_content and not code_content.endswith('\n'):
                code_content += '\n'
            text_node = TextNode(code_content, TextType.TEXT)
            code_html_node = text_node_to_html_node(text_node)
            code_node = HTMLNode(tag="code", children=[code_html_node])
            pre_node = HTMLNode(tag="pre", children=[code_node])
            block_nodes.append(pre_node)
        
    return HTMLNode(tag="div", children=block_nodes)

def text_to_children(block):
    Nodes_list = []
    objects = text_to_textnodes(block)
    for object in objects:
        Nodes_list.append(text_node_to_html_node(object))
    return Nodes_list






