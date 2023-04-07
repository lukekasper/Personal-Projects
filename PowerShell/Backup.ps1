# Create a backup
# run in terminal:
# mkdir app
# cd app
# touch index.html app.js
# cd ..
# touch Backup.ps1
# code Backup.ps1

Param(
  [string]$Path = './app', # adds default value of './app'
  [string]$DestinationPath = './'
)
$date = Get-Date -format "yyyy-MM-dd"
Compress-Archive -Path $Path -CompressionLevel 'Fastest' -DestinationPath "$($DestinationPath + 'backup-' + $date)"
Write-Host "Created backup at $($DestinationPath + 'backup-' + $date + '.zip')"