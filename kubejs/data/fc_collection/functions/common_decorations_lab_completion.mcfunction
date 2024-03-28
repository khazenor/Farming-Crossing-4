scoreboard players add @p common_decorations_lab_completion 1
tellraw @p ["", {"text":"Lab Completion ("}, {"score":{"name":"@p","objective":"common_decorations_lab_completion"}}, {"text":"/13)"}]
tellraw @p [""]
