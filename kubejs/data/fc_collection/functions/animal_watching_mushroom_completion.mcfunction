scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/120)"}]
scoreboard players add @p animal_watching_mushroom_completion 1
tellraw @p ["", {"text":"Mushroom Completion ("}, {"score":{"name":"@p","objective":"animal_watching_mushroom_completion"}}, {"text":"/3)"}]
tellraw @p [""]
