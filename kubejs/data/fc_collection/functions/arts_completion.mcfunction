scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/333)"}]
scoreboard players add @p arts_completion 1
tellraw @p ["", {"text":"Arts Completion ("}, {"score":{"name":"@p","objective":"arts_completion"}}, {"text":"/14)"}]
tellraw @p [""]
