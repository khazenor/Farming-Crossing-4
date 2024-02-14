scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/191)"}]
scoreboard players add @p cooking_collection_oven_recipes_completion 1
tellraw @p ["", {"text":"Oven Recipes Completion ("}, {"score":{"name":"@p","objective":"cooking_collection_oven_recipes_completion"}}, {"text":"/16)"}]
tellraw @p [""]
