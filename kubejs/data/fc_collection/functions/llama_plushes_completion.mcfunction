scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/333)"}]
scoreboard players add @p llama_plushes_completion 1
tellraw @p ["", {"text":"Llama Plushes Completion ("}, {"score":{"name":"@p","objective":"llama_plushes_completion"}}, {"text":"/4)"}]
tellraw @p [""]
