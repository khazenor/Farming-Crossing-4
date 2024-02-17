scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_knight_armor_completion 1
tellraw @p ["", {"text":"Knight Armor Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_knight_armor_completion"}}, {"text":"/20)"}]
tellraw @p [""]
