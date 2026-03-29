param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$WatchDir = ".\artifacts\unreal_events",
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\runtime"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "live_unreal_hook.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

New-Item -ItemType Directory -Force -Path $WatchDir | Out-Null
New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

python .\tests\runtime\live_unreal_hook.py --watch-dir $WatchDir --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Live Unreal hook failed with exit code $code"
    exit $code
}
Write-Log "Live Unreal hook completed successfully."
exit 0
