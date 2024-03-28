scoreboard players add @p common_decorations_record_players_completion 1
tellraw @p ["", {"text":"Record Players Completion ("}, {"score":{"name":"@p","objective":"common_decorations_record_players_completion"}}, {"text":"/4)"}]
tellraw @p [""]
