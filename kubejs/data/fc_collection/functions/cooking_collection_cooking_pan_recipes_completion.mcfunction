scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/191)"}]
scoreboard players add @p cooking_collection_cooking_pan_recipes_completion 1
tellraw @p ["", {"text":"Cooking Pan Recipes Completion ("}, {"score":{"name":"@p","objective":"cooking_collection_cooking_pan_recipes_completion"}}, {"text":"/11)"}]
tellraw @p [""]