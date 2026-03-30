param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$VisualDir = ".\artifacts\visual_demo",
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\unreal_runtime"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "unreal_runtime_bridge_build.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

python .\tests\runtime\unreal_runtime_bridge_builder.py --visual-dir $VisualDir --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Unreal runtime bridge build failed with exit code $code"
    exit $code
}
Write-Log "Unreal runtime bridge build completed successfully."
exit 0
