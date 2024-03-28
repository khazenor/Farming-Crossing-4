scoreboard players add @p aquarium_swamp_completion 1
tellraw @p ["", {"text":"Swamp Completion ("}, {"score":{"name":"@p","objective":"aquarium_swamp_completion"}}, {"text":"/3)"}]
tellraw @p [""]
