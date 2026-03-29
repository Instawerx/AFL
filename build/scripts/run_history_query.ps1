param(
    [Parameter(Mandatory=$false)][string]$RepoRoot = ".",
    [Parameter(Mandatory=$false)][string]$DataDir = ".\data\afl",
    [Parameter(Mandatory=$false)][int]$Limit = 5
)

$ErrorActionPreference = "Stop"
Set-Location $RepoRoot

python .\tests\runtime\history_query.py --data-dir $DataDir --limit $Limit
exit $LASTEXITCODE
