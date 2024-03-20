scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/468)"}]
scoreboard players add @p common_decorations_starbound_completion 1
tellraw @p ["", {"text":"Starbound Completion ("}, {"score":{"name":"@p","objective":"common_decorations_starbound_completion"}}, {"text":"/14)"}]
tellraw @p [""]
