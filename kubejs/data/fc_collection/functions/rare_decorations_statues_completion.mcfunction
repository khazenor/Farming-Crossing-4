scoreboard players add @p rare_decorations_statues_completion 1
tellraw @p ["", {"text":"Statues Completion ("}, {"score":{"name":"@p","objective":"rare_decorations_statues_completion"}}, {"text":"/10)"}]
tellraw @p [""]
