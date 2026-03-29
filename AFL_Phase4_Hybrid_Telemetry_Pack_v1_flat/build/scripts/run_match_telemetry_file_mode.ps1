param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$Scenario = ".\tests\runtime\scenarios\multi_capture.yaml"
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

$logDir = Join-Path $RepoRoot "artifacts\logs"
New-Item -ItemType Directory -Force -Path $logDir | Out-Null
$logFile = Join-Path $logDir "match_telemetry_file_mode.log"

function Write-Log {
    param([string]$Message)
    $line = "[{0}] {1}" -f (Get-Date -Format "s"), $Message
    $line | Tee-Object -FilePath $logFile -Append
}

if (-not (Test-Path $Scenario)) {
    Write-Log "Scenario file not found: $Scenario"
    exit 2
}

python .\tests\runtime\telemetry_ingestor.py --mode file --scenario $Scenario 2>&1 | Tee-Object -FilePath $logFile -Append
$code = $LASTEXITCODE
if ($code -ne 0) {
    Write-Log "Telemetry file mode failed with exit code $code"
    exit $code
}
Write-Log "Telemetry file mode completed successfully."
exit 0
