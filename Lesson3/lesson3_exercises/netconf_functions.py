from ncclient import manager
import credentials


filter = """
<filter>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> <interface>
<GigabitEthernet>
<name/>
<switchport>
<access xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-switch" />
</switchport>
</GigabitEthernet>
</interface>
</native>
</filter>
"""

config = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<interface>
<GigabitEthernet>
<name>{interface}</name>
<switchport>
<access xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-switch">
<vlan><vlan>{vlan}</vlan></vlan>
</access>
</switchport>
<description> Configured by NETCONF </description>
</GigabitEthernet>
</interface>
</native>
</config>
"""


def get_interfaces():
    with manager.connect(host=credentials.address, port=credentials.port, username=credentials.user, password=credentials.password, hostkey_verify=False) as m:
        return m.get_config(filter=filter, source="running").data_xml


def change_interface_vlan(interface, vlan):
    changed_config = config.format(interface=interface, vlan=vlan)
    with manager.connect(host=credentials.address, port=credentials.port, username=credentials.user, password=credentials.password, hostkey_verify=False) as m:
        return m.edit_config(changed_config, target="running")