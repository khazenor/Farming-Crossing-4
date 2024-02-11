tellraw @p [""]
scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/296)"}]
scoreboard players add @p mini_fridge_recipes_completion 1
tellraw @p ["", {"text":"Mini Fridge Recipes Completion ("}, {"score":{"name":"@p","objective":"mini_fridge_recipes_completion"}}, {"text":"/8)"}]
