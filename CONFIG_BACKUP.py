from netmiko import ConnectHandler
from getpass import getpass

username=input("Username: ")
password=getpass()
command="sh run"
ip_list=open('Device_list.txt','r')
count = 0
for ip in ip_list:
    sw = {
    'device_type': 'cisco_ios',
    'host': ip,
    'username': username,
    'password': password,
    
    }
    net_connect=ConnectHandler(**sw)
    output=net_connect.send_command(command)
    filename=ip[:-1]+".txt"
    file = open(filename,'w')
    file.write(f"Running config for {ip}")
    file.write(output+"\n")
    file.close()
    count+=1
print(f"The running config of the {count} network devices have been exported")
