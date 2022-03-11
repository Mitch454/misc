import psutil
import platform
from datetime import datetime
import csv
import os
import socket
import subprocess
import random


User = os.getlogin()


fqdn = socket.getfqdn()


def OSbits():
    OSbits = '32-bit'
    if os.name == 'nt':
        output = subprocess.check_output(['wmic', 'os', 'get', 'OSArchitecture'])
        OSbits = output.split()[1]
    else:
        output = subprocess.check_output(['uname', '-m'])
        if 'x86_64' in output:
            OSbits = '64'
        else:
            OSbits = '32'
    return OSbits

OSbit = OSbits()

trim = str(OSbit).split("'")

OSbit = (trim[1])

print('====  OSbit', OSbit)


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

uname = platform.uname()
#print('====  main uname',uname) 


#
hostName = uname.node
print('====  hostName', hostName)


#
OSRelease = uname.release
OSfamily = uname.system
OSname = OSfamily +' '+ OSRelease
print('====  OSname', OSname)


#
OSVersion = uname.version
print('====  OSVersion',OSVersion)


#
Processor = uname.processor
print('====  Processor', Processor)

#
PhysicalCores = psutil.cpu_count(logical=False)
print('====  PhysicalCores', PhysicalCores)

#
TotalCores =psutil.cpu_count(logical=True)
print('====  TotalCores', TotalCores)


svmem = psutil.virtual_memory()

TotalRam = get_size(svmem.total)
print('====  TotalRam', TotalRam)






data = [hostName, User, OSname, OSVersion, OSbit,Processor,PhysicalCores,TotalCores,TotalRam, fqdn]

try:
    with open('output.csv', 'a+', newline='') as f:
        write = csv.writer(f)
        write.writerows([data])
except:
    print('Permission error, perhaps output.csv is already open..')
    with open('output_' + User + str(random.randint(1,999)) + ".csv", 'a+', newline='') as f:
        write = csv.writer(f)
        write.writerows([data])


