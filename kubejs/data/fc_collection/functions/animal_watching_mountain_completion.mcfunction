scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/119)"}]
scoreboard players add @p animal_watching_mountain_completion 1
tellraw @p ["", {"text":"Mountain Completion ("}, {"score":{"name":"@p","objective":"animal_watching_mountain_completion"}}, {"text":"/2)"}]
tellraw @p [""]
