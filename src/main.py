import shutil
import os
import sys

from generator import generate_pages_recursive

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, ".."))

public_dir = os.path.join(project_root, "docs")
static_dir = os.path.join(project_root, "static")

def copy_static(src, dest):
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dest_path = os.path.join(dest, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        elif os.path.isdir(src_path):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            copy_static(src_path, dest_path)


def main():
    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)
    copy_static(static_dir, public_dir)

    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    # Now pass basepath to the function
    generate_pages_recursive("content", "template.html", public_dir, basepath)

if __name__ == "__main__":
    main()