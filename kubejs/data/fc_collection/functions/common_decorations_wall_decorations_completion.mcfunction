scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/468)"}]
scoreboard players add @p common_decorations_wall_decorations_completion 1
tellraw @p ["", {"text":"Wall Decorations Completion ("}, {"score":{"name":"@p","objective":"common_decorations_wall_decorations_completion"}}, {"text":"/11)"}]
tellraw @p [""]
