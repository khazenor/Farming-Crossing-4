scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_skirts_and_boots_completion 1
tellraw @p ["", {"text":"Skirts and Boots Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_skirts_and_boots_completion"}}, {"text":"/32)"}]
tellraw @p [""]
