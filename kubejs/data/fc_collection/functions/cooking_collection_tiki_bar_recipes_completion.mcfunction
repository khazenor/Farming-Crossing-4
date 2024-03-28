scoreboard players add @p cooking_collection 1
tellraw @p ["", {"text":"New dish cooked! Cooking Collection ("}, {"score":{"name":"@p","objective":"cooking_collection"}}, {"text":"/175)"}]
scoreboard players add @p cooking_collection_tiki_bar_recipes_completion 1
tellraw @p ["", {"text":"Tiki Bar Recipes Completion ("}, {"score":{"name":"@p","objective":"cooking_collection_tiki_bar_recipes_completion"}}, {"text":"/9)"}]
tellraw @p [""]
