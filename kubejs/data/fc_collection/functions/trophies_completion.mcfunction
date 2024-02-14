scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/333)"}]
scoreboard players add @p trophies_completion 1
tellraw @p ["", {"text":"Trophies Completion ("}, {"score":{"name":"@p","objective":"trophies_completion"}}, {"text":"/9)"}]
tellraw @p [""]
