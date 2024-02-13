scoreboard players add @p hat_collection 1
tellraw @p ["", {"text":"New hat obtained! Hat Collection ("}, {"score":{"name":"@p","objective":"hat_collection"}}, {"text":"/234)"}]
scoreboard players add @p head_toppers_completion 1
tellraw @p ["", {"text":"Head Toppers Completion ("}, {"score":{"name":"@p","objective":"head_toppers_completion"}}, {"text":"/25)"}]
tellraw @p [""]
