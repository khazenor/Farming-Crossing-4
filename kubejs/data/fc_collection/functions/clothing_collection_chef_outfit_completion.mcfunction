scoreboard players add @p clothing_collection_chef_outfit_completion 1
tellraw @p ["", {"text":"Chef Outfit Completion ("}, {"score":{"name":"@p","objective":"clothing_collection_chef_outfit_completion"}}, {"text":"/4)"}]
tellraw @p [""]
