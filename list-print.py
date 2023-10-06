def create_interfaces_list(count):
    for i in range (count):
        interface_list.append("Interface f0/" + str(i))

def list_interfaces_print():
    for i in interface_list:
        print(i)

def main(count):
    create_interfaces_list(count)
    list_interfaces_print()

interface_list=[]
count=eval(input("How many interfaces do you want to be created"))
main(count)