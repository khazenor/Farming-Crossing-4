scoreboard players add @p rare_decorations 1
tellraw @p ["", {"text":"New Rare Decoration Collected! Rare Decorations ("}, {"score":{"name":"@p","objective":"rare_decorations"}}, {"text":"/74)"}]