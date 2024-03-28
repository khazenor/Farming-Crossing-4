scoreboard players add @p common_decorations_bathroom_completion 1
tellraw @p ["", {"text":"Bathroom Completion ("}, {"score":{"name":"@p","objective":"common_decorations_bathroom_completion"}}, {"text":"/25)"}]
tellraw @p [""]
