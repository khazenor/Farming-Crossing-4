scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/171)"}]
scoreboard players add @p cooking_collection_farmers_delight_cooking_pot_recipes_completion 1
tellraw @p ["", {"text":"Farmers Delight Cooking Pot Recipes Completion ("}, {"score":{"name":"@p","objective":"cooking_collection_farmers_delight_cooking_pot_recipes_completion"}}, {"text":"/24)"}]
tellraw @p [""]
