# CreateFile.ps1
Param(
    $Path
)
New-Item $Path # creates a new file at Path
Write-Host "File $Path was created"

# call from cmd line:
# ./CreateFile.ps1 -Path './newfile.txt' # File ./newfile.txt was created.
# ./CreateFile.ps1 -Path './anotherfile.txt' # File ./anotherfile.txt was created.