scoreboard players add @p clothing_collection 1
tellraw @p ["", {"text":"New clothing item obtained! Clothing Collection ("}, {"score":{"name":"@p","objective":"clothing_collection"}}, {"text":"/235)"}]
scoreboard players add @p clothing_collection_christmas_elves_completion 1
tellraw @p ["", {"text":"Christmas Elves Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_christmas_elves_completion"}}, {"text":"/14)"}]
tellraw @p [""]
