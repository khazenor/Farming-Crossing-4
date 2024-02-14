scoreboard players add @p rare_decorations 1
tellraw @p ["", {"text":"New Rare Decoration Collected! Rare Decorations ("}, {"score":{"name":"@p","objective":"rare_decorations"}}, {"text":"/74)"}]
scoreboard players add @p rare_decorations_mob_trophies_completion 1
tellraw @p ["", {"text":"Mob Trophies Completion ("}, {"score":{"name":"@p","objective":"rare_decorations_mob_trophies_completion"}}, {"text":"/7)"}]
tellraw @p [""]
