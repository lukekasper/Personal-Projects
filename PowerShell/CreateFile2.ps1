# Create file with user written error
Param(
    $Path
)
If (-Not $Path -eq '') {
    New-Item $Path
    Write-Host "File created at path $Path"
}
Else {
    Write-Error: "Path cannot be empty"
}
