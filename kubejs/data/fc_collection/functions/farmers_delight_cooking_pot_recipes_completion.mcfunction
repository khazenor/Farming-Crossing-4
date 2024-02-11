tellraw @p [""]
scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/338)"}]
scoreboard players add @p farmers_delight_cooking_pot_recipes_completion 1
tellraw @p ["", {"text":"Farmers Delight Cooking Pot Recipes Completion ("}, {"score":{"name":"@p","objective":"farmers_delight_cooking_pot_recipes_completion"}}, {"text":"/24)"}]
