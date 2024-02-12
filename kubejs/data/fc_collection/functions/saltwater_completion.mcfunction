scoreboard players add @p aquarium 1
tellraw @p ["", {"text":"New fish caught! Aquarium ("}, {"score":{"name":"@p","objective":"aquarium"}}, {"text":"/37)"}]
scoreboard players add @p saltwater_completion 1
tellraw @p ["", {"text":"Saltwater Completion ("}, {"score":{"name":"@p","objective":"saltwater_completion"}}, {"text":"/3)"}]
tellraw @p [""]
