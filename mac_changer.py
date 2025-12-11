#!/usr/bin/env python
import subprocess
import optparse
def arguments ():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help=" interface to change mac address")
    parser.add_option("-m", "--mac", dest="mac", help="mac address to change")

    (options, args) = parser.parse_args()
    if not options.interface or not options.mac:
        parser.error("Please specify the interface and mac address")
    return options



def changemac(interface,newmac):
    print(" changing the Mac Address of the interface " + interface + " to " + newmac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newmac])
    subprocess.call(["ifconfig", interface, "up"])



options = arguments()
changemac(options.interface,options.mac)


#subprocess.call("ifconfig " + interface + " down" , shell = True)
#subprocess.call("ifconfig " +  interface + " hw ether " + newmac , shell = True)
#subprocess.call("ifconfig " + interface + " up", shell = True)





