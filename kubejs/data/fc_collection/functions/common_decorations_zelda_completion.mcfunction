scoreboard players add @p common_decorations_zelda_completion 1
tellraw @p ["", {"text":"Zelda Completion ("}, {"score":{"name":"@p","objective":"common_decorations_zelda_completion"}}, {"text":"/6)"}]
tellraw @p [""]
