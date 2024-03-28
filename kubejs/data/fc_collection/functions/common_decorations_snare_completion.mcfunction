scoreboard players add @p common_decorations_snare_completion 1
tellraw @p ["", {"text":"Snare Completion ("}, {"score":{"name":"@p","objective":"common_decorations_snare_completion"}}, {"text":"/16)"}]
tellraw @p [""]
