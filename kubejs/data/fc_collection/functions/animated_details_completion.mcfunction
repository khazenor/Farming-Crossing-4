scoreboard players add @p hat_collection 1
tellraw @p ["", {"text":"New hat obtained! Hat Collection ("}, {"score":{"name":"@p","objective":"hat_collection"}}, {"text":"/234)"}]
scoreboard players add @p animated_details_completion 1
tellraw @p ["", {"text":"Animated Details Completion ("}, {"score":{"name":"@p","objective":"animated_details_completion"}}, {"text":"/18)"}]
tellraw @p [""]
