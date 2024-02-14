scoreboard players add @p rare_decorations 1
tellraw @p ["", {"text":"New Rare Decoration Collected! Rare Decorations ("}, {"score":{"name":"@p","objective":"rare_decorations"}}, {"text":"/74)"}]
scoreboard players add @p paintings_completion 1
tellraw @p ["", {"text":"Paintings Completion ("}, {"score":{"name":"@p","objective":"paintings_completion"}}, {"text":"/6)"}]
tellraw @p [""]
