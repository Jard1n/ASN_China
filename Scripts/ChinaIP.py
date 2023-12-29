import requests

ChinaIP = "https://raw.githubusercontent.com/pmkol/easymosdns/rules/china_ip_list.txt"
r = requests.get(ChinaIP)

original_content = r.text.split('\n')
ip_cidr_content_all = []
ip_cidr_content_v4 = []
ip_cidr_content_v6 = []

for ip in original_content:
    if ip.strip() and '.' in ip:
        ip_cidr_v4 = "IP-CIDR," + ip.strip()
        ip_cidr_content_all.append(ip_cidr_v4)
        ip_cidr_content_v4.append(ip_cidr_v4)
    elif ip.strip() and ':' in ip:
        ip_cidr_v6 = "IP-CIDR6," + ip.strip()
        ip_cidr_content_all.append(ip_cidr_v6)
        ip_cidr_content_v6.append(ip_cidr_v6)

with open("IP.China.list", "w") as cidr_file_all:
    for line in ip_cidr_content_all:
        cidr_file_all.write(line + '\n')

with open("IPv4.China.list", "w") as cidr_file_v4:
    for line in ip_cidr_content_v4:
        cidr_file_v4.write(line + '\n')

with open("IPv6.China.list", "w") as cidr_file_v6:
    for line in ip_cidr_content_v6:
        cidr_file_v6.write(line + '\n')
