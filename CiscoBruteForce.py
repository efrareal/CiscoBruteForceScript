from netmiko import ConnectHandler 
from threading import Thread
import sys
from termcolor import colored
import time

def SSHConnection(ip, user, password):
    try:
        session = ConnectHandler(device_type = 'cisco_ios', ip = ip, username = user, password = password)
        #Obtiene el hostname del equipo
        hostname = session.find_prompt()
        session.disconnect()
        print(colored('Conexion exitosa en IP %s con Hostname {}' % ip, 'green').format(hostname))
    except:
        print(colored('Some error in %s \n' % ip, 'red'))
        #sys.exit()  

def main():
    # IP ADDRESS HERE!
    ipaddr = "A.B.C.D"

    #PUT YOUR FILES HERE
    credentials = r'CREDENTIAL_FILE'

    with open(credentials, 'r') as file:
        credentials = file.readlines()
    
    #MULTITHREDING
    for credential in credentials:

        username = credential.split(',')[0].rstrip('\n')
        password = credential.split(',')[1].rstrip('\n')
        t = Thread(target = SSHConnection, args =(ipaddr, username, password))
        t.start()

main()
