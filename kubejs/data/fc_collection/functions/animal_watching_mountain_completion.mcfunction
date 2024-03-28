scoreboard players add @p animal_watching_mountain_completion 1
tellraw @p ["", {"text":"Mountain Completion ("}, {"score":{"name":"@p","objective":"animal_watching_mountain_completion"}}, {"text":"/2)"}]
tellraw @p [""]
