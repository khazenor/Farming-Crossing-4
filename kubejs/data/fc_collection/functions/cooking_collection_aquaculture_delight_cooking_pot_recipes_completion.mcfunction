scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/191)"}]
scoreboard players add @p cooking_collection_aquaculture_delight_cooking_pot_recipes_completion 1
tellraw @p ["", {"text":"Aquaculture Delight Cooking Pot Recipes Completion ("}, {"score":{"name":"@p","objective":"cooking_collection_aquaculture_delight_cooking_pot_recipes_completion"}}, {"text":"/11)"}]
tellraw @p [""]
