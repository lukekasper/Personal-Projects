# Create File with Decorator
Param(
    [Parameter(Mandatory, HelpMessage="Please provide a valid path")]
    [string]$Path # mandate type of string
)
New-Item $Path
Write-Host "File created at path $Path"
