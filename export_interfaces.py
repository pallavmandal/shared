
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
    net_connect=ConnectHandler(**sw)
    output=net_connect.send_command(command)
    interface_list=open('interface_list.txt','a')
    interface_list.write("----------------------------------------------------------------\n")
    interface_list.write(f"Details of {ip}")
    interface_list.write("----------------------------------------------------------------\n")
    interface_list.write(output+"\n")
    interface_list.close()





