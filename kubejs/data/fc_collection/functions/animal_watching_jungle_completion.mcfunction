scoreboard players add @p animal_watching_jungle_completion 1
tellraw @p ["", {"text":"Jungle Completion ("}, {"score":{"name":"@p","objective":"animal_watching_jungle_completion"}}, {"text":"/12)"}]
tellraw @p [""]
