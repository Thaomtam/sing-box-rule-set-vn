import os
import requests
import json
import re
import subprocess

output_dir = "./rule-set"

def write_json_file(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def fetch_and_convert_url(url, convert_function, function_name):
    filename = function_name + ".json"
    filepath = os.path.join(output_dir, filename)
    response = requests.get(url)
    if response.ok:
        converted_data = convert_function(response.text)
        write_json_file(converted_data, filepath)
        return filepath
    else:
        print(f"Failed to fetch data from {url}. Status code: {response.status_code}")
        return None

# Các hàm convert_function được giữ nguyên

def main():
    os.makedirs(output_dir, exist_ok=True)

    # Lấy danh sách tên miền từ threat
    threat_url = "https://raw.githubusercontent.com/bigdargon/hostsVN/master/extensions/threat/filter.txt"
    threat_domain_list = extract_threat(threat_url)

    # Ghi danh sách tên miền từ threat vào file json
    threat_filepath = os.path.join(output_dir, "threat.json")
    write_json_file({"version": 1, "rules": [{"domain": threat_domain_list}]}, threat_filepath)

    url_convert_functions = [
        ("https://raw.githubusercontent.com/bigdargon/hostsVN/master/option/domain.txt", convert_block, "block"),
        ("https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt", convert_adway, "adway"),
        ("https://winhelp2002.mvps.org/hosts.txt", convert_MVPS, "MVPS"),
        ("https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt", convert_easylist, "easylist"),
        ("https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts", black, "black"),
        ("https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext&useip=0.0.0.0", yoyo, "yoyo")
    ]

    files = [threat_filepath]  # Đưa danh sách threat vào files

    for url, convert_function, function_name in url_convert_functions:
        filepath = fetch_and_convert_url(url, convert_function, function_name)
        if filepath:
            files.append(filepath)

    print("rule-set source generated:")
    for filepath in files:
        print(filepath)

    # Sử dụng subprocess để thực thi lệnh compile
    for filepath in files:
        srs_path = filepath.replace(".json", ".srs")
        subprocess.run(["sing-box", "rule-set", "compile", "--output", srs_path, filepath], check=True)

if __name__ == "__main__":
    main()
