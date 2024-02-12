scoreboard players add @p flora_compendium 1
tellraw @p ["", {"text":"New flora collected! Flora Compendium ("}, {"score":{"name":"@p","objective":"flora_compendium"}}, {"text":"/122)"}]
scoreboard players add @p moded_foods_completion 1
tellraw @p ["", {"text":"Moded Foods Completion ("}, {"score":{"name":"@p","objective":"moded_foods_completion"}}, {"text":"/21)"}]
tellraw @p [""]
