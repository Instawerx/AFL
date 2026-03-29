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
    Write-Host ("[AFL][QUEUE-REWARD] " + $Message)
}

if ([string]::IsNullOrWhiteSpace($LogDir)) {
    $LogDir = Join-Path $RepoRoot "artifacts\logs"
}
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

$gauntletConfig = Join-Path $RepoRoot "build\scripts\queue_reward_test_config.json"
if (-not (Test-Path $gauntletConfig)) {
    $defaultConfig = @'
{
  "scenario_name": "queue_to_reward_stub",
  "description": "Placeholder for AFL queue → session → arena → reward loop",
  "required_events": [
    "queue_joined",
    "session_created",
    "arena_loaded",
    "round_completed",
    "reward_granted"
  ],
  "disallowed_events": [
    "reward_duplicate",
    "client_authority_reward"
  ]
}
'@
    Set-Content -Path $gauntletConfig -Value $defaultConfig -Encoding UTF8
}

Write-Stage "Queue/reward scaffold ready"
Write-Host "TODO: Replace this stub with Gauntlet or custom harness once EOS + economy shell exists."
Write-Host ("Config: " + $gauntletConfig)
