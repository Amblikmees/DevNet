from netmiko import ConnectHandler
from credentials import *


CSR1000 = {
    'device_type': 'cisco_xe',
    'host':   'ios-xe-mgmt-latest.cisco.com',
    'username': username1,
    'password': password1,
    'port' : 8181,          # optional, defaults to 22
    'secret': 'C1sco12345',     # optional, defaults to ''
}

net_connect = ConnectHandler(**CSR1000)

output = net_connect.send_command('show ip int brief')
print(output)