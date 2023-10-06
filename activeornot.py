from netmiko import ConnectHandler
from getpass import getpass
password=getpass()
command="sh lldp neigh"

sw1 = {
'device_type': 'cisco_ios',
'host': '10.61.20.3',
'username': 'admin-pkma',
'password': password,
}

sw2 = {
'device_type': 'cisco_ios',
'host': '10.61.20.4',
'username': 'admin-pkma',
'password': password,
}

net_connect=ConnectHandler(**sw1)
output1=net_connect.send_command(command)

net_connect=ConnectHandler(**sw2)
output2=net_connect.send_command(command)

neighbour1=output1.find("Fortinet-GDC-HYD")
neighbour2=output2.find("Fortinet-GDC-HYD")
if neighbour1!=-1:
    print("CoreSwitch1 (10.61.20.3) is currently working in active mode and CoreSwitch2 (10.61.20.4) is in passive mode")
elif neighbour2!=-1:
    print("CoreSwitch2 (10.61.20.4) is currently working in active mode and CoreSwitch1 (10.61.20.3) is in passive mode")

