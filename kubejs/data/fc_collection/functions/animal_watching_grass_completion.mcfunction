scoreboard players add @p animal_watching_grass_completion 1
tellraw @p ["", {"text":"Grass Completion ("}, {"score":{"name":"@p","objective":"animal_watching_grass_completion"}}, {"text":"/7)"}]
tellraw @p [""]
