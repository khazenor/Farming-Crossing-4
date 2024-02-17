scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_mobster_completion 1
tellraw @p ["", {"text":"Mobster Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_mobster_completion"}}, {"text":"/4)"}]
tellraw @p [""]
