scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/191)"}]
scoreboard players add @p cooking_collection_mini_fridge_recipes_completion 1
tellraw @p ["", {"text":"Mini Fridge Recipes Completion ("}, {"score":{"name":"@p","objective":"cooking_collection_mini_fridge_recipes_completion"}}, {"text":"/8)"}]
tellraw @p [""]