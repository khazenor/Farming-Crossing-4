scoreboard players add @p clothing_collection_beach_outfit_completion 1
tellraw @p ["", {"text":"Beach Outfit Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_beach_outfit_completion"}}, {"text":"/4)"}]
tellraw @p [""]
