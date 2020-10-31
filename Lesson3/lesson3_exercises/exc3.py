import requests
from requests.auth import HTTPBasicAuth

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

address = "https://sandboxdnac.cisco.com"
user = "devnetuser"
password = "Cisco123!"

url = "{}/dna/system/api/v1/auth/token".format(address)
header = {"content-type": "application/json"}

response = requests.post(url, auth=HTTPBasicAuth(username=user, password=password), headers=header, verify=False)

dict_response = response.json()
token = dict_response["Token"]

url2 = "{}/dna/intent/api/v1/network-device".format(address)
header2 = {"content-type": "application/json", "X-Auth-Token": token}

devices_response = requests.get(url2, headers=header2, verify=False)

devices = devices_response.json()

for device in devices["response"]:
    url3 = "{}/dna/intent/api/v1/device-detail".format(address)
    params = {"identifier": "uuid", "searchBy": device["id"]}
    device_response2 = requests.get(url3, headers=header2, params=params, verify=False)
    device_info = device_response2.json()
    device_info = device_info["response"]
    print(device["hostname"] + " has following health scores:")
    print("Overall health: " + str(device_info["overallHealth"]))
    print("Memory health: " + str(device_info["memoryScore"]))
    print("CPU health: " + str(device_info["cpuScore"]) + "\n")


