scoreboard players add @p rare_decorations 1
tellraw @p ["", {"text":"New Rare Decoration Collected! Rare Decorations ("}, {"score":{"name":"@p","objective":"rare_decorations"}}, {"text":"/74)"}]
scoreboard players add @p misc_completion 1
tellraw @p ["", {"text":"Misc Completion ("}, {"score":{"name":"@p","objective":"misc_completion"}}, {"text":"/7)"}]
tellraw @p [""]
