scoreboard players add @p mineral_museum 1
tellraw @p ["", {"text":"New mineral mined! Mineral Museum ("}, {"score":{"name":"@p","objective":"mineral_museum"}}, {"text":"/79)"}]
scoreboard players add @p mineral_museum_corundums_completion 1
tellraw @p ["", {"text":"Corundums Completion ("}, {"score":{"name":"@p","objective":"mineral_museum_corundums_completion"}}, {"text":"/18)"}]
tellraw @p [""]
