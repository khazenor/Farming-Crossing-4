scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_cat_ears_completion 1
tellraw @p ["", {"text":"Cat Ears Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_cat_ears_completion"}}, {"text":"/6)"}]
tellraw @p [""]
