from textnode import TextNode, TextType 

from regex import extract_markdown_images, extract_markdown_links

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

def split_nodes_image(old_nodes):
    result = []
    
    for old_node in old_nodes:
        # If the node is not a TEXT type, just add it as is
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        
        # Get the text and find all images
        current_text = old_node.text  # This is a string
        images = extract_markdown_images(current_text)
        
        # If no images found, just add the original node
        if not images:
            result.append(old_node)
            continue
        
        # Process images one by one
        remaining_text = current_text
        
        for image_alt, image_url in images:
            # Create the full image markdown
            image_markdown = f"![{image_alt}]({image_url})"
            
            # Split at the image markdown
            parts = remaining_text.split(image_markdown, 1)  # This split is on a string
            
            # Add text before the image (if not empty)
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
            
            # Add the image node
            result.append(TextNode(image_alt, TextType.IMAGE, image_url))
            
            # Update remaining text for next iteration
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        # Add any remaining text after the last image
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    
    return result



def split_nodes_link(old_nodes):
    result = []
    
    for old_node in old_nodes:
        # If the node is not a TEXT type, just add it as is
        if old_node.text_type != TextType.TEXT:
            result.append(old_node)
            continue
        
        original_text = old_node.text
        links = extract_markdown_links(original_text)

        if not links:
            result.append(old_node)
            continue
        
        remaining_text = original_text
        
        for link_text, link_url in links:
            link_markdown = f"[{link_text}]({link_url})"
            
            parts = remaining_text.split(link_markdown, 1)
            
            if parts[0]:
                result.append(TextNode(parts[0], TextType.TEXT))
            
            result.append(TextNode(link_text, TextType.LINK, link_url))
            
            if len(parts) > 1:
                remaining_text = parts[1]
            else:
                remaining_text = ""
        
        if remaining_text:
            result.append(TextNode(remaining_text, TextType.TEXT))
    
    return result

    def text_to_textnodes(text):
        