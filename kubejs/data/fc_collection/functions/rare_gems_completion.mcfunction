scoreboard players add @p mineral_museum 1
tellraw @p ["", {"text":"New mineral mined! Mineral Museum ("}, {"score":{"name":"@p","objective":"mineral_museum"}}, {"text":"/57)"}]
scoreboard players add @p rare_gems_completion 1
tellraw @p ["", {"text":"Rare Gems Completion ("}, {"score":{"name":"@p","objective":"rare_gems_completion"}}, {"text":"/7)"}]
tellraw @p [""]
