import os
import requests
import json
import re

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
    return None

def convert_block(data):
    domain_list = [line.strip() for line in data.splitlines() if line.strip() and not line.startswith("#")]
    return {"version": 1, "rules": [{"domain": domain_list}]}

def convert_adway(data):
    domain_list = [line.split()[1].split("#")[0] for line in data.splitlines() if line.strip() and not line.startswith("#") and "localhost" not in line]
    return {"version": 1, "rules": [{"domain": domain_list}]}

def convert_MVPS(data):
    domain_list = []
    start_conversion = False
    for line in data.splitlines():
        line = line.strip()
        if line.startswith("# [Start of entries generated by MVPS HOSTS]"):
            start_conversion = True
            continue
        if start_conversion and line and not line.startswith("#") and "localhost" not in line:
            parts = line.split()
            if len(parts) >= 2 and parts[0] in ["0.0.0.0", "127.0.0.1", "::1"]:
                domain_list.append(parts[1].split("#")[0])
    return {"version": 1, "rules": [{"domain": domain_list}]}

def convert_easylist(data):
    domain_list = []
    for line in data.splitlines():
        line = line.strip()
        if line and not line.startswith("!") and "github.com" not in line:
            parts = line.split("||")
            if len(parts) >= 2:
                domain_list.append(parts[1].split("^")[0])
    return {"version": 1, "rules": [{"domain": domain_list}]}

def black(data):
    domain_list = [re.findall(r"[\w\.-]+", line)[1] for line in data.splitlines() if line.strip() and not line.startswith("#")]
    # Loại bỏ các tên miền không mong muốn
    domain_list = [domain for domain in domain_list if not domain.startswith(("localhost", "broadcasthost", "local", "ip"))]
    return {"version": 1, "rules": [{"domain": domain_list}]}

def yoyo(data):
    domain_list = [re.findall(r"[\w\.-]+", line)[1] for line in data.splitlines() if line.strip() and not line.startswith("#") and not line.startswith("0.0.0.0")]
    return {"version": 1, "rules": [{"domain": domain_list}]}

def main():
    os.makedirs(output_dir, exist_ok=True)

    url_convert_functions = [
        ("https://raw.githubusercontent.com/bigdargon/hostsVN/master/option/domain.txt", convert_block, "block"),
        ("https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt", convert_adway, "adway"),
        ("https://winhelp2002.mvps.org/hosts.txt", convert_MVPS, "MVPS"),
        ("https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt", convert_easylist, "easylist"),
        ("https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts", black, "black"),
        ("https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext&useip=0.0.0.0", yoyo, "yoyo")
    ]

    files = []
    for url, convert_function, function_name in url_convert_functions:
        filepath = fetch_and_convert_url(url, convert_function, function_name)
        if filepath:
            files.append(filepath)

    print("rule-set source generated:")
    for filepath in files:
        print(filepath)

    for filepath in files:
        srs_path = filepath.replace(".json", ".srs")
        os.system(f"sing-box rule-set compile --output {srs_path} {filepath}")

if __name__ == "__main__":
    main()
