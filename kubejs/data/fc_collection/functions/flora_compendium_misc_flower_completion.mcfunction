scoreboard players add @p flora_compendium 1
tellraw @p ["", {"text":"New flora collected! Flora Compendium ("}, {"score":{"name":"@p","objective":"flora_compendium"}}, {"text":"/127)"}]
scoreboard players add @p flora_compendium_misc_flower_completion 1
tellraw @p ["", {"text":"Misc Flower Completion ("}, {"score":{"name":"@p","objective":"flora_compendium_misc_flower_completion"}}, {"text":"/9)"}]
tellraw @p [""]
