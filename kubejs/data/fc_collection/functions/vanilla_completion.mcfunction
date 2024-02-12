scoreboard players add @p aquarium 1
tellraw @p ["", {"text":"New fish caught! Aquarium ("}, {"score":{"name":"@p","objective":"aquarium"}}, {"text":"/37)"}]
scoreboard players add @p vanilla_completion 1
tellraw @p ["", {"text":"Vanilla Completion ("}, {"score":{"name":"@p","objective":"vanilla_completion"}}, {"text":"/4)"}]
tellraw @p [""]
