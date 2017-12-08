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


ticket = get_ticket()
print("This is the ticket: " + ticket)

