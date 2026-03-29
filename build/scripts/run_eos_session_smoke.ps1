param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$Scenario = ".\tests\runtime\scenarios\eos_quickmatch_smoke.yaml",
    [Parameter(Mandatory=$false)][string]$RuntimeEnv = ".\build\config\runtime.env.local"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "eos_session_smoke.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

if (-not (Test-Path $Scenario)) {
    Write-Log "Scenario file not found: $Scenario"
    exit 2
}

$envArgs = @()
if (Test-Path $RuntimeEnv) {
    $envArgs = @("--env-file", $RuntimeEnv)
    Write-Log "Using runtime env file: $RuntimeEnv"
}

python .\tests\runtime\eos_adapter.py --scenario $Scenario @envArgs 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE

if ($code -ne 0) {
    Write-Log "EOS session smoke failed with exit code $code"
    exit $code
}

Write-Log "EOS session smoke completed successfully."
exit 0
