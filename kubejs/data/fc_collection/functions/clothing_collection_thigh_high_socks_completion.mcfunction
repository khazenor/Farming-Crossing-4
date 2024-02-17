scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_thigh_high_socks_completion 1
tellraw @p ["", {"text":"Thigh High Socks Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_thigh_high_socks_completion"}}, {"text":"/32)"}]
tellraw @p [""]
