scoreboard players add @p aquarium_saltwater_completion 1
tellraw @p ["", {"text":"Saltwater Completion ("}, {"score":{"name":"@p","objective":"aquarium_saltwater_completion"}}, {"text":"/3)"}]
tellraw @p [""]
