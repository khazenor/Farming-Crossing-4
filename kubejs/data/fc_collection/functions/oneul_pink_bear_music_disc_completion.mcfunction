scoreboard players add @p rare_decorations 1
tellraw @p ["", {"text":"New Rare Decoration Collected! Rare Decorations ("}, {"score":{"name":"@p","objective":"rare_decorations"}}, {"text":"/74)"}]
scoreboard players add @p oneul_pink_bear_music_disc_completion 1
tellraw @p ["", {"text":"Oneul Pink Bear Music Disc Completion ("}, {"score":{"name":"@p","objective":"oneul_pink_bear_music_disc_completion"}}, {"text":"/26)"}]
tellraw @p [""]
