param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$ImplDir = ".\artifacts\unreal_impl",
    [Parameter(Mandatory=$false)][string]$RuntimeDir = ".\artifacts\unreal_runtime"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "unreal_execution_validation.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

python .\tests\runtime\unreal_execution_validator.py --impl-dir $ImplDir --runtime-dir $RuntimeDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Unreal execution validation failed with exit code $code"
    exit $code
}
Write-Log "Unreal execution validation completed successfully."
exit 0
