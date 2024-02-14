scoreboard players add @p aquarium 1
tellraw @p ["", {"text":"New fish caught! Aquarium ("}, {"score":{"name":"@p","objective":"aquarium"}}, {"text":"/37)"}]
scoreboard players add @p aquarium_artic_completion 1
tellraw @p ["", {"text":"Artic Completion ("}, {"score":{"name":"@p","objective":"aquarium_artic_completion"}}, {"text":"/8)"}]
tellraw @p [""]
