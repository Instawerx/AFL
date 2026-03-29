[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$RepoRoot,
    [Parameter(Mandatory=$true)][string]$ProjectPath,
    [Parameter(Mandatory=$true)][string]$UERoot,
    [Parameter(Mandatory=$false)][string]$Platform = "Win64",
    [Parameter(Mandatory=$false)][string]$Configuration = "Development",
    [Parameter(Mandatory=$false)][string]$LogDir = ""
)

$ErrorActionPreference = "Stop"

function Write-Stage([string]$Message) {
    Write-Host ("[AFL][SMOKE] " + $Message)
}

if (-not (Test-Path $ProjectPath)) {
    throw "ProjectPath does not exist: $ProjectPath"
}

$runUAT = Join-Path $UERoot "Engine\Build\BatchFiles\RunUAT.bat"
if (-not (Test-Path $runUAT)) {
    throw "RunUAT not found: $runUAT"
}

if ([string]::IsNullOrWhiteSpace($LogDir)) {
    $LogDir = Join-Path $RepoRoot "artifacts\logs"
}
$packageDir = Join-Path $RepoRoot "artifacts\package-smoke"
New-Item -ItemType Directory -Force -Path $LogDir, $packageDir | Out-Null

$uatArgs = @(
    "BuildCookRun",
    "-project=$ProjectPath",
    "-noP4",
    "-build",
    "-cook",
    "-stage",
    "-package",
    "-clientconfig=$Configuration",
    "-targetplatform=$Platform",
    "-archivedirectory=$packageDir",
    "-utf8output",
    "-unattended"
)

Write-Stage "Packaging smoke build"
Push-Location $RepoRoot
try {
    & $runUAT @uatArgs 2>&1 | Tee-Object -FilePath (Join-Path $LogDir "packaged_smoke.log")
    if ($LASTEXITCODE -ne 0) {
        throw "Smoke package failed with exit code $LASTEXITCODE"
    }

    Write-Stage "Packaging complete. Add your executable launch and exit-code assertions here."
    Write-Host "TODO: Launch packaged client/server smoke scenario after first playable slice exists."
}
finally {
    Pop-Location
}
