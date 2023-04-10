# create a new Azure VM
# resource group: learn-0174c2bd-f99a-4eb9-b948-cc412524efe2
# name: testvm-eus-01
# Use the Get-Credential cmdlet and feed the results into the Credential parameter
# Location: choose the location of the resource (eastus)
# Choose Ubuntu Linux OS as image: Canonical:0001-com-ubuntu-server-focal:20_04-lts:latest
# OpenPorts 22: allows SSH into machine
# Create a public IP address name: testvm-01
New-AzVm -ResourceGroupName learn-0174c2bd-f99a-4eb9-b948-cc412524efe2 -Name "testvm-eus-01" -Credential (Get-Credential) -Location "eastus" -Image Canonical:0001-com-ubuntu-server-focal:20_04-lts:latest -OpenPorts 22 -PublicIpAddressName "testvm-01"

# query vm and assign to a variable
$vm = (Get-AzVM -Name "testvm-eus-01" -ResourceGroupName learn-0174c2bd-f99a-4eb9-b948-cc412524efe2)

# use "." notation to dig into complex objects associated with VM
$vm.HardwareProfile

# info on storage disks
$vm.StorageProfile.OsDisk

# get public IP address, use this to connect to VM with SSH
Get-AzPublicIpAddress -ResourceGroupName learn-0174c2bd-f99a-4eb9-b948-cc412524efe2 -Name "testvm-01"

# connect to Linux VM using: 'ssh username@publicIPaddress'
ssh lukekasper@20.172.204.90

# stop and delete VM
Stop-AzVM -Name $vm.Name -ResourceGroupName $vm.ResourceGroupName
Remove-AzVM -Name $vm.Name -ResourceGroupName $vm.ResourceGroupName

# list all resource in resource group
Get-AzResource -ResourceGroupName $vm.ResourceGroupName | Format-Table

# must also delete all resources associated with the creation of the VM
$vm | Remove-AzNetworkInterface –Force
Get-AzDisk -ResourceGroupName $vm.ResourceGroupName -DiskName $vm.StorageProfile.OSDisk.Name | Remove-AzDisk -Force
Get-AzVirtualNetwork -ResourceGroupName $vm.ResourceGroupName | Remove-AzVirtualNetwork -Force
Get-AzNetworkSecurityGroup -ResourceGroupName $vm.ResourceGroupName | Remove-AzNetworkSecurityGroup -Force
Get-AzPublicIpAddress -ResourceGroupName $vm.ResourceGroupName | Remove-AzPublicIpAddress -Force