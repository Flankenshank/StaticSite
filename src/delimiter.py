from textnode import TextNode, TextType 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception ("invalid markdown syntax")
            for idx, part in enumerate(parts):
                if idx % 2 == 0:
                    new_node = TextNode(part, TextType.TEXT)
                else:
                    new_node = TextNode(part, text_type)
                if part:
                    new_nodes.append(new_node)
        else:
            new_nodes.append(node)
    return new_nodes
