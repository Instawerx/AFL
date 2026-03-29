param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$Scenario = ".\tests\runtime\scenarios\network_quickmatch.yaml",
    [Parameter(Mandatory=$false)][string]$Host = "127.0.0.1",
    [Parameter(Mandatory=$false)][int]$Port = 9007
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "network_client_sim.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

if (-not (Test-Path $Scenario)) {
    Write-Log "Scenario file not found: $Scenario"
    exit 2
}

python .\tests\runtime\network_client_sim.py --scenario $Scenario --host $Host --port $Port 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Network client sim failed with exit code $code"
    exit $code
}
Write-Log "Network client sim completed successfully."
exit 0
