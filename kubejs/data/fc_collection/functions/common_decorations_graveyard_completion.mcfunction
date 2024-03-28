scoreboard players add @p common_decorations_graveyard_completion 1
tellraw @p ["", {"text":"Graveyard Completion ("}, {"score":{"name":"@p","objective":"common_decorations_graveyard_completion"}}, {"text":"/19)"}]
tellraw @p [""]
