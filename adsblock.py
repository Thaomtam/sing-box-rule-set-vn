import os
import requests
import json

output_dir = "./rule-set"

def fetch_domains_from_urls(urls):
    unique_domains = set()

    for url in urls:
        response = requests.get(url)
        if response.ok:
            data = response.json()
            if "rules" in data:
                for rule in data["rules"]:
                    if "domain" in rule:
                        unique_domains.update(rule["domain"])

    return list(unique_domains)

def write_json_file(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def main():
    os.makedirs(output_dir, exist_ok=True)  # Tạo thư mục nếu không tồn tại

    # Danh sách các URL chứa các tệp JSON
    urls = [
        "https://raw.githubusercontent.com/Thaomtam/sing-box-rule-set-vn/rule-set/block.json",
        "https://raw.githubusercontent.com/Thaomtam/sing-box-rule-set-vn/rule-set/adway.json"
    ]

    # Thu thập tất cả các tên miền duy nhất từ các tệp JSON
    unique_domains = fetch_domains_from_urls(urls)

    # Tạo cấu trúc JSON mới với danh sách tên miền duy nhất
    new_json_data = {"version": 1, "rules": [{"domain": unique_domains}]}

    # Ghi vào tệp JSON mới trong thư mục output_dir
    output_json_filepath = os.path.join(output_dir, "combined_domains.json")
    write_json_file(new_json_data, output_json_filepath)

    # Sử dụng tập lệnh Python để biên dịch tệp JSON mới thành tệp .srs
    output_srs_filepath = os.path.join(output_dir, "combined_domains.srs")
    os.system(f"sing-box rule-set compile --output {output_srs_filepath} {output_json_filepath}")

if __name__ == "__main__":
    main()
