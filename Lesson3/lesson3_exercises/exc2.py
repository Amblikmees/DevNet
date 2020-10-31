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
    print("Family " + device["family"] + " device with " + "hostname " + device["hostname"])
