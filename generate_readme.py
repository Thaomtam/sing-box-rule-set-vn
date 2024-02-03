# generate_readme.py

import os

def generate_readme(files):
    with open("README.md", "w") as readme_file:
        readme_file.write("# Sing-box Rule Set for VietNam\n")
        readme_file.write("This repository contains the sing-box rule set for Vietnam.\n\n")
        readme_file.write("## Rule Sets\n\n")
        for filepath in files:
            tag = os.path.splitext(os.path.basename(filepath))[0]
            readme_file.write(f"- **{tag} Rule Set:** [Download](/../../raw/rule-set/{tag}.srs)\n")
        readme_file.write("\n")
        readme_file.write("## Usage\n\n")
        readme_file.write("You can use these rule sets with the sing-box application.\n")

# Thêm dòng code này để kiểm tra xem tệp README.md đã tồn tại hay chưa
if not os.path.exists("README.md"):
    # Thêm dòng code này để lấy danh sách các tệp JSON đã được tạo
    files = ["./rule-set/block.json", "./rule-set/adway.json"]
    generate_readme(files)
