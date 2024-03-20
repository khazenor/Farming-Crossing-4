scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/468)"}]
scoreboard players add @p common_decorations_record_players_completion 1
tellraw @p ["", {"text":"Record Players Completion ("}, {"score":{"name":"@p","objective":"common_decorations_record_players_completion"}}, {"text":"/4)"}]
tellraw @p [""]
