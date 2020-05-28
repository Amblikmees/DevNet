interface = "GigabitEthernet1/0/1"
status = "up"
VLAN = 30

print(f"The interface {interface} has status {status} and VLAN {VLAN}.")



while True:
    user_choice = int(input("Select 1 to change status and 2 to change VLAN: "))
    if user_choice == 1:
        if status == "up":
            status = "down"
            break
        elif status == "down":
            status = "up"
            break
    if user_choice == 2:
        VLAN = int(input("Which VLAN would you like to have? "))
        break
    print("This is an invalid selection.")


print(f"Now the interface {interface} has status {status} and VLAN {VLAN}.")
print("Thank you for using the application!")