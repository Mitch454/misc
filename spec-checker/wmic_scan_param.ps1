param ($ArrComputers)


# Takes targets as the argument, a single target or an array eg.
# 192.168.1.10,192.168.1.11,192.168.1.12    or
# "192.168.1.10","192.168.1.11",PC001,PC002

#  or we can hardcode the array instead like this
#  $ArrComputers = ".",".","."
#  "." means local system

Clear-Host
foreach ($i in $ArrComputers) 
{
    $computerSystem = get-wmiobject Win32_ComputerSystem -Computer $i
    $computerBIOS = get-wmiobject Win32_BIOS -Computer $i
    $computerOS = get-wmiobject Win32_OperatingSystem -Computer $i
    $computerCPU = get-wmiobject Win32_Processor -Computer $i

        "-------------------------------------------------------"
        $computerSystem.Name   # hostname
        $computerSystem.Manufacturer  # Make
        $computerSystem.Model   # Model
        $computerBIOS.SerialNumber  # serial
        $computerCPU.Name  # CPU 
        $computerOS.caption   # OS name
        $computerOS.Version  # OSversion
        $computerSystem.UserName   # Current user
}       


#  $computerHDD = Get-WmiObject Win32_LogicalDisk -ComputerName $i -Filter drivetype=3
# "HDD Capacity: "  + "{0:N2}" -f ($computerHDD.Size/1GB) + "GB"
# "HDD Space: " + "{0:P2}" -f ($computerHDD.FreeSpace/$computerHDD.Size) + " Free (" + "{0:N2}" -f ($computerHDD.FreeSpace/1GB) + "GB)"
# "RAM: " + "{0:N2}" -f ($computerSystem.TotalPhysicalMemory/1GB) + "GB"


