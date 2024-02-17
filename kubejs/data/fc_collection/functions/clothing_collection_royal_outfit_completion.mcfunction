scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_royal_outfit_completion 1
tellraw @p ["", {"text":"Royal Outfit Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_royal_outfit_completion"}}, {"text":"/18)"}]
tellraw @p [""]
