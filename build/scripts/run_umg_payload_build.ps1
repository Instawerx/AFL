param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$HudDir = ".\artifacts\hud",
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\visual_demo"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "umg_payload_build.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

python .\tests\runtime\umg_payload_builder.py --hud-dir $HudDir --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "UMG payload build failed with exit code $code"
    exit $code
}
Write-Log "UMG payload build completed successfully."
exit 0
