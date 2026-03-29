param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$Target = "RunFastAutomation"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "unreal_buildgraph.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

$ueRoot = [Environment]::GetEnvironmentVariable("UE_ROOT")
$uproject = [Environment]::GetEnvironmentVariable("UPROJECT_PATH")

if ([string]::IsNullOrWhiteSpace($ueRoot)) {
    Write-Log "UE_ROOT is not set."
    exit 2
}
if ([string]::IsNullOrWhiteSpace($uproject)) {
    Write-Log "UPROJECT_PATH is not set."
    exit 2
}

$uat = Join-Path $ueRoot "Engine\Build\BatchFiles\RunUAT.bat"
$graph = Join-Path $RepoRoot "build\buildgraph\AFL_BuildGraph.xml"

if (-not (Test-Path $uat)) {
    Write-Log "RunUAT.bat not found at $uat"
    exit 3
}
if (-not (Test-Path $graph)) {
    Write-Log "BuildGraph file not found at $graph"
    exit 4
}

Write-Log "Launching BuildGraph target: $Target"
$arguments = @(
    "BuildGraph",
    "-Script=$graph",
    "-Target=$Target",
    "-Set:UProject=$uproject"
)

& $uat @arguments 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE

if ($code -ne 0) {
    Write-Log "BuildGraph failed with exit code $code"
    exit $code
}

Write-Log "BuildGraph completed successfully."
exit 0
