param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$Scenario = ".\tests\runtime\scenarios\quickmatch_reward.yaml",
    [Parameter(Mandatory=$false)][string]$RuntimeEnv = ".\build\config\runtime.env.local"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "queue_reward_harness.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

Write-Log "Starting queue-reward harness."
if (-not (Test-Path $Scenario)) {
    Write-Log "Scenario file not found: $Scenario"
    exit 2
}

$envArgs = @()
if (Test-Path $RuntimeEnv) {
    $envArgs = @("--env-file", $RuntimeEnv)
    Write-Log "Using runtime env file: $RuntimeEnv"
} else {
    Write-Log "Runtime env file not found; using current process environment."
}

python .\tests\runtime\queue_reward_harness.py --scenario $Scenario @envArgs 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE

if ($code -ne 0) {
    Write-Log "Harness failed with exit code $code"
    exit $code
}

Write-Log "Harness completed successfully."
exit 0
