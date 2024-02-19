scoreboard players add @p flora_compendium 1
tellraw @p ["", {"text":"New flora collected! Flora Compendium ("}, {"score":{"name":"@p","objective":"flora_compendium"}}, {"text":"/127)"}]
scoreboard players add @p flora_compendium_vanilla_foods_completion 1
tellraw @p ["", {"text":"Vanilla Foods Completion ("}, {"score":{"name":"@p","objective":"flora_compendium_vanilla_foods_completion"}}, {"text":"/17)"}]
tellraw @p [""]
