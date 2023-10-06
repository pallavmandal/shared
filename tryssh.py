from netmiko import ConnectHandler
from getpass import getpass

hyd_sw02 = {
    'device_type': 'cisco_ios',
    'host': '10.61.20.4',
    'username': 'admin-pkma',
    'password': getpass(),
    
}

command="sh ip int br"
net_connect=ConnectHandler(**hyd_sw02)
output=net_connect.send_command(command)
print(output)