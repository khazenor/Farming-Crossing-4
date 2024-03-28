scoreboard players add @p mineral_museum_modded_blocks_completion 1
tellraw @p ["", {"text":"Modded Blocks Completion ("}, {"score":{"name":"@p","objective":"mineral_museum_modded_blocks_completion"}}, {"text":"/16)"}]
tellraw @p [""]
