scoreboard players add @p hat_collection 1
tellraw @p ["", {"text":"New hat obtained! Hat Collection ("}, {"score":{"name":"@p","objective":"hat_collection"}}, {"text":"/234)"}]
scoreboard players add @p face_overings_completion 1
tellraw @p ["", {"text":"Face Overings Completion ("}, {"score":{"name":"@p","objective":"face_overings_completion"}}, {"text":"/30)"}]
tellraw @p [""]
