scoreboard players add @p mineral_museum 1
tellraw @p ["", {"text":"New mineral mined! Mineral Museum ("}, {"score":{"name":"@p","objective":"mineral_museum"}}, {"text":"/79)"}]
scoreboard players add @p mineral_museum_ore_completion 1
tellraw @p ["", {"text":"Ore Completion ("}, {"score":{"name":"@p","objective":"mineral_museum_ore_completion"}}, {"text":"/8)"}]
tellraw @p [""]
