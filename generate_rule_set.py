import os
import requests
import json
import re

output_dir = "./rule-set"
json_output_file = "rule-set.json"

def write_json_file(data, filepath):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def fetch_and_convert_url(url, convert_function, function_name):
    response = requests.get(url)
    if response.ok:
        converted_data = convert_function(response.text)
        return converted_data
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

def extract_sources_and_merge(urls):
    all_domains = []
    for url in urls:
        domain_list = fetch_and_convert_url(url, extract_domains, "")
        if domain_list:
            all_domains.extend(domain_list)
    return all_domains

def main():
    os.makedirs(output_dir, exist_ok=True)

    threat_url = "https://raw.githubusercontent.com/bigdargon/hostsVN/master/extensions/threat/filter.txt"
    casino_url = "https://raw.githubusercontent.com/bigdargon/hostsVN/master/extensions/gambling/filter.txt"
    adservers_url = "https://raw.githubusercontent.com/bigdargon/hostsVN/master/filters/adservers-all.txt"
    adaway_url = "https://raw.githubusercontent.com/AdAway/adaway.github.io/master/hosts.txt"
    MVPS_url = "https://winhelp2002.mvps.org/hosts.txt"
    easylist_url = "https://raw.githubusercontent.com/easylist/easylist/master/easylist/easylist_adservers.txt"
    yoyo_url = "https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext&useip=0.0.0.0"
    anudeep_url = "https://hosts.anudeep.me/mirror/adservers.txt"
    xiaomi_url = "https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Extension/GoodbyeAds-Xiaomi-Extension.txt"
    dan_url = "https://www.github.developerdan.com/hosts/lists/ads-and-tracking-extended.txt"
    Kninja_url = "https://raw.githubusercontent.com/pantsufan/BlockAds/main/hosts"
    Redirect_url = "https://blocklistproject.github.io/Lists/redirect.txt"
    Facebook_url = "https://blocklistproject.github.io/Lists/facebook.txt"

    urls = [threat_url, casino_url, adservers_url, adaway_url, MVPS_url, easylist_url, yoyo_url, anudeep_url, xiaomi_url, dan_url, Kninja_url, Redirect_url, Facebook_url]
    all_domains = extract_sources_and_merge(urls)
    
    write_json_file({"version": 1, "rules": [{"domain": all_domains}]}, json_output_file)
    os.system(f"sing-box rule-set compile --output rule-set.srs {json_output_file}")

if __name__ == "__main__":
    main()
