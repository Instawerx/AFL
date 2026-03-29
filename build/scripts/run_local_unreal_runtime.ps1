param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$RuntimeEnv = ".\build\config\runtime.env.local"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "local_unreal_runtime.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

$envArgs = @()
if (Test-Path $RuntimeEnv) {
    $envArgs = @("--env-file", $RuntimeEnv)
    Write-Log "Using runtime env file: $RuntimeEnv"
}

python .\tests\runtime\unreal_server_adapter.py @envArgs 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE

if ($code -ne 0) {
    Write-Log "Local Unreal runtime failed with exit code $code"
    exit $code
}

Write-Log "Local Unreal runtime completed successfully."
exit 0
