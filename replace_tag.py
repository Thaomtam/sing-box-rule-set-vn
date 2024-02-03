import re
import os
import json

# Đường dẫn đến tệp README.md
README_FILE = "README.md"

# Đường dẫn đến tệp readme.json
README_JSON_FILE = "readme.json"

def replace_tags():
    # Đọc nội dung từ tệp README.md
    with open(README_FILE, "r") as f:
        content = f.read()
    
    # Đọc các biến từ tệp readme.json
    with open(README_JSON_FILE, "r") as f:
        variables = json.load(f)

    # Thực hiện thay thế các thẻ <>
    for key, value in variables.items():
        tag = f"<variable-{key}-tag>"
        content = content.replace(tag, f"`{value}`")

    # Ghi nội dung đã được thay thế vào tệp README.md
    with open(README_FILE, "w") as f:
        f.write(content)

if __name__ == "__main__":
    replace_tags()
