scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/191)"}]
scoreboard players add @p animal_watching 1
tellraw @p ["", {"text":"Animal Watching ("}, {"score":{"name":"@p","objective":"animal_watching"}}, {"text":"/115)"}]
