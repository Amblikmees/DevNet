import json


def read_file():
    file = "mission_response.json"
    my_file = open(file, mode="r")
    info = my_file.read()
    return info


def parsing_json():
    info = read_file()
    data = json.loads(info)
    data = data["response"]
    new_list = []
    for i in data:
        new_list.append({"name": i["portName"], "vlan": i["vlanId"], "status": i["status"]})
    return new_list


def show_interface():
    new_list = parsing_json()
    i = 0
    for device in new_list:
        i = i + 1
        print(str(i) + ":" + " The interface " + device["name"] + " has status " + device["status"]
              + " and VLAN " + str(device["vlan"]))


def ask_which_interface():
    devices_list = parsing_json()
    user_input = int(input("Which interface you would like to work with? "))
    interface = devices_list[user_input - 1]
    print("Got it, configuring interface " + interface["name"] + "!")
    return interface


def ask_what_to_do():
    interface = ask_which_interface()
    while True:
        user_choice = int(input("Select 1 to change status and 2 to change VLAN: "))
        if user_choice == 1:
            if interface["status"] == "up":
                interface["status"] = "down"
                break
            else:
                interface["status"] = "up"
                break
        if user_choice == 2:
            try:
                interface["vlan"] = int(input("Which VLAN would you like to have? "))
            except ValueError:
                print("you must enter an integer")
                continue
            break

    print("Now the interface " + interface["name"] + " has status " + interface["status"]
          + " and VLAN " + str(interface["vlan"]))
    print("Thank you for using the application!")


def main():
    show_interface()
    ask_what_to_do()


main()
