scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/333)"}]
scoreboard players add @p axolotl_plushes_completion 1
tellraw @p ["", {"text":"Axolotl Plushes Completion ("}, {"score":{"name":"@p","objective":"axolotl_plushes_completion"}}, {"text":"/5)"}]
tellraw @p [""]
