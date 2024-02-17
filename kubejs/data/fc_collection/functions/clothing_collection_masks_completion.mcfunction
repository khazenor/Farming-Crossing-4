scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_masks_completion 1
tellraw @p ["", {"text":"Masks Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_masks_completion"}}, {"text":"/7)"}]
tellraw @p [""]
