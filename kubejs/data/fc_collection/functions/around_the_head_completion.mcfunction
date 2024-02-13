scoreboard players add @p hat_collection 1
tellraw @p ["", {"text":"New hat obtained! Hat Collection ("}, {"score":{"name":"@p","objective":"hat_collection"}}, {"text":"/234)"}]
scoreboard players add @p around_the_head_completion 1
tellraw @p ["", {"text":"Around the Head Completion ("}, {"score":{"name":"@p","objective":"around_the_head_completion"}}, {"text":"/15)"}]
tellraw @p [""]
