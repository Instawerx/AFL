param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][int]$Port = 9120,
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\broadcast"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null

$clientOut = Join-Path $logDir "spectator_client.out.log"
$clientErr = Join-Path $logDir "spectator_client.err.log"
$serverLog = Join-Path $logDir "spectator_stream_server.out.log"

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

# Start spectator first so it is already bound to the UDP port
$client = Start-Process `
    -FilePath python `
    -ArgumentList ".\tests\runtime\spectator_sim.py --port $Port --output-dir $OutputDir --max-packets 5" `
    -PassThru `
    -RedirectStandardOutput $clientOut `
    -RedirectStandardError $clientErr

Start-Sleep -Seconds 1

# Then broadcast packets
python .\tests\runtime\udp_state_broadcaster.py --port $Port --state-file .\artifacts\runtime\authoritative_state_snapshot.json --output-dir .\artifacts\broadcast --ticks 10 2>&1 | Tee-Object -FilePath $serverLog -Append
$serverCode = $LASTEXITCODE

# Client may already be gone by the time we reach here, so guard it
$clientCode = 0
try {
    if (Get-Process -Id $client.Id -ErrorAction SilentlyContinue) {
        Wait-Process -Id $client.Id -Timeout 10
    }
    $client.Refresh()
    if ($null -ne $client.ExitCode) {
        $clientCode = $client.ExitCode
    }
}
catch {
    $clientCode = 0
}

if ($serverCode -ne 0) { exit $serverCode }
if ($clientCode -ne 0) { exit $clientCode }

Write-Host "Spectator simulation completed successfully."
exit 0
