scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
scoreboard players add @p desert_completion 1
tellraw @p ["", {"text":"Desert Completion ("}, {"score":{"name":"@p","objective":"desert_completion"}}, {"text":"/6)"}]
tellraw @p [""]
