scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/468)"}]
scoreboard players add @p common_decorations_mariachi_completion 1
tellraw @p ["", {"text":"Mariachi Completion ("}, {"score":{"name":"@p","objective":"common_decorations_mariachi_completion"}}, {"text":"/6)"}]
tellraw @p [""]
