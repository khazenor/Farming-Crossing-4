scoreboard players add @p animal_watching_savanna_completion 1
tellraw @p ["", {"text":"Savanna Completion ("}, {"score":{"name":"@p","objective":"animal_watching_savanna_completion"}}, {"text":"/11)"}]
tellraw @p [""]
