import os
import requests
import json

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

def convert_to_json(domain_list):
    return {"version": 1, "rules": [{"domain": domain_list, "domain_keyword": [], "domain_suffix": []}]}

def main():
    os.makedirs(output_dir, exist_ok=True)

    url_convert_functions = [
        ("https://raw.githubusercontent.com/bigdargon/hostsVN/master/option/domain.txt", lambda data: convert_to_json([line.strip() for line in data.splitlines() if line and not line.startswith("#")]), "block"),
        ("https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt", lambda data: convert_to_json([line.split()[1] for line in data.splitlines() if line and not line.startswith("#")]), "adway"),
        ("https://raw.githubusercontent.com/StevenBlack/hosts/master/data/StevenBlack/hosts", lambda data: convert_to_json([line.split()[1] for line in data.splitlines() if line and not line.startswith("#")]), "stevenblack"),
        ("https://winhelp2002.mvps.org/hosts.txt", lambda data: convert_to_json([line.strip() for line in data.splitlines() if line and not line.startswith("#")]), "MVPS")
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
