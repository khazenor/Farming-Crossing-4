scoreboard players add @p clothing_collection_christmas_completion 1
tellraw @p ["", {"text":"Christmas Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_christmas_completion"}}, {"text":"/7)"}]
tellraw @p [""]
