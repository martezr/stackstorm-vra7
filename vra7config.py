# Python script for configuring vRA7 StackStorm Pack

import getpass                                                                       
import subprocess

configfile = '/opt/stackstorm/configs/vra7.yaml'

hostname = raw_input("hostname (vRA FQDN ex. cloud.company.local): ")

# vRA SSl certification verification configuration
verifyssl = raw_input("verify vRA SSL certificate (true/false) [false]: ")
verifysslvalue = verifyssl or 'vsphere.local'

username = raw_input("username: ")

pprompt = lambda: (getpass.getpass(), getpass.getpass('Retype password: '))

p1, p2 = pprompt()
while p1 != p2:
  print('Passwords do not match. Try again')
  p1, p2 = pprompt()

# vRA tenant configuration
tenant = raw_input("tenant name [vsphere.local]: ")
tenantvalue = tenant or 'vsphere.local'

p = subprocess.Popen(["st2", "key", "set", "vra7_password", p1, "--encrypt"],
                         stdout=subprocess.PIPE)
cmdoutput, err = p.communicate()

config = open(configfile, 'w')
config.write("hostname: " + '"' + str(hostname) + '"' + "\n")
config.write("username: " + '"' + str(username) + '"' + "\n")
config.write('password: "{{st2kv.system.vra7_password}}"' + "\n")
config.write("tenant: " + '"' + str(tenantvalue) + '"' + "\n") 
config.write("verify_ssl: " + str(verifyssl) + "\n")
config.close

print("Successfully configured vRA7 integration pack")
