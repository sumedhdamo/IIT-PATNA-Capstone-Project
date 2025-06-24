# Define backup folders
$BackupFolders = @(
    "E:\ADReports\DC-01",
    "E:\ADReports\DC-02"
)

# Set retention period in days
$RetentionDays = 7
$CutoffDate = (Get-Date).AddDays(-$RetentionDays)

foreach ($Folder in $BackupFolders) {
    Write-Host "Checking folder: $Folder"

    if (Test-Path $Folder) {
        $OldFiles = Get-ChildItem -Path $Folder -File | Where-Object { $_.LastWriteTime -lt $CutoffDate }

        foreach ($File in $OldFiles) {
            try {
                Remove-Item $File.FullName -Force
                Write-Host "Deleted: $($File.FullName)"
            } catch {
                Write-Warning "Failed to delete: $($File.FullName) - $_"
            }
        }
    } else {
        Write-Warning "Folder does not exist: $Folder"
    }
}
