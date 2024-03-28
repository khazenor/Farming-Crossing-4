scoreboard players add @p common_decorations_arts_completion 1
tellraw @p ["", {"text":"Arts Completion ("}, {"score":{"name":"@p","objective":"common_decorations_arts_completion"}}, {"text":"/14)"}]
tellraw @p [""]
