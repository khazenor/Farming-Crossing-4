scoreboard players add @p hat_collection 1
tellraw @p ["", {"text":"New hat obtained! Hat Collection ("}, {"score":{"name":"@p","objective":"hat_collection"}}, {"text":"/234)"}]
scoreboard players add @p flat_hats_completion 1
tellraw @p ["", {"text":"Flat Hats Completion ("}, {"score":{"name":"@p","objective":"flat_hats_completion"}}, {"text":"/26)"}]
tellraw @p [""]
