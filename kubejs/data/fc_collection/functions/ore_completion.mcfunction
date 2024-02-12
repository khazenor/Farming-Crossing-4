scoreboard players add @p mineral_museum 1
tellraw @p ["", {"text":"New mineral mined! Mineral Museum ("}, {"score":{"name":"@p","objective":"mineral_museum"}}, {"text":"/57)"}]
scoreboard players add @p ore_completion 1
tellraw @p ["", {"text":"Ore Completion ("}, {"score":{"name":"@p","objective":"ore_completion"}}, {"text":"/8)"}]
tellraw @p [""]
