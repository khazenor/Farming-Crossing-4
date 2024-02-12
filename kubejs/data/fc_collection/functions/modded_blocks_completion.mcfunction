scoreboard players add @p mineral_museum 1
tellraw @p ["", {"text":"New mineral mined! Mineral Museum ("}, {"score":{"name":"@p","objective":"mineral_museum"}}, {"text":"/57)"}]
scoreboard players add @p modded_blocks_completion 1
tellraw @p ["", {"text":"Modded Blocks Completion ("}, {"score":{"name":"@p","objective":"modded_blocks_completion"}}, {"text":"/12)"}]
tellraw @p [""]
