scoreboard players add @p flora_compendium 1
tellraw @p ["", {"text":"New flora collected! Flora Compendium ("}, {"score":{"name":"@p","objective":"flora_compendium"}}, {"text":"/122)"}]
scoreboard players add @p flora_compendium_vanilla_flower_completion 1
tellraw @p ["", {"text":"Vanilla Flower Completion ("}, {"score":{"name":"@p","objective":"flora_compendium_vanilla_flower_completion"}}, {"text":"/18)"}]
tellraw @p [""]
