param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$RuntimeDir = ".\artifacts\runtime",
    [Parameter(Mandatory=$false)][string]$DataDir = ".\data\afl"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "persistence_archive.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

New-Item -ItemType Directory -Force -Path $DataDir | Out-Null

python .\tests\runtime\persistence_store.py --runtime-dir $RuntimeDir --data-dir $DataDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Persistence archive failed with exit code $code"
    exit $code
}
Write-Log "Persistence archive completed successfully."
exit 0
