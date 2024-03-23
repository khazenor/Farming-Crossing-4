scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/120)"}]
scoreboard players add @p animal_watching_savanna_completion 1
tellraw @p ["", {"text":"Savanna Completion ("}, {"score":{"name":"@p","objective":"animal_watching_savanna_completion"}}, {"text":"/11)"}]
tellraw @p [""]
