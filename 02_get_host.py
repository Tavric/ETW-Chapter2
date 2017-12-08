import requests
from APIC_EM import get_ticket
from tabulate import tabulate


def get_hosts():
    url = "https://sandboxapicem.cisco.com/api/v1/host"
    ticket = get_ticket()

    hosts = []
    if ticket:
        headers = {
            'X-Auth-Token': ticket,
            'Cache-Control': "no-cache"
            }

        response = requests.request("GET", url, headers=headers, verify=False)

        if response.status_code is 200:
            json_data = response.json()
            i = 0

            for device in json_data["response"]:
                i += 1
                hosts.append([i, device["hostType"], device["hostIp"]])
            return hosts
        else:
            print("[*] Could not get host ips")


hosts = get_hosts()
print (tabulate(hosts,headers=['Number','Type','IP'],tablefmt='rst'))
