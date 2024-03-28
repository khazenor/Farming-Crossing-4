scoreboard players add @p mineral_museum_common_gems_completion 1
tellraw @p ["", {"text":"Common Gems Completion ("}, {"score":{"name":"@p","objective":"mineral_museum_common_gems_completion"}}, {"text":"/16)"}]
tellraw @p [""]
