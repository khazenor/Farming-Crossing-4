scoreboard players add @p flora_compendium 1
tellraw @p ["", {"text":"New flora collected! Flora Compendium ("}, {"score":{"name":"@p","objective":"flora_compendium"}}, {"text":"/122)"}]
scoreboard players add @p misc_flower_completion 1
tellraw @p ["", {"text":"Misc Flower Completion ("}, {"score":{"name":"@p","objective":"misc_flower_completion"}}, {"text":"/9)"}]
tellraw @p [""]
