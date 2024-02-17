scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_winter_survivalist_completion 1
tellraw @p ["", {"text":"Winter Survivalist Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_winter_survivalist_completion"}}, {"text":"/12)"}]
tellraw @p [""]
