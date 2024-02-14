scoreboard players add @p flora_compendium 1
tellraw @p ["", {"text":"New flora collected! Flora Compendium ("}, {"score":{"name":"@p","objective":"flora_compendium"}}, {"text":"/122)"}]
scoreboard players add @p flora_compendium_biomes_o_plenty_flowers_completion 1
tellraw @p ["", {"text":"Biomes o Plenty Flowers Completion ("}, {"score":{"name":"@p","objective":"flora_compendium_biomes_o_plenty_flowers_completion"}}, {"text":"/17)"}]
tellraw @p [""]
