import os
from formatting import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    with open(template_path, 'r') as file:
        template_content = file.read()
    page_title = extract_title(markdown_content)
    html_content = markdown_to_html_node(markdown_content).to_html()
    html_page = template_content.replace("{{ Title }}", page_title)
    html_page = html_page.replace("{{ Content }}", html_content)

    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(html_page)