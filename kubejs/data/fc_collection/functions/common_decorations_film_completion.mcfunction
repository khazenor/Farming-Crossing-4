scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/333)"}]
scoreboard players add @p common_decorations_film_completion 1
tellraw @p ["", {"text":"Film Completion ("}, {"score":{"name":"@p","objective":"common_decorations_film_completion"}}, {"text":"/7)"}]
tellraw @p [""]
