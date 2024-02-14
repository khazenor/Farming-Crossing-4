scoreboard players add @p rare_decorations 1
tellraw @p ["", {"text":"New Rare Decoration Collected! Rare Decorations ("}, {"score":{"name":"@p","objective":"rare_decorations"}}, {"text":"/74)"}]
scoreboard players add @p oneul_food_music_discs_completion 1
tellraw @p ["", {"text":"Oneul Food Music Discs Completion ("}, {"score":{"name":"@p","objective":"oneul_food_music_discs_completion"}}, {"text":"/7)"}]
tellraw @p [""]
