scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/468)"}]
scoreboard players add @p common_decorations_lab_completion 1
tellraw @p ["", {"text":"Lab Completion ("}, {"score":{"name":"@p","objective":"common_decorations_lab_completion"}}, {"text":"/13)"}]
tellraw @p [""]
