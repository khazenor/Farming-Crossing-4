scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/175)"}]
scoreboard players add @p cooking_collection_alexs_delight_cooking_pot_recipes_completion 1
tellraw @p ["", {"text":"Alex's Delight Cooking Pot Recipes Completion ("}, {"score":{"name":"@p","objective":"cooking_collection_alexs_delight_cooking_pot_recipes_completion"}}, {"text":"/4)"}]
tellraw @p [""]
