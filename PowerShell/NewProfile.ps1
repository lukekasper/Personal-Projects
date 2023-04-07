# Run in cmd line: 
# $Profile | Select-Object *
# New-Item `
#   -ItemType "file" `
#   -Value 'Write-Host "Hello <replace with your name>, welcome back" -foregroundcolor Green ' `
#   -Path $Profile.CurrentUserCurrentHost -Force

# $PI = 3.14
# New-Item -Path . -Name "PI.ps1" -ItemType "file"
# code PI.ps1
$PI = 3
Write-Host "The value of `$PI is now $PI, inside the script"