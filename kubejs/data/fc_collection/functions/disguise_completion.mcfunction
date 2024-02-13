scoreboard players add @p hat_collection 1
tellraw @p ["", {"text":"New hat obtained! Hat Collection ("}, {"score":{"name":"@p","objective":"hat_collection"}}, {"text":"/234)"}]
scoreboard players add @p disguise_completion 1
tellraw @p ["", {"text":"Disguise Completion ("}, {"score":{"name":"@p","objective":"disguise_completion"}}, {"text":"/32)"}]
tellraw @p [""]
