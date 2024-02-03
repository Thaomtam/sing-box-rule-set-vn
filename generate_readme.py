import os
import requests
from urllib.parse import urljoin

def generate_readme(files):
    with open("README.md", "w") as readme_file:
        readme_file.write("# Sing-box Rule Set for VietNam\n")
        readme_file.write("This repository contains the sing-box rule set for Vietnam.\n\n")
        readme_file.write("## Rule Sets\n\n")
        for filename in files:
            tag = os.path.splitext(os.path.basename(filename))[0]
            readme_file.write(f"- **{tag} Rule Set:** [Download](/../../raw/rule-set/{tag}.srs)\n")
        readme_file.write("\n")
        readme_file.write("## Usage\n\n")
        readme_file.write("You can use these rule sets with the sing-box application.\n")

# Kiểm tra xem README.md đã tồn tại hay chưa
if not os.path.exists("README.md"):
    # Lấy danh sách các tệp JSON từ thư mục "rule-set" trên GitHub
    repo_name = "Thaomtam/sing-box-rule-set-vn"
    api_url = f"https://api.github.com/repos/{repo_name}/contents/rule-set"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(api_url, headers=headers)
    
    if response.ok:
        files = [content["name"] for content in response.json() if content["name"].endswith(".json")]
        generate_readme(files)
    else:
        print("Failed to retrieve file list from GitHub API.")
