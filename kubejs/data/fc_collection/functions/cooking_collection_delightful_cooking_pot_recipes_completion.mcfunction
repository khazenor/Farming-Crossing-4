scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/175)"}]
scoreboard players add @p cooking_collection_delightful_cooking_pot_recipes_completion 1
tellraw @p ["", {"text":"Delightful Cooking Pot Recipes Completion ("}, {"score":{"name":"@p","objective":"cooking_collection_delightful_cooking_pot_recipes_completion"}}, {"text":"/10)"}]
tellraw @p [""]
