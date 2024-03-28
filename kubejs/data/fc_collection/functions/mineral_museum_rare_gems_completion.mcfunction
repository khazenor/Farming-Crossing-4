scoreboard players add @p mineral_museum_rare_gems_completion 1
tellraw @p ["", {"text":"Rare Gems Completion ("}, {"score":{"name":"@p","objective":"mineral_museum_rare_gems_completion"}}, {"text":"/7)"}]
tellraw @p [""]
