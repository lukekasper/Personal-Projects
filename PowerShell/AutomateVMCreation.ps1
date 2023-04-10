# automate creation of multiple VMs
# if not in Azure Cloud Shell, must authenticate with Azure using: Connect-AzAccount
param([string]$resourceGroup)

# prompt user for username and password and store in credentials variable
$adminCredential = Get-Credential -Message "Enter a username and password for the VM administrator."
For ($i = 1; $i -le 3; $i++) 
{
    # create a name for each VM and write output to console
    $vmName = "ConferenceDemo" + $i
    echo "Creating VM: " $vmName

    # create new VM using variable name
    New-AzVm -ResourceGroupName $resourceGroup -Name $vmName -Credential $adminCredential -Image Canonical:0001-com-ubuntu-server-focal:20_04-lts:latest
}

# run from cmd line using: ./AutomateVMCreation.ps1 learn-0174c2bd-f99a-4eb9-b948-cc412524efe2
# check resource creation from cmd line using: Get-AzResource -ResourceType Microsoft.Compute/virtualMachines