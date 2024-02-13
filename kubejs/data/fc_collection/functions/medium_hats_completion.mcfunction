scoreboard players add @p hat_collection 1
tellraw @p ["", {"text":"New hat obtained! Hat Collection ("}, {"score":{"name":"@p","objective":"hat_collection"}}, {"text":"/234)"}]
scoreboard players add @p medium_hats_completion 1
tellraw @p ["", {"text":"Medium Hats Completion ("}, {"score":{"name":"@p","objective":"medium_hats_completion"}}, {"text":"/23)"}]
tellraw @p [""]
