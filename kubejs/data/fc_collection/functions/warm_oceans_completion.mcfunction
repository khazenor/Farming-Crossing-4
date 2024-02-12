scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
scoreboard players add @p warm_oceans_completion 1
tellraw @p ["", {"text":"Warm Oceans Completion ("}, {"score":{"name":"@p","objective":"warm_oceans_completion"}}, {"text":"/2)"}]
tellraw @p [""]
