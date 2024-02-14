scoreboard players add @p aquarium 1
tellraw @p ["", {"text":"New fish caught! Aquarium ("}, {"score":{"name":"@p","objective":"aquarium"}}, {"text":"/37)"}]
scoreboard players add @p aquarium_arid_completion 1
tellraw @p ["", {"text":"Arid Completion ("}, {"score":{"name":"@p","objective":"aquarium_arid_completion"}}, {"text":"/4)"}]
tellraw @p [""]
