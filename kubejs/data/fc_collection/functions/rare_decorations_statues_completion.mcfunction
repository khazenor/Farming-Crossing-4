scoreboard players add @p rare_decorations 1
tellraw @p ["", {"text":"New Rare Decoration Collected! Rare Decorations ("}, {"score":{"name":"@p","objective":"rare_decorations"}}, {"text":"/74)"}]
scoreboard players add @p rare_decorations_statues_completion 1
tellraw @p ["", {"text":"Statues Completion ("}, {"score":{"name":"@p","objective":"rare_decorations_statues_completion"}}, {"text":"/10)"}]
tellraw @p [""]
