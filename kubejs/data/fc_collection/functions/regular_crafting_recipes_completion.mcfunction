tellraw @p [""]
scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/290)"}]
scoreboard players add @p regular_crafting_recipes_completion 1
tellraw @p ["", {"text":"Regular Crafting Recipes Completion ("}, {"score":{"name":"@p","objective":"regular_crafting_recipes_completion"}}, {"text":"/6)"}]
