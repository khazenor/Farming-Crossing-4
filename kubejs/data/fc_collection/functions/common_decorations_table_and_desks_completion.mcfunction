scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/468)"}]
scoreboard players add @p common_decorations_table_and_desks_completion 1
tellraw @p ["", {"text":"Table and Desks Completion ("}, {"score":{"name":"@p","objective":"common_decorations_table_and_desks_completion"}}, {"text":"/10)"}]
tellraw @p [""]
