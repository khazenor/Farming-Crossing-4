scoreboard players add @p animal_watching_general_water_completion 1
tellraw @p ["", {"text":"General Water Completion ("}, {"score":{"name":"@p","objective":"animal_watching_general_water_completion"}}, {"text":"/5)"}]
tellraw @p [""]
