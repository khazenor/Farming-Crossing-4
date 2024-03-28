scoreboard players add @p common_decorations_toys_completion 1
tellraw @p ["", {"text":"Toys Completion ("}, {"score":{"name":"@p","objective":"common_decorations_toys_completion"}}, {"text":"/15)"}]
tellraw @p [""]
