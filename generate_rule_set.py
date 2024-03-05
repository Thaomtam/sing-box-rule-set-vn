import os
import requests
import json
import re

output_dir = "./rule-set"
json_output_file = os.path.join(output_dir, "all_domains.json")

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

def merge_domains(*args):
    merged_domains = set()
    for domain_list in args:
        for domain in domain_list:
            merged_domains.add(domain)
    return list(merged_domains)

def extract_domains(data):
    domain_list = [re.findall(r"[\w\.-]+", line)[1] for line in data.splitlines() if line.strip() and not line.startswith("#")]
    return domain_list

def extract_threat(url):
    response = requests.get(url)
    if response.status_code == 200:
        return extract_domains(response.text)
    else:
        print("Failed to fetch threat file.")
        return []

def extract_casino(url):
    response = requests.get(url)
    if response.status_code == 200:
        return extract_domains(response.text)
    else:
        print("Failed to fetch casino file.")
        return []

def extract_adservers(url):
    response = requests.get(url)
    if response.status_code == 200:
        return extract_domains(response.text)
    else:
        print("Failed to fetch adservers file.")
        return []

def main():
    os.makedirs(output_dir, exist_ok=True)

    threat_url = "https://raw.githubusercontent.com/bigdargon/hostsVN/master/extensions/threat/filter.txt"
    casino_url = "https://raw.githubusercontent.com/bigdargon/hostsVN/master/extensions/gambling/filter.txt"
    adservers_url = "https://raw.githubusercontent.com/bigdargon/hostsVN/master/filters/adservers-all.txt"

    threat_domains = extract_threat(threat_url)
    casino_domains = extract_casino(casino_url)
    adservers_domains = extract_adservers(adservers_url)

    all_domains = merge_domains(threat_domains, casino_domains, adservers_domains)

    write_json_file({"version": 1, "rules": [{"domain": all_domains}]}, json_output_file)
    os.system(f"sing-box rule-set compile --output rule-set.srs {json_output_file}")

if __name__ == "__main__":
    main()
