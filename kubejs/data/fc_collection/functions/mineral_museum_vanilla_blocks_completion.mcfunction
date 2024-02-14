scoreboard players add @p mineral_museum 1
tellraw @p ["", {"text":"New mineral mined! Mineral Museum ("}, {"score":{"name":"@p","objective":"mineral_museum"}}, {"text":"/57)"}]
scoreboard players add @p mineral_museum_vanilla_blocks_completion 1
tellraw @p ["", {"text":"Vanilla Blocks Completion ("}, {"score":{"name":"@p","objective":"mineral_museum_vanilla_blocks_completion"}}, {"text":"/14)"}]
tellraw @p [""]
