scoreboard players add @p hat_collection_disguise_completion 1
tellraw @p ["", {"text":"Disguise Completion ("}, {"score":{"name":"@p","objective":"hat_collection_disguise_completion"}}, {"text":"/32)"}]
tellraw @p [""]
