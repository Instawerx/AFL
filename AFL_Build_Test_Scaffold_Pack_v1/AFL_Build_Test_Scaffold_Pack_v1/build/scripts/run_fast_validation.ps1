[CmdletBinding()]
param(
    [Parameter(Mandatory=$true)][string]$RepoRoot,
    [Parameter(Mandatory=$false)][string]$LogDir = ""
)

$ErrorActionPreference = "Stop"

function Write-Stage([string]$Message) {
    Write-Host ("[AFL][VALIDATE] " + $Message)
}

if (-not (Test-Path $RepoRoot)) {
    throw "RepoRoot does not exist: $RepoRoot"
}

if ([string]::IsNullOrWhiteSpace($LogDir)) {
    $LogDir = Join-Path $RepoRoot "artifacts\logs"
}
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

$python = "python"
$repoScript = Join-Path $RepoRoot "build\scripts\validate_repo.py"
$agentScript = Join-Path $RepoRoot "build\scripts\validate_agents.py"
$namingScript = Join-Path $RepoRoot "build\scripts\validate_naming.py"

foreach ($path in @($repoScript, $agentScript, $namingScript)) {
    if (-not (Test-Path $path)) {
        throw "Missing validation script: $path"
    }
}

Push-Location $RepoRoot
try {
    Write-Stage "Running validate_repo.py"
    & $python $repoScript 2>&1 | Tee-Object -FilePath (Join-Path $LogDir "validate_repo.log")
    if ($LASTEXITCODE -ne 0) { throw "validate_repo.py failed with exit code $LASTEXITCODE" }

    Write-Stage "Running validate_naming.py"
    & $python $namingScript 2>&1 | Tee-Object -FilePath (Join-Path $LogDir "validate_naming.log")
    if ($LASTEXITCODE -ne 0) { throw "validate_naming.py failed with exit code $LASTEXITCODE" }

    Write-Stage "Running validate_agents.py"
    & $python $agentScript 2>&1 | Tee-Object -FilePath (Join-Path $LogDir "validate_agents.log")
    if ($LASTEXITCODE -ne 0) { throw "validate_agents.py failed with exit code $LASTEXITCODE" }

    Write-Stage "Validation complete"
}
finally {
    Pop-Location
}
