scoreboard players add @p animal_watching_forest_completion 1
tellraw @p ["", {"text":"Forest Completion ("}, {"score":{"name":"@p","objective":"animal_watching_forest_completion"}}, {"text":"/17)"}]
tellraw @p [""]
