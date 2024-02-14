scoreboard players add @p hat_collection 1
tellraw @p ["", {"text":"New hat obtained! Hat Collection ("}, {"score":{"name":"@p","objective":"hat_collection"}}, {"text":"/234)"}]
scoreboard players add @p hat_collection_tall_hats_completion 1
tellraw @p ["", {"text":"Tall Hats Completion ("}, {"score":{"name":"@p","objective":"hat_collection_tall_hats_completion"}}, {"text":"/8)"}]
tellraw @p [""]
