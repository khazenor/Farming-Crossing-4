scoreboard players add @p animal_watching_swamp_completion 1
tellraw @p ["", {"text":"Swamp Completion ("}, {"score":{"name":"@p","objective":"animal_watching_swamp_completion"}}, {"text":"/6)"}]
tellraw @p [""]
