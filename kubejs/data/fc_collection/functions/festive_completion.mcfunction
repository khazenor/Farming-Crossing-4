scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/333)"}]
scoreboard players add @p festive_completion 1
tellraw @p ["", {"text":"Festive Completion ("}, {"score":{"name":"@p","objective":"festive_completion"}}, {"text":"/19)"}]
tellraw @p [""]
