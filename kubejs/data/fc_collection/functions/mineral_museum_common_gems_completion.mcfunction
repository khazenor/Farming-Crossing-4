scoreboard players add @p mineral_museum 1
tellraw @p ["", {"text":"New mineral mined! Mineral Museum ("}, {"score":{"name":"@p","objective":"mineral_museum"}}, {"text":"/79)"}]
scoreboard players add @p mineral_museum_common_gems_completion 1
tellraw @p ["", {"text":"Common Gems Completion ("}, {"score":{"name":"@p","objective":"mineral_museum_common_gems_completion"}}, {"text":"/16)"}]
tellraw @p [""]
