scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/468)"}]
scoreboard players add @p common_decorations_cat_plushes_completion 1
tellraw @p ["", {"text":"Cat Plushes Completion ("}, {"score":{"name":"@p","objective":"common_decorations_cat_plushes_completion"}}, {"text":"/12)"}]
tellraw @p [""]
