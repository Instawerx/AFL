param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$Scenario = ".\tests\runtime\scenarios\multiplayer_quickmatch.yaml",
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\runtime"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "multiplayer_session.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

if (-not (Test-Path $Scenario)) {
    Write-Log "Scenario file not found: $Scenario"
    exit 2
}

python .\tests\runtime\multiplayer_orchestrator.py --scenario $Scenario --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Multiplayer session failed with exit code $code"
    exit $code
}
Write-Log "Multiplayer session completed successfully."
exit 0
