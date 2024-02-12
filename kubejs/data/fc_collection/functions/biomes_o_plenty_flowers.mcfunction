scoreboard players add @p flora_compendium 1
tellraw @p ["", {"text":"New flora collected! Flora Compendium ("}, {"score":{"name":"@p","objective":"flora_compendium"}}, {"text":"/122)"}]
scoreboard players add @p biomes_o_plenty_flowers 1
tellraw @p ["", {"text":"Biomes o Plenty Flowers ("}, {"score":{"name":"@p","objective":"biomes_o_plenty_flowers"}}, {"text":"/17)"}]
tellraw @p [""]
