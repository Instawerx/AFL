param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$EventFile = ".\artifacts\unreal_events\recorded_match_events.json",
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\runtime"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "match_playback.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

if (-not (Test-Path $EventFile)) {
    Write-Log "Playback event file not found: $EventFile"
    exit 2
}

python .\tests\runtime\match_playback.py --event-file $EventFile --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Match playback failed with exit code $code"
    exit $code
}
Write-Log "Match playback completed successfully."
exit 0
