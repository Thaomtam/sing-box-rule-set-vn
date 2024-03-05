import os
import requests
import json
import re

output_dir = "./rule-set"
output_filename = "thaomtam.json"  # Tên của tệp JSON kết quả

def write_json_file(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def merge_json_files(files):
    merged_data = {"version": 1, "rules": []}
    for filepath in files:
        with open(filepath, "r") as f:
            data = json.load(f)
            merged_data["rules"].extend(data["rules"])
    return merged_data

def fetch_and_convert_url(url, convert_function, function_name):
    filename = function_name + ".json"
    filepath = os.path.join(output_dir, filename)
    response = requests.get(url)
    if response.ok:
        converted_data = convert_function(response.text)
        write_json_file(converted_data, filepath)
        return filepath
    return None

def main():
    os.makedirs(output_dir, exist_ok=True)

    # Lấy danh sách các tệp JSON từ các nguồn khác nhau
    url_convert_functions = [
        ("https://raw.githubusercontent.com/bigdargon/hostsVN/master/option/domain.txt", convert_block, "block"),
        ("https://raw.githubusercontent.com/Spam404/lists/master/main-blacklist.txt", convert_spam404, "spam404"),
        ("https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt", convert_adway, "adway"),
        ("https://winhelp2002.mvps.org/hosts.txt", convert_MVPS, "MVPS"),
        ("https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt", convert_easylist, "easylist"),
        ("https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts", black, "black"),
        ("https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext&useip=0.0.0.0", yoyo, "yoyo"),
        ("https://hosts.anudeep.me/mirror/adservers.txt", anudeep, "anudeep"),
        ("https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Extension/GoodbyeAds-Xiaomi-Extension.txt", xiaomi, "xiaomi"),
        ("https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt", dan, "dan"),
        ("https://raw.githubusercontent.com/pantsufan/BlockAds/main/hosts", Kninja, "Kninja"),
        ("https://blocklistproject.github.io/Lists/redirect.txt", Redirect, "Redirect"),
        ("https://blocklistproject.github.io/Lists/facebook.txt", Facebook, "Facebook")
    ]

    files = [os.path.join(output_dir, "threat.json"), os.path.join(output_dir, "casino.json"), os.path.join(output_dir, "adservers.json")]

    for url, convert_function, function_name in url_convert_functions:
        filepath = fetch_and_convert_url(url, convert_function, function_name)
        if filepath:
            files.append(filepath)

    # Gộp tất cả các tệp JSON thành một tệp duy nhất
    merged_data = merge_json_files(files)

    # Ghi tệp JSON kết quả
    result_filepath = os.path.join(output_dir, output_filename)
    write_json_file(merged_data, result_filepath)
    print(f"Combined JSON file: {result_filepath}")

if __name__ == "__main__":
    main()
