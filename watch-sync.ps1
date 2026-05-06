# Optional auto-sync: every N seconds, if there are changes, commit and push.
# Run: powershell -NoProfile -ExecutionPolicy Bypass -File .\watch-sync.ps1
# Ctrl+C to stop.

param(
    [int]$IntervalSeconds = 20,
    [string]$Message = "auto sync"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

Write-Host "Polling every ${IntervalSeconds}s. Ctrl+C to stop."

while ($true) {
    Start-Sleep -Seconds $IntervalSeconds
    $dirty = git status --porcelain 2>$null
    if (-not $dirty) { continue }
    Write-Host "[watch-sync] $(Get-Date -Format o) Changes detected, syncing..."
    & (Join-Path $PSScriptRoot "sync-to-github.ps1") -Message $Message
}
