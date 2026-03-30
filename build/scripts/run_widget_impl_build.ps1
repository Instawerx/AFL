param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$RuntimeDir = ".\artifacts\unreal_runtime",
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\unreal_impl"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "widget_impl_build.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

python .\tests\runtime\widget_impl_builder.py --runtime-dir $RuntimeDir --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Widget implementation build failed with exit code $code"
    exit $code
}
Write-Log "Widget implementation build completed successfully."
exit 0
