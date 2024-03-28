scoreboard players add @p common_decorations_village_plushes_completion 1
tellraw @p ["", {"text":"Village Plushes Completion ("}, {"score":{"name":"@p","objective":"common_decorations_village_plushes_completion"}}, {"text":"/10)"}]
tellraw @p [""]
