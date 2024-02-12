scoreboard players add @p aquarium 1
tellraw @p ["", {"text":"New fish caught! Aquarium ("}, {"score":{"name":"@p","objective":"aquarium"}}, {"text":"/37)"}]
scoreboard players add @p artic_completion 1
tellraw @p ["", {"text":"Artic Completion ("}, {"score":{"name":"@p","objective":"artic_completion"}}, {"text":"/8)"}]
tellraw @p [""]
