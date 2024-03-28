scoreboard players add @p aquarium_freshwater_completion 1
tellraw @p ["", {"text":"Freshwater Completion ("}, {"score":{"name":"@p","objective":"aquarium_freshwater_completion"}}, {"text":"/9)"}]
tellraw @p [""]
