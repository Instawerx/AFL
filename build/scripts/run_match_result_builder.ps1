param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$EventFile = ".\artifacts\runtime\match_events.json"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "match_result_builder.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

if (-not (Test-Path $EventFile)) {
    Write-Log "Event file not found: $EventFile"
    exit 2
}

python .\tests\runtime\match_result_builder.py --event-file $EventFile 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Match result builder failed with exit code $code"
    exit $code
}
Write-Log "Match result builder completed successfully."
exit 0
