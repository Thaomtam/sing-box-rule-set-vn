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

def convert_to_json_and_srs(url, convert_function, function_name):
    data = fetch_and_convert_url(url, convert_function, function_name)
    if data:
        json_data = {"version": 1, "rules": [{"domain": data}]}
        write_json_file(json_data, json_output_file)
        srs_output_file = json_output_file.replace(".json", ".srs")
        os.system(f"sing-box rule-set compile --output {srs_output_file} {json_output_file}")

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

def extract_adaway(url):
    response = requests.get(url)
    if response.status_code == 200:
        domain_list = [line.split()[1].split("#")[0] for line in response.text.splitlines() if line.strip() and not line.startswith("#") and "localhost" not in line]
        return domain_list
    else:
        print("Failed to fetch AdAway file.")
        return []

def extract_MVPS(url):
    response = requests.get(url)
    if response.status_code == 200:
        domain_list = []
        start_conversion = False
        for line in response.text.splitlines():
            line = line.strip()
            if line.startswith("# [Start of entries generated by MVPS HOSTS]"):
                start_conversion = True
                continue
            if start_conversion and line and not line.startswith("#") and "localhost" not in line:
                parts = line.split()
                if len(parts) >= 2 and parts[0] in ["0.0.0.0", "127.0.0.1", "::1"]:
                    domain_list.append(parts[1].split("#")[0])
        return domain_list
    else:
        print("Failed to fetch MVPS file.")
        return []

def extract_easylist(url):
    response = requests.get(url)
    if response.status_code == 200:
        domain_list = []
        for line in response.text.splitlines():
            line = line.strip()
            if line and not line.startswith("!") and "github.com" not in line:
                parts = line.split("||")
                if len(parts) >= 2:
                    domain_list.append(parts[1].split("^")[0])
        return domain_list
    else:
        print("Failed to fetch EasyList file.")
        return []

def extract_yoyo(url):
    response = requests.get(url)
    if response.status_code == 200:
        domain_list = [re.findall(r"[\w\.-]+", line)[1] for line in response.text.splitlines() if line.strip() and not line.startswith("#")]
        # Loại bỏ các tên miền không mong muốn
        unwanted_domains = {"localhost", "broadcasthost", "local", "ip6-localhost", "ip6-loopback", "0.0.0.0", "localhost.localdomain", "1", "0", "2", "3"}
        domain_list = [domain for domain in domain_list if domain not in unwanted_domains]
        return domain_list
    else:
        print("Failed to fetch Yoyo file.")
        return []

def extract_anudeep(url):
    response = requests.get(url)
    if response.status_code == 200:
        domain_list = [re.findall(r"[\w\.-]+", line)[1] for line in response.text.splitlines() if line.strip() and not line.startswith("#")]
        # Loại bỏ các tên miền không mong muốn
        unwanted_domains = {"localhost", "broadcasthost", "local", "ip6-localhost", "ip6-loopback", "0.0.0.0", "localhost.localdomain", "1", "0", "2", "3"}
        domain_list = [domain for domain in domain_list if domain not in unwanted_domains]
        return domain_list
    else:
        print("Failed to fetch Anudeep file.")
        return []

def extract_xiaomi(url):
    response = requests.get(url)
    if response.status_code == 200:
        domain_list = [re.findall(r"[\w\.-]+", line)[1] for line in response.text.splitlines() if line.strip() and not line.startswith("#")]
        # Loại bỏ các tên miền không mong muốn
        unwanted_domains = {"localhost", "broadcasthost", "local", "ip6-localhost", "ip6-loopback", "0.0.0.0", "localhost.localdomain", "1", "0", "2", "3"}
        domain_list = [domain for domain in domain_list if domain not in unwanted_domains]
        return domain_list
    else:
        print("Failed to fetch Xiaomi file.")
        return []

