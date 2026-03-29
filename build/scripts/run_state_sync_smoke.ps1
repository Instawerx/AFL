param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][int]$Port = 9018,
    [Parameter(Mandatory=$false)][string]$Scenario = ".\tests\runtime\scenarios\state_sync_quickmatch.yaml"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$clientLog = Join-Path $logDir "state_sync_client_smoke.log"
$serverOut = Join-Path $logDir "state_sync_server_smoke.out.log"
$serverErr = Join-Path $logDir "state_sync_server_smoke.err.log"

$server = Start-Process `
    -FilePath python `
    -ArgumentList ".\tests\runtime\authoritative_match_server.py --port $Port --output-dir .\artifacts\runtime --once-complete" `
    -PassThru `
    -RedirectStandardOutput $serverOut `
    -RedirectStandardError $serverErr

Start-Sleep -Seconds 2

python .\tests\runtime\state_sync_client_sim.py --scenario $Scenario --host 127.0.0.1 --port $Port 2>&1 | Tee-Object -FilePath $clientLog -Append
$clientCode = $LASTEXITCODE

if ($server -and !$server.HasExited) {
    try { Stop-Process -Id $server.Id -Force } catch {}
}

if ($clientCode -ne 0) { exit $clientCode }
Write-Host "State sync smoke completed successfully."
exit 0
