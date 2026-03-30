param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$RuntimeDir = ".\artifacts\unreal_runtime",
    [Parameter(Mandatory=$false)][string]$ImplDir = ".\artifacts\unreal_impl",
    [Parameter(Mandatory=$false)][string]$OutputDir = ".\artifacts\unreal_impl"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "demo_bootflow_build.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

python .\tests\runtime\demo_bootflow_builder.py --runtime-dir $RuntimeDir --impl-dir $ImplDir --output-dir $OutputDir 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Demo bootflow build failed with exit code $code"
    exit $code
}
Write-Log "Demo bootflow build completed successfully."
exit 0
