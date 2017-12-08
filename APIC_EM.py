import requests


def get_ticket():
    print("[*] Getting ticket")
    url = "https://sandboxapicem.cisco.com/api/v1/ticket"

    payload = "{\n\t\"password\": \"Cisco123!\",\n\t\"username\": \"devnetuser\"\n}"
    headers = {
        'Content-Type': "application/json"
        }

    response = requests.request("POST", url, data=payload, headers=headers, verify=False)

    status = response.status_code

    json_data = response.json()

    ticket = json_data["response"]["serviceTicket"]

    if status == 200:
        return ticket
    else:
        print("[*] Unable to get ticket")


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