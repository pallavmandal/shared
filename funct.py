def vlan_creation(num):
    num+=1
    for i in range (1,num):
        print(f"Vlan {i}")

num=eval(input ("How many VLANs do you want to be created"))

vlan_creation(num)

