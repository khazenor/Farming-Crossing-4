scoreboard players add @p common_decorations_trophies_completion 1
tellraw @p ["", {"text":"Trophies Completion ("}, {"score":{"name":"@p","objective":"common_decorations_trophies_completion"}}, {"text":"/9)"}]
tellraw @p [""]
