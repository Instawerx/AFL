param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$ExePath = "",
    [Parameter(Mandatory=$false)][string]$Args = ""
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "run_afl_server.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

if ([string]::IsNullOrWhiteSpace($ExePath)) {
    $ExePath = [Environment]::GetEnvironmentVariable("AFL_SERVER_EXE")
}

if ([string]::IsNullOrWhiteSpace($ExePath)) {
    Write-Log "AFL_SERVER_EXE is not set."
    exit 2
}

if (-not (Test-Path $ExePath)) {
    Write-Log "Server executable not found: $ExePath"
    exit 3
}

Write-Log "Starting AFL server: $ExePath $Args"
Start-Process -FilePath $ExePath -ArgumentList $Args -WorkingDirectory $RepoRoot
Write-Log "Server launch command issued."
exit 0
