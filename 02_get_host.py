import requests
from APIC_EM import get_ticket


def get_host_ips():
    url = "https://sandboxapicem.cisco.com/api/v1/host"
    ticket = get_ticket()

    host_ips = []
    if ticket:
        headers = {
            'X-Auth-Token': ticket,
            'Cache-Control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers, verify=False)

        if response.status_code is 200:
            json_data = response.json()

            for device in json_data["response"]:
                host_ips.append(device["hostIp"])
            return host_ips
        else:
            print("[*] Could not get host ips")


host_ips = get_host_ips()
print(host_ips)
