scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
scoreboard players add @p swamp_completion 1
tellraw @p ["", {"text":"Swamp Completion ("}, {"score":{"name":"@p","objective":"swamp_completion"}}, {"text":"/6)"}]
tellraw @p [""]
