param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$RuntimeDir = ".\artifacts\unreal_runtime",
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\unreal_runtime"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "demo_map_manifest_build.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

python .\tests\runtime\demo_map_manifest_builder.py --runtime-dir $RuntimeDir --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Demo map manifest build failed with exit code $code"
    exit $code
}
Write-Log "Demo map manifest build completed successfully."
exit 0
