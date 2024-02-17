scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_archer_completion 1
tellraw @p ["", {"text":"Archer Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_archer_completion"}}, {"text":"/12)"}]
tellraw @p [""]
