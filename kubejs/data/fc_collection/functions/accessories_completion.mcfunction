scoreboard players add @p hat_collection 1
tellraw @p ["", {"text":"New hat obtained! Hat Collection ("}, {"score":{"name":"@p","objective":"hat_collection"}}, {"text":"/234)"}]
scoreboard players add @p accessories_completion 1
tellraw @p ["", {"text":"Accessories Completion ("}, {"score":{"name":"@p","objective":"accessories_completion"}}, {"text":"/13)"}]
tellraw @p [""]
