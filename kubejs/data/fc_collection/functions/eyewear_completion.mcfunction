scoreboard players add @p hat_collection 1
tellraw @p ["", {"text":"New hat obtained! Hat Collection ("}, {"score":{"name":"@p","objective":"hat_collection"}}, {"text":"/234)"}]
scoreboard players add @p eyewear_completion 1
tellraw @p ["", {"text":"Eyewear Completion ("}, {"score":{"name":"@p","objective":"eyewear_completion"}}, {"text":"/24)"}]
tellraw @p [""]
