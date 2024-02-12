scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
scoreboard players add @p beaches_completion 1
tellraw @p ["", {"text":"Beaches Completion ("}, {"score":{"name":"@p","objective":"beaches_completion"}}, {"text":"/9)"}]
tellraw @p [""]
