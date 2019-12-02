import subprocess
# subprocess module is to process things using your terminal
import optparse
# optparse module is to add options to your command
import re
# re module is to process regex code
import random

#Adding options to your script
def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i","--interface", dest = "interface", help = "Interface of the MAC Address you want to change")
    parser.add_option("-m","--mac", dest ="new_mac", help="New MAC Address (should be in format 'xx:xx:xx:xx:xx:xx')")
    parser.add_option("-r","--random", action = "get_current_mac()", help="gp")
    (options,result) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify the interface you want to change, use --help for more information.")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac address, use --help for more information")
    return options

#Changing the MAC Address
def change_macadd(interface,new_mac):
    print("[-] Changing MAC Address of " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_result:
        return mac_result.group(0)
    else:
        print("[-] Could not read MAC Address")

def random_mac_gen():
    r_mac ="00"
    for r in range(9):
        value = random.randrange(1,8,1)
        if(r%2==0):
            r_mac = r_mac + ":"
        if (r%3!=0):
            r_mac = r_mac+ str(value)
        else:
            lists = ["a","b","c","d","e","f","a","b","d","e"]
            value_a = lists[r]
            r_mac = r_mac+value_a
    print(r_mac)
    r_mac = str(r_mac)+"b"
    print(r_mac)

    
    



options = get_argument()
current_mac = get_current_mac(options.interface)
print("Current Mac is " + str(current_mac))
get_current_mac(options.interface)
#change_macadd(options.interface, options.new_mac)
random_mac_gen()


