scoreboard players add @p common_decorations 1
tellraw @p ["", {"text":"New Common Decoration Collected! Common Decorations ("}, {"score":{"name":"@p","objective":"common_decorations"}}, {"text":"/333)"}]
scoreboard players add @p common_decorations_books_and_exploration_completion 1
tellraw @p ["", {"text":"Books and Exploration Completion ("}, {"score":{"name":"@p","objective":"common_decorations_books_and_exploration_completion"}}, {"text":"/10)"}]
tellraw @p [""]
