scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/362)"}]
scoreboard players add @p cuisine_delight_recipes_completion 1
tellraw @p ["", {"text":"Cuisine Delight Recipes Completion ("}, {"score":{"name":"@p","objective":"cuisine_delight_recipes_completion"}}, {"text":"/20)"}]
tellraw @p [""]
