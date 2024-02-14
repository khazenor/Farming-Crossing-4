scoreboard players add @p rare_decorations 1
tellraw @p ["", {"text":"New Rare Decoration Collected! Rare Decorations ("}, {"score":{"name":"@p","objective":"rare_decorations"}}, {"text":"/74)"}]
scoreboard players add @p rare_decorations_oneul_misc_music_disc_completion 1
tellraw @p ["", {"text":"Oneul Misc Music Disc Completion ("}, {"score":{"name":"@p","objective":"rare_decorations_oneul_misc_music_disc_completion"}}, {"text":"/11)"}]
tellraw @p [""]
