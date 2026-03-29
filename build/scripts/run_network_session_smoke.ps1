param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][int]$Port = 9007,
    [Parameter(Mandatory=$false)][string]$Scenario = ".\tests\runtime\scenarios\network_quickmatch.yaml"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$serverLog = Join-Path $logDir "network_session_server_smoke.log"
$clientLog = Join-Path $logDir "network_client_smoke.log"

$server = Start-Process -FilePath python -ArgumentList ".\tests\runtime\network_session_server.py --port $Port --output-dir .\artifacts\runtime --once-ready" -PassThru -RedirectStandardOutput $serverLog -RedirectStandardError $serverLog
Start-Sleep -Seconds 2

python .\tests\runtime\network_client_sim.py --scenario $Scenario --host 127.0.0.1 --port $Port 2>&1 | Tee-Object -FilePath $clientLog -Append
$clientCode = $LASTEXITCODE

if ($server -and !$server.HasExited) {
    try { Stop-Process -Id $server.Id -Force } catch {}
}

if ($clientCode -ne 0) { exit $clientCode }
Write-Host "Network session smoke completed successfully."
exit 0
