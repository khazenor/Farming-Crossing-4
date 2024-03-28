scoreboard players add @p animal_watching_desert_completion 1
tellraw @p ["", {"text":"Desert Completion ("}, {"score":{"name":"@p","objective":"animal_watching_desert_completion"}}, {"text":"/7)"}]
tellraw @p [""]
