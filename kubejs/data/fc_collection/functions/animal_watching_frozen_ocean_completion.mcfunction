scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"New animal observed! Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/120)"}]
scoreboard players add @p animal_watching_frozen_ocean_completion 1
tellraw @p ["", {"text":"Frozen Ocean Completion ("}, {"score":{"name":"@p","objective":"animal_watching_frozen_ocean_completion"}}, {"text":"/2)"}]
tellraw @p [""]
