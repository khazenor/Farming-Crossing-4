scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/333)"}]
scoreboard players add @p common_decorations_bathroom_completion 1
tellraw @p ["", {"text":"Bathroom Completion ("}, {"score":{"name":"@p","objective":"common_decorations_bathroom_completion"}}, {"text":"/25)"}]
tellraw @p [""]
