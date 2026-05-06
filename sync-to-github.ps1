# One-command sync: stage, commit (if needed), push to origin main.
# Usage: .\sync-to-github.ps1
#         .\sync-to-github.ps1 -Message "update api"

param(
    [string]$Message = ""
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

if (-not $Message) {
    $Message = "Sync: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
}

if (-not (Test-Path .git)) {
    Write-Error "No .git in $($PSScriptRoot). Run git init and add remote first."
}

git add -A
$dirty = git status --porcelain
if (-not $dirty) {
    Write-Host "Working tree clean; nothing to commit."
} else {
    git commit -m $Message
    if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
}

git push origin main
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host "Done. Pushed to origin/main."
