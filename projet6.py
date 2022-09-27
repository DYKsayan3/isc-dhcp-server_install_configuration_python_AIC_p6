#!/usr/bin/env python3
import apt
import os
import json


x=open('projet6.json') #ouverture du fichier json

projet6 = json.load(x) #chargement


#Fonction vérification presence service isc-dhcp-

def verification():
    isc = 'isc-dhcp-server'
    cache = apt.Cache()
    isc_installe = False

    if isc in cache:
        isc_installe = cache[isc].is_installed
    if isc_installe == True:
        print("##############################")
        print("#isc-dhcp-server est installé#")
        print("############################## \n")
    else:
        print("####################################")
        print("#isc-dhcp-server n'est pas installé#")
        print("#################################### \n")
    return isc_installe

#Fonction installation server dhcp
def installation():
    install = "sudo apt-get install -y isc-dhcp-server"
    os.system(install)

    #Fonction de désinstallation isc-dhcp-server
def desinstallation():
    remove = "sudo apt-get autoremove -y --purge isc-dhcp-server"
    os.system(remove)
 #Fonction configuration du fichier etc/default/isc-dhcp-server

def configfile1():
   
    interfacename = projet6["interface"]
    config= " sed -i '17 s/\"\"/\"{}\"/' /etc/default/isc-dhcp-server ".format(interfacename)
    os.system(config)

#configfile1()     

#fonction qui permet de decommenter la ligne 24

def configfile2():
    config= " sed -i '24 s/#authoritative/authoritative/' /etc/dhcp/dhcpd.conf "
    os.system(config)

#configfile2()    
    
#fonction qui permet configurer le subnet et le netmask 

def configfile3():
    subnetname = projet6["subnet"]
    netmaskname = projet6["netmask"]
    config= " sed -i '53 s/#subnet 10.5.5.0 netmask 255.255.255.224/subnet {} netmask {} /' /etc/dhcp/dhcpd.conf ".format(subnetname,netmaskname)
    os.system(config) 

#configfile3() 

#fonction qui permet de configurer le range 

def configfile4():
    rangename = projet6["range"]
    config= " sed -i '54 s/#  range 10.5.5.26 10.5.5.30/range {} /' /etc/dhcp/dhcpd.conf ".format(rangename)
    os.system(config) 

#configfile4() 

#fonction qui permet de configurer de configuer l'option dns

def configfile5():
    optdns = projet6["option domain-name-servers"]
    config= " sed -i '55 s/#  option domain-name-servers ns1.internal.example.org/option domain-name-servers {} /' /etc/dhcp/dhcpd.conf ".format(optdns)
    os.system(config) 
 
#configfile5() 

#fonction qui permet de configurer l'adresse de diffusion 

def configfile6():
    optbc = projet6["option broadcast-address"]
    config= " sed -i '59 s/#  option broadcast-address 10.5.5.31/option broadcast-address {} /' /etc/dhcp/dhcpd.conf ".format(optbc)
    os.system(config) 

#configfile6()

#fonction qui permet de configurer l'adresse du routeur 

def configfile7():
    optrt = projet6["option routers"]
    config= " sed -i '58 s/#  option routers 10.5.5.1/option routers {} /' /etc/dhcp/dhcpd.conf ".format(optrt)
    os.system(config) 

#configfile7()  

#fonction qui permet de decommenter la ligne de 60 

def configfile8():
    config= " sed -i '60 s/#  default-lease-time 600/default-lease-time 600/' /etc/dhcp/dhcpd.conf "
    os.system(config)

#configfile8()

#fonction qui permet de decommenter la ligne 61

def configfile9():
    config= " sed -i '61 s/#  max-lease-time 7200/max-lease-time 7200/' /etc/dhcp/dhcpd.conf "
    os.system(config)

#configfile9()  

#fonction qui permet de decommenter la ligne 62

def configfile10():
    config= " sed -i '62 s/#//' /etc/dhcp/dhcpd.conf "
    os.system(config)

#configfile10()  

def restartservice():
    restart = "systemctl restart isc-dhcp-server"
    status = "systemctl status isc-dhcp-server"
    os.system(restart)
    os.system(status)

def main():

    verif = verification()

    if verif == True:
        desinstallation()
        installation()
    else:
        installation()
    
    configfile1()
    configfile2()
    configfile3()
    configfile4()
    configfile5()
    configfile6()
    configfile7()
    configfile8()
    configfile9()
    configfile10()
    restartservice()

main()