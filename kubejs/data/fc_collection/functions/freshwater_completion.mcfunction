scoreboard players add @p aquarium 1
tellraw @p ["", {"text":"New fish caught! Aquarium ("}, {"score":{"name":"@p","objective":"aquarium"}}, {"text":"/37)"}]
scoreboard players add @p freshwater_completion 1
tellraw @p ["", {"text":"Freshwater Completion ("}, {"score":{"name":"@p","objective":"freshwater_completion"}}, {"text":"/9)"}]
tellraw @p [""]
