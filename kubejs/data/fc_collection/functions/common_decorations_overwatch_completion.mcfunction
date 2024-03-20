scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/468)"}]
scoreboard players add @p common_decorations_overwatch_completion 1
tellraw @p ["", {"text":"Overwatch Completion ("}, {"score":{"name":"@p","objective":"common_decorations_overwatch_completion"}}, {"text":"/4)"}]
tellraw @p [""]
