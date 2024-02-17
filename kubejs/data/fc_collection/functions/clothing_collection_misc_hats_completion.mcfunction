scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_misc_hats_completion 1
tellraw @p ["", {"text":"Misc Hats Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_misc_hats_completion"}}, {"text":"/8)"}]
tellraw @p [""]
