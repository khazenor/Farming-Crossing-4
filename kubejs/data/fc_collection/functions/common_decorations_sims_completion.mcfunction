scoreboard players add @p common_decorations_sims_completion 1
tellraw @p ["", {"text":"Sims Completion ("}, {"score":{"name":"@p","objective":"common_decorations_sims_completion"}}, {"text":"/4)"}]
tellraw @p [""]
