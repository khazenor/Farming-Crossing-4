scoreboard players add @p animal_watching_river_completion 1
tellraw @p ["", {"text":"River Completion ("}, {"score":{"name":"@p","objective":"animal_watching_river_completion"}}, {"text":"/8)"}]
tellraw @p [""]
