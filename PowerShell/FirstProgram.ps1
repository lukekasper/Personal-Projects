## First Program

# New-Item HelloWorld.ps1: create a new powershell file in the current directory
# code HelloWorld.ps1: opens PowerShell editor (can define full path instead of file name to run a script from a different directory)
# Write-Output 'Hello World!': writes 'Hello World!' to console
# . ./HelloWorld.ps1: '.' runs the script 'HelloWorld.ps1' which is in the current directory
# Read-Host - Prompt: prompt a user for input
# $name: where to store prompt variable entered by user; define variables with a $var = ...

Write-Output 'Hello World!'

$name = Read-Host -Prompt "Please enter your name"
Write-Output "Congratulations $name! You have written your first code with PowerShell!"
