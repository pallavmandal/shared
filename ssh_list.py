from netmiko import ConnectHandler
from getpass import getpass
password=getpass()
command="sh ip int br"
ip_list=open('Device_list.txt')
for ip in ip_list:
    sw = {
    'device_type': 'cisco_ios',
    'host': ip,
    'username': 'admin-pkma',
    'password': password,
    
    }
    print (f"Details for {ip}")
    net_connect=ConnectHandler(**sw)
    output=net_connect.send_command(command)
    print(output+"\n")






