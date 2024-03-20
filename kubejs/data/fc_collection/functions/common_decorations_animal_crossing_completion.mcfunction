scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/468)"}]
scoreboard players add @p common_decorations_animal_crossing_completion 1
tellraw @p ["", {"text":"Animal Crossing Completion ("}, {"score":{"name":"@p","objective":"common_decorations_animal_crossing_completion"}}, {"text":"/27)"}]
tellraw @p [""]
