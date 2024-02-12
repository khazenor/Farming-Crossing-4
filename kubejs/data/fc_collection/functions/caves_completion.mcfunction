scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
scoreboard players add @p caves_completion 1
tellraw @p ["", {"text":"Caves Completion ("}, {"score":{"name":"@p","objective":"caves_completion"}}, {"text":"/5)"}]
tellraw @p [""]
