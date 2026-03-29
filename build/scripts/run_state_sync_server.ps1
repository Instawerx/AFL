param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][int]$Port = 9018,
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\runtime"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "state_sync_server.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

python .\tests\runtime\authoritative_match_server.py --port $Port --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "State sync server failed with exit code $code"
    exit $code
}
Write-Log "State sync server completed successfully."
exit 0
