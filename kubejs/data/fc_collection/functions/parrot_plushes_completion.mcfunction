scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/333)"}]
scoreboard players add @p parrot_plushes_completion 1
tellraw @p ["", {"text":"Parrot Plushes Completion ("}, {"score":{"name":"@p","objective":"parrot_plushes_completion"}}, {"text":"/5)"}]
tellraw @p [""]
