import json, xmltodict

file = "mission_response.xml"
my_file = open(file, mode="r")
content = my_file.read()

data = json.loads(json.dumps(xmltodict.parse(content)))

data2 = data["rpc-reply"]["data"]["native"]["interface"]["GigabitEthernet"]

for names in data2:
    print(names["name"])