def extract_dan(url):
    response = requests.get(url)
    if response.status_code == 200:
        domain_list = [re.findall(r"[\w\.-]+", line)[1] for line in response.text.splitlines() if line.strip() and not line.startswith("#")]
        # Loại bỏ các tên miền không mong muốn
        unwanted_domains = {"localhost", "broadcasthost", "local", "ip6-localhost", "ip6-loopback", "0.0.0.0", "localhost.localdomain", "1", "0", "2", "3"}
        domain_list = [domain for domain in domain_list if domain not in unwanted_domains]
        return domain_list
    else:
        print("Failed to fetch Dan file.")
        return []

def extract_Kninja(url):
    response = requests.get(url)
    if response.status_code == 200:
        domain_list = [re.findall(r"[\w\.-]+", line)[1] for line in response.text.splitlines() if line.strip() and not line.startswith("#")]
        # Loại bỏ các tên miền không mong muốn
        unwanted_domains = {"127.0.0.1", "255.255.255.255", "::1", "fe00::0", "ff02::1", "ff02::2", "ff02::3", "localhost", "broadcasthost", "local", "ip6-localhost", "ip6-loopback", "0.0.0.0", "localhost.localdomain", "1", "0", "2", "3"}
        domain_list = [domain for domain in domain_list if domain not in unwanted_domains]
        return domain_list
    else:
        print("Failed to fetch Kninja file.")
        return []

def extract_Redirect(url):
    response = requests.get(url)
    if response.status_code == 200:
        domain_list = [re.findall(r"[\w\.-]+", line)[1] for line in response.text.splitlines() if line.strip() and not line.startswith("#")]
        # Loại bỏ các tên miền không mong muốn
        unwanted_domains = {"127.0.0.1", "255.255.255.255", "::1", "fe00::0", "ff02::1", "ff02::2", "ff02::3", "localhost", "broadcasthost", "local", "ip6-localhost", "ip6-loopback", "0.0.0.0", "localhost.localdomain", "1", "0", "2", "3"}
        domain_list = [domain for domain in domain_list if domain not in unwanted_domains]
        return domain_list
    else:
        print("Failed to fetch Redirect file.")
        return []

def extract_Facebook(url):
    response = requests.get(url)
    if response.status_code == 200:
        domain_list = [re.findall(r"[\w\.-]+", line)[1] for line in response.text.splitlines() if line.strip() and not line.startswith("#")]
        # Loại bỏ các tên miền không mong muốn
        unwanted_domains = {"127.0.0.1", "255.255.255.255", "::1", "fe00::0", "ff02::1", "ff02::2", "ff02::3", "localhost", "broadcasthost", "local", "ip6-localhost", "ip6-loopback", "0.0.0.0", "localhost.localdomain", "1", "0", "2", "3"}
        domain_list = [domain for domain in domain_list if domain not in unwanted_domains]
        return domain_list
    else:
        print("Failed to fetch Facebook file.")
        return []

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

    threat_domains = extract_threat(threat_url)
    casino_domains = extract_casino(casino_url)
    adservers_domains = extract_adservers(adservers_url)
    adaway_domains = extract_adaway(adaway_url)
    MVPS_domains = extract_MVPS(MVPS_url)
    easylist_domains = extract_easylist(easylist_url)
    yoyo_domains = extract_yoyo(yoyo_url)
    anudeep_domains = extract_anudeep(anudeep_url)
    xiaomi_domains = extract_xiaomi(xiaomi_url)
    dan_domains = extract_dan(dan_url)
    Kninja_domains = extract_Kninja(Kninja_url)
    Redirect_domains = extract_Redirect(Redirect_url)
    Facebook_domains = extract_Facebook(Facebook_url)

    all_domains = merge_domains(threat_domains, casino_domains, adservers_domains, adaway_domains, MVPS_domains, easylist_domains, yoyo_domains, anudeep_domains, xiaomi_domains, dan_domains, Kninja_domains, Redirect_domains, Facebook_domains)
    
    write_json_file({"version": 1, "rules": [{"domain": all_domains}]}, json_output_file)
    os.system(f"sing-box rule-set compile --output rule-set.srs {json_output_file}")

if __name__ == "__main__":
    main()
