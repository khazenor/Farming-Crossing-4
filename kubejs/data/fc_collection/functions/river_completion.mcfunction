scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
scoreboard players add @p river_completion 1
tellraw @p ["", {"text":"River Completion ("}, {"score":{"name":"@p","objective":"river_completion"}}, {"text":"/8)"}]
tellraw @p [""]
