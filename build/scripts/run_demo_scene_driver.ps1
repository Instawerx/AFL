param([string]$HudDir=".\artifacts\hud",[string]$OutputDir=".\artifacts\hud")

python .\tests\runtime\demo_scene_driver.py --hud-dir $HudDir --output-dir $OutputDir
