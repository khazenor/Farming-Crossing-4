scoreboard players add @p flora_compendium 1
tellraw @p ["", {"text":"New flora collected! Flora Compendium ("}, {"score":{"name":"@p","objective":"flora_compendium"}}, {"text":"/127)"}]
scoreboard players add @p flora_compendium_vanilla_sapling_completion 1
tellraw @p ["", {"text":"Vanilla Sapling Completion ("}, {"score":{"name":"@p","objective":"flora_compendium_vanilla_sapling_completion"}}, {"text":"/8)"}]
tellraw @p [""]
