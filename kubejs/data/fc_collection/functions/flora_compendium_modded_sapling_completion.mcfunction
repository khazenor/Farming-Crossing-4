scoreboard players add @p flora_compendium 1
tellraw @p ["", {"text":"New flora collected! Flora Compendium ("}, {"score":{"name":"@p","objective":"flora_compendium"}}, {"text":"/122)"}]
scoreboard players add @p flora_compendium_modded_sapling_completion 1
tellraw @p ["", {"text":"Modded Sapling Completion ("}, {"score":{"name":"@p","objective":"flora_compendium_modded_sapling_completion"}}, {"text":"/19)"}]
tellraw @p [""]
