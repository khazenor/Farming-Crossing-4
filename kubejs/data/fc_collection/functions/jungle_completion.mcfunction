scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
scoreboard players add @p jungle_completion 1
tellraw @p ["", {"text":"Jungle Completion ("}, {"score":{"name":"@p","objective":"jungle_completion"}}, {"text":"/12)"}]
tellraw @p [""]
