scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/215)"}]
scoreboard players add @p baking_station_recipes_completion 1
tellraw @p ["", {"text":"Baking Station Recipes Completion ("}, {"score":{"name":"@p","objective":"baking_station_recipes_completion"}}, {"text":"/9)"}]
tellraw @p [""]
