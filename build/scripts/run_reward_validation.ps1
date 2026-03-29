param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$ResultFile = ".\artifacts\runtime\match_result.json"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "reward_validation.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

if (-not (Test-Path $ResultFile)) {
    Write-Log "Result file not found: $ResultFile"
    exit 2
}

python .\tests\runtime\reward_engine.py --result-file $ResultFile 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Reward validation failed with exit code $code"
    exit $code
}
Write-Log "Reward validation completed successfully."
exit 0
