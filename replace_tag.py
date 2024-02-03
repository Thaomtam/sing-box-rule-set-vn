import re
import os
import json

def replace_tags():
    # Đọc tệp readme.json để lấy giá trị của biến VERSION
    with open('readme.json') as f:
        variables = json.load(f)
        version = variables.get("VERSION", "")

    # Đọc tất cả các tệp .md
    readme_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".md"):
                 readme_files.append(os.path.join(root, file))

    # Thay thế các thẻ trong tệp README.md
    for filename in readme_files:
        with open(filename, "r") as f:
            content = f.read()

        # Thay thế thẻ <VERSION> bằng giá trị từ readme.json
        content = re.sub(r"<VERSION>", version, content)

        with open(filename, "w") as f:
            f.write(content)

if __name__ == "__main__":
    replace_tags()
