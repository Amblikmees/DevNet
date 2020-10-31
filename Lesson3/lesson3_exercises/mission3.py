from ncclient import manager
import json
import xmltodict
import netconf_functions


def get_interfaces():
    interfaces = netconf_functions.get_interfaces()
    data = xmltodict.parse(interfaces)
    data_dict = json.loads(json.dumps(data))
    interfaces = data_dict["data"]["native"]["interface"]["GigabitEthernet"]
    return interfaces


def change_interface_vlan(interface, vlan):
    netconf_functions.change_interface_vlan(interface, vlan)


def read_file():
    file = "mission_response.json"
    my_file = open(file, mode="r")
    info = my_file.read()
    return info


def parsing_json(info):
    data = json.loads(info)
    data = data["response"]
    new_list = []
    for i in data:
        new_list.append({"name": i["portName"], "vlan": i["vlanId"], "status": i["status"]})
    return new_list


def show_interface(interfaces):
    i = 1
    for item in interfaces:
        try:
            vlan = item["switchport"]["access"]["vlan"]["vlan"]
        except KeyError:
            vlan = None
        print(str(i) + ". The interface " + item["name"] + " has VLAN " + str(vlan) + ".")
        i = i + 1


def ask_which_interface(new_list):
    user_input = int(input("Which interface you would like to work with? "))
    interface = new_list[user_input - 1]
    print("Got it, configuring interface " + interface["name"] + "!")
    return interface


def main():
    while True:
        new_list = get_interfaces()
        show_interface(new_list)
        interface = ask_which_interface(new_list)
        user_choice = input("Which VLAN would you like to have? ")
        try:
            select = int(user_choice)
            change_interface_vlan(interface["name"], select)
            print("Vlan has been changed!")
        except ValueError:
            print("You need to select a number!!!!!")
            continue

        selection = input("Do you want to continue changing VLANs? (yes/no)")
        if selection == "yes":
            continue
        else:
            print("Thank you for using the application!")
            break


if __name__ == "__main__":
    main()
