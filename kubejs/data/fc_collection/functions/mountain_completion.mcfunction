scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
scoreboard players add @p mountain_completion 1
tellraw @p ["", {"text":"Mountain Completion ("}, {"score":{"name":"@p","objective":"mountain_completion"}}, {"text":"/1)"}]
tellraw @p [""]
