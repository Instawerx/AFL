param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$VisualDir = ".\artifacts\visual_demo",
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\visual_demo"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "scene_playback_build.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

python .\tests\runtime\scene_playback_builder.py --visual-dir $VisualDir --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Scene playback build failed with exit code $code"
    exit $code
}
Write-Log "Scene playback build completed successfully."
exit 0
