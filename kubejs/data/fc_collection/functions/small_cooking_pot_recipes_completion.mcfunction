tellraw @p [""]
scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/207)"}]
scoreboard players add @p small_cooking_pot_recipes_completion 1
tellraw @p ["", {"text":"Small Cooking Pot Recipes Completion ("}, {"score":{"name":"@p","objective":"small_cooking_pot_recipes_completion"}}, {"text":"/8)"}]
