scoreboard players add @p aquarium 1
tellraw @p ["", {"text":"New fish caught! Aquarium ("}, {"score":{"name":"@p","objective":"aquarium"}}, {"text":"/37)"}]
scoreboard players add @p mushroom_completion 1
tellraw @p ["", {"text":"Mushroom Completion ("}, {"score":{"name":"@p","objective":"mushroom_completion"}}, {"text":"/2)"}]
tellraw @p [""]
