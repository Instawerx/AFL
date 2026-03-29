param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = "."
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "eos_preflight.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

Write-Log "Starting EOS preflight."

$required = @(
    "EOS_PRODUCT_ID",
    "EOS_SANDBOX_ID",
    "EOS_DEPLOYMENT_ID",
    "EOS_CLIENT_ID",
    "EOS_CLIENT_SECRET"
)

$missing = @()
foreach ($name in $required) {
    $value = [Environment]::GetEnvironmentVariable($name)
    if ([string]::IsNullOrWhiteSpace($value)) {
        $missing += $name
    }
}

if ($missing.Count -gt 0) {
    Write-Log ("Missing EOS variables: " + ($missing -join ", "))
    exit 2
}

Write-Log "EOS preflight passed."
exit 0
