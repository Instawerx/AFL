param([string]$BroadcastDir=".\artifacts\broadcast",[string]$OutputDir=".\artifacts\hud")

python .\tests\runtime\hud_bridge_builder.py --broadcast-dir $BroadcastDir --output-dir $OutputDir
