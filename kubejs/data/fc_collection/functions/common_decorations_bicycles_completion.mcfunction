scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/468)"}]
scoreboard players add @p common_decorations_bicycles_completion 1
tellraw @p ["", {"text":"Bicycles Completion ("}, {"score":{"name":"@p","objective":"common_decorations_bicycles_completion"}}, {"text":"/8)"}]
tellraw @p [""]
