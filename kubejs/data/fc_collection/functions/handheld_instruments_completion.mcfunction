scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/333)"}]
scoreboard players add @p handheld_instruments_completion 1
tellraw @p ["", {"text":"Handheld Instruments Completion ("}, {"score":{"name":"@p","objective":"handheld_instruments_completion"}}, {"text":"/19)"}]
tellraw @p [""]
