scoreboard players add @p mineral_museum_corundums_completion 1
tellraw @p ["", {"text":"Corundums Completion ("}, {"score":{"name":"@p","objective":"mineral_museum_corundums_completion"}}, {"text":"/18)"}]
tellraw @p [""]
