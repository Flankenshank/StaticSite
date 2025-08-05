import os
from formatting import markdown_to_html_node, extract_title

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, 'r') as file:
        markdown_content = file.read()
    with open(template_path, 'r') as file:
        template_content = file.read()
    page_title = extract_title(markdown_content)
    html_content = markdown_to_html_node(markdown_content).to_html()
    html_page = template_content.replace("{{ Title }}", page_title)
    html_page = html_page.replace("{{ Content }}", html_content)
    html_page = html_page.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    dir_path = os.path.dirname(dest_path)
    os.makedirs(dir_path, exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(html_page)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    contents = os.listdir(dir_path_content)
    for i in contents:
        if not os.path.isfile(os.path.join (dir_path_content, i)):
            dir = os.path.join (dir_path_content, i)
            generate_pages_recursive(dir, template_path, dir.replace("content", "docs"), basepath)
        else:
            if i.endswith(".md"):
                dir = os.path.join (dir_path_content, i)
                dest_dir = dir.replace("content", "docs").replace(".md", ".html")
                dest_directory = os.path.dirname(dest_dir)
                os.makedirs(dest_directory, exist_ok=True)
                generate_page(dir, template_path, dest_dir, basepath)
