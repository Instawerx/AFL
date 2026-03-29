param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][int]$Port = 9120,
    [Parameter(Mandatory=$false)][string]$StateFile = ".\artifacts\runtime\authoritative_state_snapshot.json",
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\broadcast"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "unreal_state_stream.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

if (-not (Test-Path $StateFile)) {
    Write-Log "State file not found: $StateFile"
    exit 2
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

python .\tests\runtime\udp_state_broadcaster.py --port $Port --state-file $StateFile --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Unreal state stream failed with exit code $code"
    exit $code
}
Write-Log "Unreal state stream completed successfully."
exit 0
