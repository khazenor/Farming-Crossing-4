scoreboard players add @p clothing_collection_halo_completion 1
tellraw @p ["", {"text":"Halo Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_halo_completion"}}, {"text":"/8)"}]
tellraw @p [""]
